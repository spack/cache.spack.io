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
import requests
import shutil
import sys
import tempfile
import yaml

import spack.database
import spack.repo
import spack.spec
import spack.binary_distribution

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
spec_details: %s
---"""


def binary_size(spec):
    # TODO: blocked on this value being baked into the build cache index.json
    return "-"


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
def get_version_stacks(repo: git.Repo, name: str) -> Set[str]:
    repo.git.checkout(name)

    stacks_dir = (
        Path(repo.working_dir)
        / "share"
        / "spack"
        / "gitlab"
        / "cloud_pipelines"
        / "stacks"
    )
    return set(os.listdir(stacks_dir))


def get_hash_stacks(repo: git.Repo, name: str) -> dict[str, set[str]]:
    hash_stacks = defaultdict(set)

    if name != "develop":
        name = f"releases/{name}"

    for stack in get_version_stacks(repo, name):
        url = f"https://binaries.spack.io/{name}/{stack}/build_cache/index.json"
        r = requests.get(url)
        if r.status_code == 404:
            print(f"No build cache for {name} {stack} ({url})")
            continue
        else:
            r.raise_for_status()

        for hash in r.json()["database"]["installs"].keys():
            hash_stacks[hash].add(stack)

    return hash_stacks


def write_cache_entries(name, specs, hash_stacks):
    """
    Given a named list of specs, write markdown and json to cache output directory.
    """
    # For each spec, write to the _cache folder
    for package_name, speclist in specs.items():
        # Keep a set of summary metrics for a package
        metrics = {
            "versions": set(),
            "compilers": set(),
            "oss": set(),
            "platforms": set(),
            "targets": set(),
            "stacks": set(),
            "num_specs": 0,
            "num_specs_by_stack": defaultdict(int),
        }

        package_dir = os.path.join(here, "_cache", name, package_name)
        if not os.path.exists(package_dir):
            os.makedirs(package_dir)
        spec_details = []
        for i, spec in enumerate(speclist):
            metrics["oss"].add(spec.architecture.os)
            metrics["platforms"].add(spec.architecture.platform)
            metrics["targets"].add(spec.architecture.target.name)
            metrics["versions"].add(str(spec.version))
            metrics["compilers"].add(str(spec.compiler))
            metrics["stacks"] |= hash_stacks[spec._hash]
            metrics["num_specs"] += 1

            for stack in hash_stacks[spec._hash]:
                metrics["num_specs_by_stack"][stack] += 1

            spec_name = "spec-%s.json" % i
            assert len(spec.versions) == 1, spec.versions
            tarball_dir = spack.binary_distribution.tarball_directory_name(spec)
            tarball_name = spack.binary_distribution.tarball_name(spec, ".spack")
            release_prefix = "releases/" if name != "develop" else ""
            tarball = f"{release_prefix}{name}/build_cache/{tarball_dir}/{tarball_name}"
            tarball_url = f"https://binaries.spack.io/{tarball}"
            spec_details.append(
                {
                    "hash": spec._hash,
                    "compiler": str(spec.compiler),
                    "versions": [str(v) for v in spec.versions],
                    "os": spec.architecture.os,
                    "platform": spec.architecture.platform,
                    "target": spec.architecture.target.name,
                    "variants": [str(v) for v in spec.variants.values()],
                    "stacks": list(hash_stacks[spec._hash]),
                    "size": binary_size(spec),
                    "tarball": tarball_url,
                }
            )
        metrics["oss"] = sorted(list(metrics["oss"]))
        metrics["platforms"] = sorted(list(metrics["platforms"]))
        metrics["targets"] = sorted(list(metrics["targets"]))
        metrics["versions"] = sorted(list(metrics["versions"]))
        metrics["compilers"] = sorted(list(metrics["compilers"]))
        metrics["stacks"] = sorted(list(metrics["stacks"]))
        render = template % (
            package_name,
            name,
            json.dumps(metrics),
            json.dumps(spec_details),
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
    specs = defaultdict(list)

    # keep lookup of specs
    with db.read_transaction():
        for spec in db.query_local(installed=False, in_buildcache=True):
            specs[spec.name].append(spec)
    return index, specs


def get_specs_metadata(specs):
    """
    Given loaded specs, parse metadata and return dict lookup.
    """
    # For funsies store top level metrics
    updates = {}
    parameters = {}
    compilers = {}
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
            if "name" not in entry or "url" not in entry:
                sys.exit(f"Malformed entry {entry} missing url or name.")
            name = entry["name"]
            url = entry["url"]
            print(f"Parsing cache for {name}")

            # Create spack database and load specs
            print("Loading spack db")
            index, specs = load_spack_db(name, url)

            print("Getting hash stacks")
            hash_stacks = get_hash_stacks(repo, name)

            # Update metadata file
            meta[name] = {
                "version": index["database"]["version"],
                "count": len(index["database"]["installs"]),
            }
            del index

            # Get metadata for specs
            print("Getting specs metadata")
            updates = get_specs_metadata(specs)
            meta[name].update(updates)

            # Write jekyll files
            print("Writing jekyll files")
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
