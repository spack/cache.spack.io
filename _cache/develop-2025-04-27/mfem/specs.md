---
title: "mfem"
layout: cache
categories: [package, develop-2025-04-27]
meta: {"compilers": ["cce@18.0.0", "gcc@11.1.0", "gcc@11.4.0", "gcc@7.3.1", "gcc@7.5.0", "intel-oneapi-compilers@2025.1.0"], "num_specs": 20, "num_specs_by_stack": {"data-vis-sdk": 1, "e4s": 7, "e4s-cray-rhel": 1, "e4s-neoverse-v2": 2, "e4s-oneapi": 1, "e4s-rocm-external": 2, "radiuss": 1, "radiuss-aws": 3, "radiuss-aws-aarch64": 2, "root": 20}, "oss": ["amzn2", "rhel8", "ubuntu18.04", "ubuntu20.04", "ubuntu22.04"], "platforms": ["linux"], "stacks": ["data-vis-sdk", "e4s", "e4s-cray-rhel", "e4s-neoverse-v2", "e4s-oneapi", "e4s-rocm-external", "radiuss", "radiuss-aws", "radiuss-aws-aarch64", "root"], "targets": ["aarch64", "neoverse_v2", "x86_64_v3"], "versions": ["4.7.0"]}
spec_details: [{"compiler": "gcc@11.4.0", "hash": "3hl2r6xviy5rp2fau2vghymnpmh6hfsl", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@11.4.0", "hash": "5qp3kjnqzqxms7bls5qdiggxauf24olj", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "~conduit", "+cuda", "cuda_arch:=90", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "cce@18.0.0", "hash": "5v6q2jgs5mg2cfyf6jdr6alaywbfoh3j", "os": "rhel8", "platform": "linux", "size": "-", "stacks": ["e4s-cray-rhel", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@7.3.1", "hash": "5vgunwzcdddro7tgf6fdznyfk24573co", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["radiuss-aws", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@11.4.0", "hash": "6rhgjfp6vxq2fvyjwenj3qa4vo3czm6j", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-rocm-external", "root"], "target": "x86_64_v3", "variants": ["amdgpu_target:=gfx908", "~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "+rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@11.1.0", "hash": "757ihvqlsoih2un56pu6w23g5gcr3uuh", "os": "ubuntu20.04", "platform": "linux", "size": "-", "stacks": ["data-vis-sdk", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "+conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "+exceptions", "+fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "+shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@11.4.0", "hash": "a45a6xfzeucwltalfxbiqeoiihuwh2nl", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "~conduit", "+cuda", "cuda_arch:=80", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@11.4.0", "hash": "duqvcohzu364zcscc5ixsxwi4yg2vv2u", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse-v2", "root"], "target": "neoverse_v2", "variants": ["~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@11.4.0", "hash": "dvhoshnefrb23ila2z3b2bzqmlg2cmki", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "+conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "+exceptions", "+fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "+shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@11.4.0", "hash": "gb5npvbnxr7qu7feb5ijtdhyl3ibv6b3", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "target": "x86_64_v3", "variants": ["amdgpu_target:=gfx90a", "~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "+rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@7.3.1", "hash": "ghp6j26tp6ggbahha3fmchlujqmq2mam", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["radiuss-aws", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "~conduit", "+cuda", "cuda_arch:=70", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@11.4.0", "hash": "j5dz3gwxitzrihdqzmmbyejnyfve3i6t", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-rocm-external", "root"], "target": "x86_64_v3", "variants": ["amdgpu_target:=gfx90a", "~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "+rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@7.3.1", "hash": "lxzz77rcp7h2xtfq7xmkuf3wf62b3sdo", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["radiuss-aws-aarch64", "root"], "target": "aarch64", "variants": ["~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=2576bfc,71ce9ee", "+petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "+sundials", "+superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@7.3.1", "hash": "mkqs5vz6mdy676l65fk3nwixafdtmt25", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["radiuss-aws-aarch64", "root"], "target": "aarch64", "variants": ["~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@11.4.0", "hash": "piss7vkwka5umcipztdnhsgnqnkeuzf4", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@7.5.0", "hash": "pl32fz7cytykclflasx7lpj5kcu5dtse", "os": "ubuntu18.04", "platform": "linux", "size": "-", "stacks": ["radiuss", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@11.4.0", "hash": "r73q3dd7yh2uvjbpfl6zyprtwb7prd77", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse-v2", "root"], "target": "neoverse_v2", "variants": ["~amgx", "build_system=generic", "~conduit", "+cuda", "cuda_arch:=90", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "intel-oneapi-compilers@2025.1.0", "hash": "ru3gfxde5bfi7iq3kuecf7hihufldray", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-oneapi", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@7.3.1", "hash": "zfhorliiv2cntl47ioi4pm6wo2nxt3v4", "os": "amzn2", "platform": "linux", "size": "-", "stacks": ["radiuss-aws", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "~conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "~exceptions", "~fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=2576bfc,71ce9ee", "+petsc", "precision=double", "~pumi", "~raja", "~rocm", "~shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "+sundials", "+superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}, {"compiler": "gcc@11.4.0", "hash": "ziw3gvvvziwzrwgjd4ywlzdog4gzw4ws", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "target": "x86_64_v3", "variants": ["~amgx", "build_system=generic", "+conduit", "~cuda", "cxxstd=auto", "~debug", "~examples", "+exceptions", "+fms", "~ginkgo", "~gnutls", "~gslib", "~hiop", "~lapack", "~libceed", "~libunwind", "+metis", "~miniapps", "~mpfr", "+mpi", "~mumps", "~netcdf", "~occa", "~openmp", "patches:=71ce9ee", "~petsc", "precision=double", "~pumi", "~raja", "~rocm", "+shared", "~slepc", "+static", "~strumpack", "~suite-sparse", "~sundials", "~superlu-dist", "~threadsafe", "timer=auto", "~umpire", "+zlib"], "versions": ["4.7.0"]}]
---