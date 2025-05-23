---
title: "eigen"
layout: cache
categories: [package, develop-2023-12-03]
meta: {"versions": ["3.4.0"], "compilers": ["apple-clang@=15.0.0", "cce@=15.0.1", "gcc@=11.1.0", "gcc@=11.3.0", "gcc@=11.4.0", "gcc@=7.3.1", "gcc@=9.4.0", "oneapi@=2023.2.0"], "oss": ["amzn2", "rhel8", "ubuntu20.04", "ubuntu22.04", "ventura"], "platforms": ["darwin", "linux"], "targets": ["aarch64", "neoverse_n1", "neoverse_v1", "ppc64le", "x86_64_v3", "zen4"], "stacks": ["aws-isc", "aws-isc-aarch64", "data-vis-sdk", "e4s", "e4s-cray-rhel", "e4s-neoverse_v1", "e4s-oneapi", "e4s-power", "e4s-rocm-external", "ml-darwin-aarch64-mps", "ml-linux-x86_64-cpu", "ml-linux-x86_64-cuda", "ml-linux-x86_64-rocm", "root"], "num_specs": 12, "num_specs_by_stack": {"ml-darwin-aarch64-mps": 1, "root": 12, "aws-isc-aarch64": 2, "aws-isc": 1, "e4s-cray-rhel": 1, "e4s-neoverse_v1": 1, "e4s-power": 1, "data-vis-sdk": 2, "e4s-rocm-external": 1, "e4s": 1, "e4s-oneapi": 1, "ml-linux-x86_64-cpu": 1, "ml-linux-x86_64-cuda": 1, "ml-linux-x86_64-rocm": 1}}
spec_details: [{"hash": "tbmuox73333kydyht4zip3l6pmuxhj3t", "compiler": "apple-clang@=15.0.0", "versions": ["3.4.0"], "os": "ventura", "platform": "darwin", "target": "aarch64", "variants": ["build_system=cmake", "build_type=RelWithDebInfo", "generator=make", "~ipo"], "stacks": ["ml-darwin-aarch64-mps", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2023-12-03/build_cache/darwin-ventura-aarch64/apple-clang-15.0.0/eigen-3.4.0/darwin-ventura-aarch64-apple-clang-15.0.0-eigen-3.4.0-tbmuox73333kydyht4zip3l6pmuxhj3t.spack"}, {"hash": "2ueyrdjkopumwxtbhb354uexa2dqxnmi", "compiler": "gcc@=7.3.1", "versions": ["3.4.0"], "os": "amzn2", "platform": "linux", "target": "aarch64", "variants": ["build_system=cmake", "build_type=RelWithDebInfo", "generator=make", "~ipo"], "stacks": ["aws-isc-aarch64", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2023-12-03/build_cache/linux-amzn2-aarch64/gcc-7.3.1/eigen-3.4.0/linux-amzn2-aarch64-gcc-7.3.1-eigen-3.4.0-2ueyrdjkopumwxtbhb354uexa2dqxnmi.spack"}, {"hash": "zt7nqseg4rswfyxzlv6u647jwzkkbog6", "compiler": "gcc@=7.3.1", "versions": ["3.4.0"], "os": "amzn2", "platform": "linux", "target": "neoverse_n1", "variants": ["build_system=cmake", "build_type=RelWithDebInfo", "generator=make", "~ipo"], "stacks": ["aws-isc-aarch64", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2023-12-03/build_cache/linux-amzn2-neoverse_n1/gcc-7.3.1/eigen-3.4.0/linux-amzn2-neoverse_n1-gcc-7.3.1-eigen-3.4.0-zt7nqseg4rswfyxzlv6u647jwzkkbog6.spack"}, {"hash": "6cnx73652tz3uk4pzeihy6uadfqqcypc", "compiler": "gcc@=7.3.1", "versions": ["3.4.0"], "os": "amzn2", "platform": "linux", "target": "x86_64_v3", "variants": ["build_system=cmake", "build_type=RelWithDebInfo", "generator=make", "~ipo"], "stacks": ["aws-isc", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2023-12-03/build_cache/linux-amzn2-x86_64_v3/gcc-7.3.1/eigen-3.4.0/linux-amzn2-x86_64_v3-gcc-7.3.1-eigen-3.4.0-6cnx73652tz3uk4pzeihy6uadfqqcypc.spack"}, {"hash": "itr5qphtzxzmwxclf5cjty5663gfkzes", "compiler": "cce@=15.0.1", "versions": ["3.4.0"], "os": "rhel8", "platform": "linux", "target": "zen4", "variants": ["build_system=cmake", "build_type=RelWithDebInfo", "generator=make", "~ipo"], "stacks": ["e4s-cray-rhel", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2023-12-03/build_cache/linux-rhel8-zen4/cce-15.0.1/eigen-3.4.0/linux-rhel8-zen4-cce-15.0.1-eigen-3.4.0-itr5qphtzxzmwxclf5cjty5663gfkzes.spack"}, {"hash": "otjilydqtihez54ivnmsnfknv26zul57", "compiler": "gcc@=11.4.0", "versions": ["3.4.0"], "os": "ubuntu20.04", "platform": "linux", "target": "neoverse_v1", "variants": ["build_system=cmake", "build_type=RelWithDebInfo", "generator=make", "~ipo"], "stacks": ["e4s-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2023-12-03/build_cache/linux-ubuntu20.04-neoverse_v1/gcc-11.4.0/eigen-3.4.0/linux-ubuntu20.04-neoverse_v1-gcc-11.4.0-eigen-3.4.0-otjilydqtihez54ivnmsnfknv26zul57.spack"}, {"hash": "oog2u36o5mslt2qvjatiu6kc2hrdifnt", "compiler": "gcc@=9.4.0", "versions": ["3.4.0"], "os": "ubuntu20.04", "platform": "linux", "target": "ppc64le", "variants": ["build_system=cmake", "build_type=RelWithDebInfo", "generator=make", "~ipo"], "stacks": ["e4s-power", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2023-12-03/build_cache/linux-ubuntu20.04-ppc64le/gcc-9.4.0/eigen-3.4.0/linux-ubuntu20.04-ppc64le-gcc-9.4.0-eigen-3.4.0-oog2u36o5mslt2qvjatiu6kc2hrdifnt.spack"}, {"hash": "untzrtimbidxx7kbucikqkeift5m7s3m", "compiler": "gcc@=11.1.0", "versions": ["3.4.0"], "os": "ubuntu20.04", "platform": "linux", "target": "x86_64_v3", "variants": ["build_system=cmake", "build_type=RelWithDebInfo", "generator=make", "~ipo"], "stacks": ["data-vis-sdk", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2023-12-03/build_cache/linux-ubuntu20.04-x86_64_v3/gcc-11.1.0/eigen-3.4.0/linux-ubuntu20.04-x86_64_v3-gcc-11.1.0-eigen-3.4.0-untzrtimbidxx7kbucikqkeift5m7s3m.spack"}, {"hash": "fkq44hobpybbrf7dqnih34s3cupbr3d5", "compiler": "gcc@=11.1.0", "versions": ["3.4.0"], "os": "ubuntu20.04", "platform": "linux", "target": "x86_64_v3", "variants": ["build_system=cmake", "build_type=RelWithDebInfo", "generator=make", "~ipo"], "stacks": ["data-vis-sdk", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2023-12-03/build_cache/linux-ubuntu20.04-x86_64_v3/gcc-11.1.0/eigen-3.4.0/linux-ubuntu20.04-x86_64_v3-gcc-11.1.0-eigen-3.4.0-fkq44hobpybbrf7dqnih34s3cupbr3d5.spack"}, {"hash": "me6j73rweltp7nacellttbo4lbzjjmeg", "compiler": "gcc@=11.4.0", "versions": ["3.4.0"], "os": "ubuntu20.04", "platform": "linux", "target": "x86_64_v3", "variants": ["build_system=cmake", "build_type=RelWithDebInfo", "generator=make", "~ipo"], "stacks": ["e4s-rocm-external", "root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/develop-2023-12-03/build_cache/linux-ubuntu20.04-x86_64_v3/gcc-11.4.0/eigen-3.4.0/linux-ubuntu20.04-x86_64_v3-gcc-11.4.0-eigen-3.4.0-me6j73rweltp7nacellttbo4lbzjjmeg.spack"}, {"hash": "acp57d6e4uyqkhejotfuhp5qjmns73a7", "compiler": "oneapi@=2023.2.0", "versions": ["3.4.0"], "os": "ubuntu20.04", "platform": "linux", "target": "x86_64_v3", "variants": ["build_system=cmake", "build_type=RelWithDebInfo", "generator=make", "~ipo"], "stacks": ["e4s-oneapi", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2023-12-03/build_cache/linux-ubuntu20.04-x86_64_v3/oneapi-2023.2.0/eigen-3.4.0/linux-ubuntu20.04-x86_64_v3-oneapi-2023.2.0-eigen-3.4.0-acp57d6e4uyqkhejotfuhp5qjmns73a7.spack"}, {"hash": "hm5zmwmkabkkfeaddnd6trr3buo7soz2", "compiler": "gcc@=11.3.0", "versions": ["3.4.0"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["build_system=cmake", "build_type=RelWithDebInfo", "generator=make", "~ipo"], "stacks": ["ml-linux-x86_64-cpu", "ml-linux-x86_64-cuda", "ml-linux-x86_64-rocm", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2023-12-03/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.3.0/eigen-3.4.0/linux-ubuntu22.04-x86_64_v3-gcc-11.3.0-eigen-3.4.0-hm5zmwmkabkkfeaddnd6trr3buo7soz2.spack"}]
---