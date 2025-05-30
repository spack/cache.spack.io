---
title: "libyaml"
layout: cache
categories: [package, develop-2025-04-06]
meta: {"compilers": ["apple-clang@16.0.0", "gcc@10.5.0", "gcc@11.1.0", "gcc@11.4.0", "gcc@12.4.0", "gcc@13.2.0", "gcc@13.3.0", "gcc@7.5.0", "intel-oneapi-compilers@2024.1.0", "intel-oneapi-compilers@2025.1.0"], "num_specs": 14, "num_specs_by_stack": {"aws-pcluster-neoverse_v1": 1, "aws-pcluster-x86_64_v4": 2, "build_systems": 1, "data-vis-sdk": 1, "developer-tools-aarch64-linux-gnu": 1, "developer-tools-darwin": 1, "developer-tools-x86_64_v3-linux-gnu": 1, "e4s": 2, "e4s-neoverse-v2": 1, "e4s-oneapi": 1, "hep": 1, "ml-darwin-aarch64-mps": 1, "ml-linux-aarch64-cpu": 1, "ml-linux-aarch64-cuda": 1, "ml-linux-x86_64-cpu": 1, "ml-linux-x86_64-cuda": 1, "ml-linux-x86_64-rocm": 1, "radiuss": 1, "root": 14}, "oss": ["amzn2", "centos7", "rhel8", "sequoia", "ubuntu18.04", "ubuntu20.04", "ubuntu22.04", "ubuntu24.04"], "platforms": ["darwin", "linux"], "stacks": ["aws-pcluster-neoverse_v1", "aws-pcluster-x86_64_v4", "build_systems", "data-vis-sdk", "developer-tools-aarch64-linux-gnu", "developer-tools-darwin", "developer-tools-x86_64_v3-linux-gnu", "e4s", "e4s-neoverse-v2", "e4s-oneapi", "hep", "ml-darwin-aarch64-mps", "ml-linux-aarch64-cpu", "ml-linux-aarch64-cuda", "ml-linux-x86_64-cpu", "ml-linux-x86_64-cuda", "ml-linux-x86_64-rocm", "radiuss", "root"], "targets": ["aarch64", "neoverse_v1", "neoverse_v2", "x86_64_v3", "x86_64_v4"], "versions": ["0.1.7", "0.2.5"]}
spec_details: [{"compiler": "gcc@7.5.0", "hash": "4heuxube5ndr26fqow2g6w4rjnkfd2rj", "os": "ubuntu18.04", "platform": "linux", "size": "-", "stacks": ["build_systems", "radiuss", "root"], "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}, {"compiler": "gcc@12.4.0", "hash": "5ksphdrmrffiiya5v2fkilmvr3u24s4o", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["aws-pcluster-neoverse_v1", "root"], "target": "neoverse_v1", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}, {"compiler": "intel-oneapi-compilers@2024.1.0", "hash": "6c345hlf3joyzga5fyebnarnwphckfd6", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["aws-pcluster-x86_64_v4", "root"], "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}, {"compiler": "gcc@11.4.0", "hash": "b22riwnwphemtrtmo45coptezf2lzqiy", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "hep", "root"], "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}, {"compiler": "gcc@13.3.0", "hash": "erdxl66yw6vnd763uyxp5jv2pfho3uie", "os": "rhel8", "platform": "linux", "size": "-", "stacks": ["developer-tools-aarch64-linux-gnu", "root"], "target": "aarch64", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}, {"compiler": "gcc@10.5.0", "hash": "hj2oh5tsp5oesohvuctfnbzxja4fzuzu", "os": "centos7", "platform": "linux", "size": "-", "stacks": ["developer-tools-x86_64_v3-linux-gnu", "root"], "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}, {"compiler": "intel-oneapi-compilers@2025.1.0", "hash": "jo24axsu4e67kl6a2ewxruoiqiahyhuh", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-oneapi", "root"], "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}, {"compiler": "gcc@11.4.0", "hash": "kk6llyt63th6grm7kwfi7copxxhq4ewn", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["0.1.7"]}, {"compiler": "gcc@13.2.0", "hash": "l4lltchict5u57qtynfnfi7v3b6lqkyd", "os": "ubuntu24.04", "platform": "linux", "size": "-", "stacks": ["ml-linux-x86_64-cpu", "ml-linux-x86_64-cuda", "ml-linux-x86_64-rocm", "root"], "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}, {"compiler": "gcc@11.4.0", "hash": "lnhxmrtnv4462x6w34kcogybdn66o4tb", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse-v2", "root"], "target": "neoverse_v2", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}, {"compiler": "gcc@13.2.0", "hash": "lsi74h23pvjxeaju5rgpxmd7gltzx7fd", "os": "ubuntu24.04", "platform": "linux", "size": "-", "stacks": ["ml-linux-aarch64-cpu", "ml-linux-aarch64-cuda", "root"], "target": "aarch64", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}, {"compiler": "apple-clang@16.0.0", "hash": "prgnwheh7wclc6kscsuld4gvq3fay7ws", "os": "sequoia", "platform": "darwin", "size": "-", "stacks": ["developer-tools-darwin", "ml-darwin-aarch64-mps", "root"], "target": "aarch64", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}, {"compiler": "intel-oneapi-compilers@2024.1.0", "hash": "rvnkohhwojogu37a4hh36gf76hrvc5ls", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["aws-pcluster-x86_64_v4", "root"], "target": "x86_64_v4", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}, {"compiler": "gcc@11.1.0", "hash": "zcd6q5iyh4z7bfdogqg7z7bgxrjw5fhs", "os": "ubuntu20.04", "platform": "linux", "size": "-", "stacks": ["data-vis-sdk", "root"], "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["0.2.5"]}]
---