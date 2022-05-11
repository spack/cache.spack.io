#!/usr/bin/env python3

# This script will generate package metadata files for
# each package in the latest version of spack
#
# Usage:
# python generate_cache.py


import json
import yaml
import tempfile
import subprocess
import shutil
import sys
import os
import requests
import yaml
import time
from datetime import datetime

import spack.database
import spack.repo
import spack.spec

here = os.getcwd()

CACHE = "https://cache.e4s.io/build_cache/index.json"
db_root = os.path.join(here, "spack-db")


def write_json(content, filename):
    with open(filename, "w") as outfile:
        outfile.write(json.dumps(content, indent=4))


# Template for cache data
template = """
---
title: {package}
layout: cache
category: package
spec: {spec}
---
"""


def main():

    response = requests.get(CACHE)
    if response.status_code != 200:
        sys.exit(f"Issue with request to get package index: %s" % response.reason)
    index = response.json()

    # Write index.json to file
    if not os.path.exists(db_root):
        os.makedirs(db_root)
    write_json(index, os.path.join(db_root, "index.json"))

    # yeah this is awkward <--- from @tgamblin :D
    db = spack.database.Database(None, db_root)

    # Get complete list of packages
    packages = set()
    for _, spec in index["database"]["installs"].items():
        packages.add(list(spec["spec"].keys())[0])
    del index

    # keep lookup of specs
    specs = {}
    start = time.time()
    for i, package in enumerate(packages):
        print(f"Deriving database specs for {package}")
        with db.read_transaction():
            specs[package] = db.query(package, installed=False, in_buildcache=True)
    end = time.time()
    import IPython

    IPython.embed()
    sys.exit()

    # We will save a metadata file
    count = 0
    meta = {
        "version": index["database"]["version"],
        "count": len(index["database"]["installs"]),
    }

    # Organize specs by package
    specs = {}

    # For funsies store top level metrics
    parameters = {}
    compilers = {}
    arches = {"platform": {}, "platform_os": {}, "compiler": {}, "target": {}}

    # For each package, generate a data page, including the spec.json
    for hash_, spec in index["database"]["installs"].items():
        package_name = list(spec["spec"].keys())[0]
        if package_name not in specs:
            specs[package_name] = []
        specs[package_name].append(spec)
        for paramname, setting in spec["spec"][package_name]["parameters"].items():

            # Is true or not empty list
            if setting:
                if paramname not in parameters:
                    parameters[paramname] = 0
                parameters[paramname] += 1

        for key, value in spec["spec"][package_name]["arch"].items():

            # Target can have another level of nesting
            if key == "target" and isinstance(value, dict):
                value = "%s %s" % (value["vendor"], value["name"])
            if value not in arches[key]:
                arches[key][value] = 0
            arches[key][value] += 1

        compiler = "%s@%s" % (
            spec["spec"][package_name]["compiler"]["name"],
            spec["spec"][package_name]["compiler"]["version"],
        )
        if compiler not in compilers:
            compilers[compiler] = 0
        compilers[compiler] += 1

    # For each meta, write to data file
    meta_file = os.path.join(here, "_data", "meta.yaml")
    meta["compilers"] = compilers
    meta["parameters"] = parameters
    meta["compiler_count"] = len(compilers)

    import IPython

    IPython.embed()


if __name__ == "__main__":
    main()
