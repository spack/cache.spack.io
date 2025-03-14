---
title: "automake"
layout: cache
categories: [package, v0.22.5]
meta: {"compilers": ["gcc@=10.2.1", "gcc@=11.1.0", "gcc@=11.4.0", "gcc@=12.3.0", "gcc@=7.3.1", "gcc@=7.5.0", "gcc@=9.4.0", "oneapi@=2024.0.0"], "num_specs": 15, "num_specs_by_stack": {"aws-isc": 1, "aws-isc-aarch64": 2, "aws-pcluster-neoverse_v1": 2, "build_systems": 1, "data-vis-sdk": 1, "developer-tools": 1, "developer-tools-manylinux2014": 1, "e4s": 1, "e4s-neoverse-v2": 1, "e4s-neoverse_v1": 1, "e4s-oneapi": 1, "e4s-power": 1, "e4s-rocm-external": 1, "ml-linux-x86_64-cpu": 1, "ml-linux-x86_64-cuda": 1, "radiuss": 2, "radiuss-aws": 1, "radiuss-aws-aarch64": 2, "root": 15, "tutorial": 2}, "oss": ["amzn2", "centos7", "ubuntu18.04", "ubuntu20.04", "ubuntu22.04"], "platforms": ["linux"], "stacks": ["aws-isc", "aws-isc-aarch64", "aws-pcluster-neoverse_v1", "build_systems", "data-vis-sdk", "developer-tools", "developer-tools-manylinux2014", "e4s", "e4s-neoverse-v2", "e4s-neoverse_v1", "e4s-oneapi", "e4s-power", "e4s-rocm-external", "ml-linux-x86_64-cpu", "ml-linux-x86_64-cuda", "radiuss", "radiuss-aws", "radiuss-aws-aarch64", "root", "tutorial"], "targets": ["aarch64", "neoverse_n1", "neoverse_v1", "neoverse_v2", "ppc64le", "x86_64_v3"], "versions": ["1.15.1", "1.16.5"]}
spec_details: [{"compiler": "gcc@=9.4.0", "hash": "3z3akomqjbjodjik3vk5xcpumfrc4eeo", "os": "ubuntu20.04", "platform": "linux", "size": "-", "stacks": ["e4s-power", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-ubuntu20.04-ppc64le/gcc-9.4.0/automake-1.16.5/linux-ubuntu20.04-ppc64le-gcc-9.4.0-automake-1.16.5-3z3akomqjbjodjik3vk5xcpumfrc4eeo.spack", "target": "ppc64le", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "gcc@=12.3.0", "hash": "5vz6ecvdxhryz6of6kzmh4stbtmnlii3", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["aws-pcluster-neoverse_v1", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-amzn2-neoverse_v1/gcc-12.3.0/automake-1.16.5/linux-amzn2-neoverse_v1-gcc-12.3.0-automake-1.16.5-5vz6ecvdxhryz6of6kzmh4stbtmnlii3.spack", "target": "neoverse_v1", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "gcc@=11.4.0", "hash": "6liamd64ojf4yihwzdw6zn3pe3mhfxrx", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "e4s-rocm-external", "ml-linux-x86_64-cpu", "ml-linux-x86_64-cuda", "root", "tutorial"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/automake-1.16.5/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-automake-1.16.5-6liamd64ojf4yihwzdw6zn3pe3mhfxrx.spack", "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "oneapi@=2024.0.0", "hash": "7q5clakgxm5xpgsitkiou7dq7yaqbrun", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-oneapi", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.0.0/automake-1.16.5/linux-ubuntu22.04-x86_64_v3-oneapi-2024.0.0-automake-1.16.5-7q5clakgxm5xpgsitkiou7dq7yaqbrun.spack", "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "gcc@=7.3.1", "hash": "fjcufy75oogtdpudlgofn726bpcdjkkz", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["aws-isc-aarch64", "radiuss-aws-aarch64", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-amzn2-aarch64/gcc-7.3.1/automake-1.16.5/linux-amzn2-aarch64-gcc-7.3.1-automake-1.16.5-fjcufy75oogtdpudlgofn726bpcdjkkz.spack", "target": "aarch64", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "gcc@=7.3.1", "hash": "hakhm3opsmsvmo4hyxf7wgsuwvdvpbo5", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["aws-isc", "radiuss-aws", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-amzn2-x86_64_v3/gcc-7.3.1/automake-1.16.5/linux-amzn2-x86_64_v3-gcc-7.3.1-automake-1.16.5-hakhm3opsmsvmo4hyxf7wgsuwvdvpbo5.spack", "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "gcc@=7.3.1", "hash": "i25syyehspodq7qg3jiwbhezcheo2iwf", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["aws-isc-aarch64", "radiuss-aws-aarch64", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-amzn2-neoverse_n1/gcc-7.3.1/automake-1.16.5/linux-amzn2-neoverse_n1-gcc-7.3.1-automake-1.16.5-i25syyehspodq7qg3jiwbhezcheo2iwf.spack", "target": "neoverse_n1", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "gcc@=10.2.1", "hash": "lxcpar7zjm3ojsfgejhsjz44mrixgl3k", "os": "centos7", "platform": "linux", "size": "-", "stacks": ["developer-tools-manylinux2014", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-centos7-x86_64_v3/gcc-10.2.1/automake-1.16.5/linux-centos7-x86_64_v3-gcc-10.2.1-automake-1.16.5-lxcpar7zjm3ojsfgejhsjz44mrixgl3k.spack", "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "gcc@=11.1.0", "hash": "nfc7ryjrdbtl6wds5mfhddjtkdbnktxe", "os": "ubuntu20.04", "platform": "linux", "size": "-", "stacks": ["data-vis-sdk", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-ubuntu20.04-x86_64_v3/gcc-11.1.0/automake-1.16.5/linux-ubuntu20.04-x86_64_v3-gcc-11.1.0-automake-1.16.5-nfc7ryjrdbtl6wds5mfhddjtkdbnktxe.spack", "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "gcc@=7.5.0", "hash": "omyf7janz6eerau7atc5y4ruuvojaiff", "os": "ubuntu18.04", "platform": "linux", "size": "-", "stacks": ["radiuss", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-ubuntu18.04-x86_64_v3/gcc-7.5.0/automake-1.15.1/linux-ubuntu18.04-x86_64_v3-gcc-7.5.0-automake-1.15.1-omyf7janz6eerau7atc5y4ruuvojaiff.spack", "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["1.15.1"]}, {"compiler": "gcc@=7.5.0", "hash": "qudcqjzd5vcqxx6e3zegt57tv63rsh2g", "os": "ubuntu18.04", "platform": "linux", "size": "-", "stacks": ["build_systems", "developer-tools", "radiuss", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-ubuntu18.04-x86_64_v3/gcc-7.5.0/automake-1.16.5/linux-ubuntu18.04-x86_64_v3-gcc-7.5.0-automake-1.16.5-qudcqjzd5vcqxx6e3zegt57tv63rsh2g.spack", "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "gcc@=11.4.0", "hash": "slzbpcprchfbg56b5qsyl3zrvs2k67cx", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse_v1", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/automake-1.16.5/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-automake-1.16.5-slzbpcprchfbg56b5qsyl3zrvs2k67cx.spack", "target": "neoverse_v1", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "gcc@=12.3.0", "hash": "vfqzozxqcvv32fimcm6qta3p4j2fu4xd", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["aws-pcluster-neoverse_v1", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-amzn2-neoverse_n1/gcc-12.3.0/automake-1.16.5/linux-amzn2-neoverse_n1-gcc-12.3.0-automake-1.16.5-vfqzozxqcvv32fimcm6qta3p4j2fu4xd.spack", "target": "neoverse_n1", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "gcc@=12.3.0", "hash": "wnghuqgizqk3q2ijti4q2a7neqzg7x66", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["root", "tutorial"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-12.3.0/automake-1.16.5/linux-ubuntu22.04-x86_64_v3-gcc-12.3.0-automake-1.16.5-wnghuqgizqk3q2ijti4q2a7neqzg7x66.spack", "target": "x86_64_v3", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}, {"compiler": "gcc@=11.4.0", "hash": "ysms5vx3hiz33bficxf6ss2pvqswgc5j", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse-v2", "root"], "tarball": "https://binaries.spack.io/v0.22.5/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/automake-1.16.5/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-automake-1.16.5-ysms5vx3hiz33bficxf6ss2pvqswgc5j.spack", "target": "neoverse_v2", "variants": ["build_system=autotools"], "versions": ["1.16.5"]}]
---