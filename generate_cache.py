#!/usr/bin/env spack-python

# This script will generate package metadata files for
# each package in the latest version of spack
#
# Usage:
# python generate_cache.py

from dataclasses import dataclass
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Iterable, Literal
import json
import os
import requests
import re
import yaml

import spack.database
import spack.spec

from spack.database import _DB_DIRNAME

here = Path(os.getcwd())
db_root = here / "spack-db"

INDEX_URL = "https://binaries.spack.io/cache_spack_io_index.json"
MUTABLE_REFS = ["develop"]
INDEX_BUCKET_MATCHER = re.compile(r"^s3://([^\/]+)/(.+)$")
BUCKET_URLS = {
    "spack-binaries": "https://binaries.spack.io",
}

# Template for cache data
template = """---
title: "%s"
layout: cache
categories: [package, %s]
meta: %s
spec_details: %s
---"""

tag_page_template = """---
layout: table
permalink: /tag/%s/
tag: %s
---"""


def binary_size(spec: spack.spec.Spec) -> int | Literal["-"]:
    # TODO: blocked on this value being baked into the build cache index.json
    return "-"


@dataclass(frozen=True)
class Stack:
    label: str
    url: str


@lru_cache
def get_build_cache_index() -> dict[str, list[Stack]]:
    r = requests.get(INDEX_URL)
    r.raise_for_status()
    return {k: [Stack(**x) for x in v] for k, v in r.json().items()}


def get_hash_stacks(entry: str, stacks: Iterable[Stack]) -> dict[str, set[str]]:
    hash_stacks = defaultdict(set)

    for stack in stacks:
        r = requests.get(
            stack.url.replace("s3://spack-binaries/", "https://binaries.spack.io/")
        )
        if r.status_code == 404:
            print(f"No build cache for {entry} {stack} ({stack.url})")
            continue
        else:
            r.raise_for_status()

        for hash in r.json()["database"]["installs"].keys():
            hash_stacks[hash].add(stack.label)

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

        package_dir = here / "_cache" / name / package_name
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

            assert len(spec.versions) == 1, spec.versions
            spec_details.append(
                {
                    "hash": spec._hash,
                    "compiler": str(spec.compiler),
                    "versions": [str(v) for v in spec.versions],
                    "os": spec.architecture.os,
                    "platform": spec.architecture.platform,
                    "target": spec.architecture.target.name,
                    "variants": [str(v) for v in spec.variants.values()],
                    "stacks": sorted(list(hash_stacks[spec._hash])),
                    "size": binary_size(spec),
                }
            )
        metrics["oss"] = sorted(list(metrics["oss"]))
        metrics["platforms"] = sorted(list(metrics["platforms"]))
        metrics["targets"] = sorted(list(metrics["targets"]))
        metrics["versions"] = sorted(list(metrics["versions"]))
        metrics["compilers"] = sorted(list(metrics["compilers"]))
        metrics["stacks"] = sorted(list(metrics["stacks"]))
        spec_details = sorted(spec_details, key=lambda obj: obj["hash"])
        render = template % (
            package_name,
            name,
            json.dumps(metrics, sort_keys=True),
            json.dumps(spec_details, sort_keys=True),
        )
        md_file = os.path.join(package_dir, "specs.md")
        with open(md_file, "w") as fd:
            fd.write(render)


def specs_by_package(name: str, url: str) -> dict[str, list[spack.spec.Spec]]:
    """
    Given a named entry and a URL, load a spack database
    """
    response = requests.get(url)
    response.raise_for_status()
    index = response.json()

    # Write index.json to file
    entry_db = os.path.join(db_root, name, _DB_DIRNAME)
    if not os.path.exists(entry_db):
        os.makedirs(entry_db)

    with open(os.path.join(entry_db, "index.json"), "w") as outfile:
        outfile.write(json.dumps(index, indent=4))

    # yeah this is awkward <--- from @tgamblin :D
    db = spack.database.Database(os.path.join(db_root, name))

    # Organize specs by package
    specs: dict[str, list[spack.spec.Spec]] = defaultdict(list)

    # keep lookup of specs
    with db.read_transaction():
        db_specs = db.query_local(installed=False, in_buildcache=True)
        if db_specs:
            for spec in db_specs:
                assert isinstance(spec.name, str)  # appease type checker
                specs[spec.name].append(spec)

    return specs


def get_specs_metadata(specs: dict[str, list[spack.spec.Spec]]) -> dict:
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
        updates["count"] = count
    return updates


def load_existing_metadata() -> dict[str, dict]:
    meta_path = here / "_data" / "meta.yaml"
    try:
        with open(meta_path) as fd:
            return yaml.safe_load(fd.read())
    except Exception:
        print("No pre-existing metadata could be read")
        return {}


def load_existing_tags() -> list[dict]:
    tag_path = here / "_data" / "tags.yaml"
    try:
        with open(tag_path) as fd:
            return yaml.safe_load(fd.read())
    except Exception:
        print("No pre-existing tags could be read")
        return []


def s3_to_cloudfront(url):
    m = INDEX_BUCKET_MATCHER.match(url)
    if m:
        bucket = m.group(1)
        prefix = m.group(2)
        if bucket in BUCKET_URLS:
            return f"{BUCKET_URLS[bucket]}/{prefix}"
    return url


def main():
    # Metadata file will store all versions
    meta: dict[str, dict] = load_existing_metadata()
    tags = load_existing_tags()

    tags_dir = here / "pages" / "tags"
    tags_dir.mkdir(parents=True, exist_ok=True)

    for name, stacks in get_build_cache_index().items():
        for s in stacks:
            if s.label == "root":
                url = s3_to_cloudfront(s.url)
                break
        else:
            print(f"Skipping {name} because it doesn't have a root stack")
            continue

        cache_path = here / "_cache" / name
        if os.path.exists(cache_path) and name not in MUTABLE_REFS:
            print(f"Skip parsing cache for {name}. We already have it, and it is immutable.")
            continue

        print(f"Parsing cache for {name}")

        # Create spack database and load specs
        print("Loading spack db")
        specs = specs_by_package(name, url)

        print("Getting hash stacks")
        hash_stacks = get_hash_stacks(name, stacks)

        # Get metadata for specs
        print("Getting specs metadata")
        meta[name] = get_specs_metadata(specs)

        # Write jekyll files
        print("Writing jekyll files")
        write_cache_entries(name, specs, hash_stacks)

        tag_entry = {"name": name, "stacks": sorted([s.label for s in stacks])}

        for idx, tag_stacks in enumerate(tags):
            if tag_stacks["name"] == name:
                tags[idx] = tag_entry
                break
        else:
            tags.append(tag_entry)

        with open(f"pages/tags/{name}.md", "w") as f:
            f.write(tag_page_template % (name, name))

    with open("_data/tags.yaml", "w") as f:
        # sort tags such that develop is first, named tags are next,
        # and develop-* are last (but in reverse order)
        def tag_sorter(item):
            if item["name"] == "develop":
                return 0, 0
            elif match := re.match(r"^develop-(\d{4}-\d{2}-\d{2})$", item["name"]):
                return 2, -int(match.group(1).replace("-", ""))
            else:
                return 1, -int(item["name"].replace("v", "").replace(".", ""))

        tags = sorted(tags, key=tag_sorter)

        yaml.dump(tags, f)

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
    meta_file = here / "_data" / "meta.yaml"
    with open(meta_file, "w") as fd:
        fd.write(yaml.dump(meta))

    print("Done!\n\n")


if __name__ == "__main__":
    main()
