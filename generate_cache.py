#!/usr/bin/env python3

# This script will generate package metadata files for
# each package in the latest version of spack
#
# Usage:
# python generate_cache.py

from collections import defaultdict
from contextlib import contextmanager
from functools import lru_cache
from pathlib import Path
from typing import Set
import git
import json
import os
import os
import requests
import shutil
import sys
import tempfile
import yaml

import spack.database
import spack.repo
import spack.spec

here = os.getcwd()
db_root = os.path.join(here, "spack-db")


def write_json(content, filename):
    with open(filename, "w") as outfile:
        outfile.write(json.dumps(content, indent=4))


def read_yaml(filename):
    with open(filename, "r") as stream:
        content = yaml.safe_load(stream)
    return content


# Template for cache data
template = """---
title: "%s"
layout: cache
categories: [package, %s]
meta: %s
spec_files: 
 - %s
spec_details: %s
spec_names:
 - %s
---"""

def binary_size(spec):
    # TODO: fetch at build time
    return 1024 * 1024


@contextmanager
def git_repo_context(repo_url):
    """
    A context manager that clones a Git repository into a temporary directory, and
    provides a reference to the repository object for use within the context.

    :param repo_url: The URL of the repository to clone.
    """
    temp_dir = tempfile.mkdtemp()

    try:
        repo = git.Repo.clone_from(repo_url, temp_dir)
        yield repo
    finally:
        shutil.rmtree(temp_dir)


@lru_cache
def get_version_stacks(repo: git.Repo, tag: str) -> Set[str]:
    repo.git.checkout(tag)
    stacks_dir = (
        Path(repo.working_dir)
        / "share"
        / "spack"
        / "gitlab"
        / "cloud_pipelines"
        / "stacks"
    )
    return set(os.listdir(stacks_dir))

def get_hash_stacks(repo: git.Repo, tag: str) -> dict[str, set[str]]:
    hash_stacks = defaultdict(set)

    for stack in get_version_stacks(repo, tag):
        url = f'https://binaries.spack.io/{tag}/{stack}/build_cache/index.json'
        r = requests.get(url)
        if r.status_code == 404:
            print(f'No build cache for {tag} {stack} ({url})')
            continue
        else:
            r.raise_for_status()

        for hash in r.json()['database']['installs'].keys():
            hash_stacks[hash].add(stack)

    return hash_stacks


def write_cache_entries(name, specs, hash_stacks):
    """
    Given a named list of specs, write markdown and json to cache output directory.
    """
    # For each spec, write to the _cache folder
    for package_name, speclist in specs.items():
        # Keep a set of summary metrics for a spec
        metrics = {
            "versions": set(),
            "compilers": set(),
            "arches": set(),
            "stacks": set(),
        }

        package_dir = os.path.join(here, "_cache", name, package_name)
        if not os.path.exists(package_dir):
            os.makedirs(package_dir)
        spec_files = []
        spec_names = []
        spec_details = []
        for i, spec in enumerate(speclist):
            metrics["arches"].add(str(spec.architecture))
            metrics["versions"].add(str(spec.version))
            metrics["compilers"].add(str(spec.compiler))
            metrics["stacks"] |= hash_stacks[spec._hash]
            spec_name = "spec-%s.json" % i
            spec_file = os.path.join(package_dir, spec_name)
            write_json(spec.to_dict(), spec_file)
            spec_files.append(spec_name)
            spec_details.append(
                {
                    "hash": spec._hash,
                    "compiler": str(spec.compiler),
                    "versions": [str(v) for v in spec.versions],
                    "arches": str(spec.architecture),
                    "variants": list(spec.variants.keys()),
                    "stacks": list(hash_stacks[spec._hash]),
                    "size": binary_size(spec),
                }
            )
            spec_names.append("'" + str(spec) + "'")
        metrics["arches"] = sorted(list(metrics["arches"]))
        metrics["versions"] = sorted(list(metrics["versions"]))
        metrics["compilers"] = sorted(list(metrics["compilers"]))
        metrics["stacks"] = sorted(list(metrics["stacks"]))
        render = template % (
            package_name,
            name,
            json.dumps(metrics),
            " - ".join([x + "\n" for x in spec_files]).strip(),
            json.dumps(spec_details),
            " - ".join([x + "\n" for x in spec_names]).strip(),
        )
        md_file = os.path.join(package_dir, "specs.md")
        with open(md_file, "w") as fd:
            fd.write(render)


def load_spack_db(name, url):
    """
    Given a named entry and a URL, load a spack database
    """
    response = requests.get(url)

    if response.status_code != 200:
        sys.exit(
            "Issue with request to get package index: %s %s" % (url, response.reason)
        )
    index = response.json()

    # Write index.json to file
    entry_db = os.path.join(db_root, name)
    if not os.path.exists(entry_db):
        os.makedirs(entry_db)
    write_json(index, os.path.join(entry_db, "index.json"))

    # yeah this is awkward <--- from @tgamblin :D
    db = spack.database.Database(None, entry_db)

    # Organize specs by package
    specs = {}

    # keep lookup of specs
    with db.read_transaction():
        for record in db._data.values():
            specs.setdefault(record.spec.name, []).append(record.spec)
    return index, specs


def get_specs_metadata(specs):
    """
    Given loaded specs, parse metadata and return dict lookup.
    """
    # For funsies store top level metrics
    updates = {}
    parameters = {}
    compilers = {}
    arches = {"platform": {}, "platform_os": {}, "compiler": {}, "target": {}}
    count = 0

    # For each package, generate a data page, including the spec.json
    for package_name, speclist in specs.items():
        for s in speclist:
            count += 1
            nodes = s.to_dict()["spec"]["nodes"]
            for spec in nodes:
                for paramname, setting in spec["parameters"].items():

                    # Is true or not empty list
                    if setting:
                        if paramname not in parameters:
                            parameters[paramname] = 0
                        parameters[paramname] += 1

                for key, value in spec["arch"].items():

                    # Target can have another level of nesting
                    if key == "target" and isinstance(value, dict):
                        value = "%s %s" % (value["vendor"], value["name"])
                    if value not in arches[key]:
                        arches[key][value] = 0
                    arches[key][value] += 1

                compiler = "%s@%s" % (
                    spec["compiler"]["name"],
                    spec["compiler"]["version"],
                )
                if compiler not in compilers:
                    compilers[compiler] = 0
                compilers[compiler] += 1

        # For each meta, write to data file
        updates["compilers"] = compilers
        updates["parameters"] = parameters
        updates["arches"] = arches
        updates["parameter_count"] = "{:,}".format(len(parameters))
        updates["compiler_count"] = "{:,}".format(len(compilers))
        updates["count"] = count
    return updates


def main():

    tags_file = os.path.join(here, "_data", "tags.yaml")
    if not os.path.exists(tags_file):
        sys.exit(f"{tags_file} does not exist.")

    # Metadata file will store all versions
    meta = {}
    tags = read_yaml(tags_file)
    with git_repo_context("https://github.com/spack/spack") as repo:
        for entry in tags.get("tags", []):
            if "name" not in entry or "url" not in entry or "tag" not in entry:
                sys.exit(f"Malformed entry {entry} missing url or tag or name.")
            name = entry["name"]
            tag = entry["tag"]
            url = entry["url"]
            print(f"Parsing cache for {name}")

            # Create spack database and load specs
            print('Loading spack db')
            index, specs = load_spack_db(name, url)

            print('Getting hash stacks')
            hash_stacks = get_hash_stacks(repo, tag)

            # Update metadata file
            meta[name] = {
                "version": index["database"]["version"],
                "count": len(index["database"]["installs"]),
            }
            del index

            # Get metadata for specs
            print('Getting specs metadata')
            updates = get_specs_metadata(specs)
            meta[name].update(updates)

            # Write jekyll files
            print('Writing jekyll files')
            write_cache_entries(name, specs, hash_stacks)

    # Create the "all" group
    meta["all"] = {"version": "all", "count": 0}
    compilers = {}
    parameters = {}

    # Count total compilers, params, specs
    for k, entry in meta.items():
        if k == "all":
            continue
        meta["all"]["count"] += entry["count"]
        for compiler, ccount in entry["compilers"].items():
            if compiler not in compilers:
                compilers[compiler] = 0
            compilers[compiler] += ccount
        for param, pcount in entry["parameters"].items():
            if param not in parameters:
                parameters[param] = 0
            parameters[param] += pcount

    meta["all"]["compiler_count"] = "{:,}".format(len(compilers))
    meta["all"]["parameter_count"] = "{:,}".format(len(parameters))

    # Save all metadata
    meta_file = os.path.join(here, "_data", "meta.yaml")
    with open(meta_file, "w") as fd:
        fd.write(yaml.dump(meta))


if __name__ == "__main__":
    main()
