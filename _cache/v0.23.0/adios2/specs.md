---
title: "adios2"
layout: cache
categories: [package, v0.23.0]
meta: {"versions": ["2.10.2", "2.7.1", "2.8.3"], "compilers": ["cce@=15.0.1", "gcc@=11.1.0", "gcc@=11.4.0", "gcc@=12.4.0", "gcc@=7.3.1", "gcc@=9.4.0", "oneapi@=2024.2.1"], "oss": ["amzn2", "rhel8", "ubuntu20.04", "ubuntu22.04"], "platforms": ["linux"], "targets": ["aarch64", "neoverse_n1", "neoverse_v1", "neoverse_v2", "ppc64le", "x86_64_v3", "x86_64_v4", "zen4"], "stacks": ["aws-isc", "aws-isc-aarch64", "aws-pcluster-neoverse_v1", "aws-pcluster-x86_64_v4", "data-vis-sdk", "e4s", "e4s-cray-rhel", "e4s-neoverse-v2", "e4s-neoverse_v1", "e4s-oneapi", "e4s-power", "e4s-rocm-external", "root"], "num_specs": 47, "num_specs_by_stack": {"aws-isc-aarch64": 2, "root": 47, "aws-pcluster-neoverse_v1": 2, "aws-pcluster-x86_64_v4": 2, "aws-isc": 1, "e4s-cray-rhel": 1, "e4s-power": 5, "data-vis-sdk": 2, "e4s-neoverse_v1": 10, "e4s-neoverse-v2": 5, "e4s": 9, "e4s-rocm-external": 3, "e4s-oneapi": 5}}
spec_details: [{"hash": "ixmbce3f5q4ommhrxjjqwf45rkrlmeqd", "compiler": "gcc@=7.3.1", "versions": ["2.7.1"], "os": "amzn2", "platform": "linux", "target": "aarch64", "variants": ["+blosc", "build_system=cmake", "build_type=Release", "+bzip2", "~cuda", "~dataspaces", "~fortran", "generator=make", "~hdf5", "~ipo", "+mpi", "patches=8221073,88b2cd1,9e67deb", "~pic", "+png", "~python", "~rocm", "+ssc", "+sst", "+sz", "+zfp"], "stacks": ["aws-isc-aarch64", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-amzn2-aarch64/gcc-7.3.1/adios2-2.7.1/linux-amzn2-aarch64-gcc-7.3.1-adios2-2.7.1-ixmbce3f5q4ommhrxjjqwf45rkrlmeqd.spack"}, {"hash": "xkvim2y36iwk7gi2xny6g727ylbw2svf", "compiler": "gcc@=12.4.0", "versions": ["2.10.2"], "os": "amzn2", "platform": "linux", "target": "neoverse_n1", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "~fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["aws-pcluster-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-amzn2-neoverse_n1/gcc-12.4.0/adios2-2.10.2/linux-amzn2-neoverse_n1-gcc-12.4.0-adios2-2.10.2-xkvim2y36iwk7gi2xny6g727ylbw2svf.spack"}, {"hash": "rz72n5i6iiajl4fy5os4wjddtegwbkhe", "compiler": "gcc@=7.3.1", "versions": ["2.7.1"], "os": "amzn2", "platform": "linux", "target": "neoverse_n1", "variants": ["+blosc", "build_system=cmake", "build_type=Release", "+bzip2", "~cuda", "~dataspaces", "~fortran", "generator=make", "~hdf5", "~ipo", "+mpi", "patches=8221073,88b2cd1,9e67deb", "~pic", "+png", "~python", "~rocm", "+ssc", "+sst", "+sz", "+zfp"], "stacks": ["aws-isc-aarch64", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-amzn2-neoverse_n1/gcc-7.3.1/adios2-2.7.1/linux-amzn2-neoverse_n1-gcc-7.3.1-adios2-2.7.1-rz72n5i6iiajl4fy5os4wjddtegwbkhe.spack"}, {"hash": "bbuqg4x6nfgmg2umojbcgtmio4ihuyhx", "compiler": "gcc@=12.4.0", "versions": ["2.10.2"], "os": "amzn2", "platform": "linux", "target": "neoverse_v1", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "~fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["aws-pcluster-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-amzn2-neoverse_v1/gcc-12.4.0/adios2-2.10.2/linux-amzn2-neoverse_v1-gcc-12.4.0-adios2-2.10.2-bbuqg4x6nfgmg2umojbcgtmio4ihuyhx.spack"}, {"hash": "i2ghddrcsw4okgnuj5dbixhufopwxvse", "compiler": "gcc@=12.4.0", "versions": ["2.10.2"], "os": "amzn2", "platform": "linux", "target": "x86_64_v3", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "~fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "aws-pcluster-x86_64_v4"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-amzn2-x86_64_v3/gcc-12.4.0/adios2-2.10.2/linux-amzn2-x86_64_v3-gcc-12.4.0-adios2-2.10.2-i2ghddrcsw4okgnuj5dbixhufopwxvse.spack"}, {"hash": "7i7ont7tyftqarhhwkz3emcz24w6h75r", "compiler": "gcc@=7.3.1", "versions": ["2.7.1"], "os": "amzn2", "platform": "linux", "target": "x86_64_v3", "variants": ["+blosc", "build_system=cmake", "build_type=Release", "+bzip2", "~cuda", "~dataspaces", "~fortran", "generator=make", "~hdf5", "~ipo", "+mpi", "patches=8221073,88b2cd1,9e67deb", "~pic", "+png", "~python", "~rocm", "+ssc", "+sst", "+sz", "+zfp"], "stacks": ["aws-isc", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-amzn2-x86_64_v3/gcc-7.3.1/adios2-2.7.1/linux-amzn2-x86_64_v3-gcc-7.3.1-adios2-2.7.1-7i7ont7tyftqarhhwkz3emcz24w6h75r.spack"}, {"hash": "2gmopoxqnpr6o2y2jkc4wygzs2tuuwzq", "compiler": "gcc@=12.4.0", "versions": ["2.10.2"], "os": "amzn2", "platform": "linux", "target": "x86_64_v4", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "~fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "aws-pcluster-x86_64_v4"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-amzn2-x86_64_v4/gcc-12.4.0/adios2-2.10.2/linux-amzn2-x86_64_v4-gcc-12.4.0-adios2-2.10.2-2gmopoxqnpr6o2y2jkc4wygzs2tuuwzq.spack"}, {"hash": "uhuzfoftemwy4xmpudsigo3ffv32a2ro", "compiler": "cce@=15.0.1", "versions": ["2.10.2"], "os": "rhel8", "platform": "linux", "target": "zen4", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "~mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-cray-rhel", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-rhel8-zen4/cce-15.0.1/adios2-2.10.2/linux-rhel8-zen4-cce-15.0.1-adios2-2.10.2-uhuzfoftemwy4xmpudsigo3ffv32a2ro.spack"}, {"hash": "2554oq7hwfusurjkye7blx2s63rcynkn", "compiler": "gcc@=9.4.0", "versions": ["2.10.2"], "os": "ubuntu20.04", "platform": "linux", "target": "ppc64le", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "~fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-power", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu20.04-ppc64le/gcc-9.4.0/adios2-2.10.2/linux-ubuntu20.04-ppc64le-gcc-9.4.0-adios2-2.10.2-2554oq7hwfusurjkye7blx2s63rcynkn.spack"}, {"hash": "5ylcd3cy3qvbp4i5zgwd2shhyn5ikp5z", "compiler": "gcc@=9.4.0", "versions": ["2.10.2"], "os": "ubuntu20.04", "platform": "linux", "target": "ppc64le", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "+cuda", "cuda_arch=70", "+dataman", "~dataspaces", "+fortran", "generator=make", "+hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "+pic", "+png", "+python", "~rocm", "+shared", "+sst", "~sycl", "~sz", "+zfp"], "stacks": ["e4s-power", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu20.04-ppc64le/gcc-9.4.0/adios2-2.10.2/linux-ubuntu20.04-ppc64le-gcc-9.4.0-adios2-2.10.2-5ylcd3cy3qvbp4i5zgwd2shhyn5ikp5z.spack"}, {"hash": "7pquopgirtcic6z65oyt7wkgbktd7zqj", "compiler": "gcc@=9.4.0", "versions": ["2.10.2"], "os": "ubuntu20.04", "platform": "linux", "target": "ppc64le", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "+cuda", "cuda_arch=70", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-power", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu20.04-ppc64le/gcc-9.4.0/adios2-2.10.2/linux-ubuntu20.04-ppc64le-gcc-9.4.0-adios2-2.10.2-7pquopgirtcic6z65oyt7wkgbktd7zqj.spack"}, {"hash": "yehnchsouazxb7blkpj77uvr4bh7cknx", "compiler": "gcc@=9.4.0", "versions": ["2.10.2"], "os": "ubuntu20.04", "platform": "linux", "target": "ppc64le", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-power", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu20.04-ppc64le/gcc-9.4.0/adios2-2.10.2/linux-ubuntu20.04-ppc64le-gcc-9.4.0-adios2-2.10.2-yehnchsouazxb7blkpj77uvr4bh7cknx.spack"}, {"hash": "yx33dhzhi235ju2adoxf62zzlepn3hgo", "compiler": "gcc@=9.4.0", "versions": ["2.10.2"], "os": "ubuntu20.04", "platform": "linux", "target": "ppc64le", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-power", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu20.04-ppc64le/gcc-9.4.0/adios2-2.10.2/linux-ubuntu20.04-ppc64le-gcc-9.4.0-adios2-2.10.2-yx33dhzhi235ju2adoxf62zzlepn3hgo.spack"}, {"hash": "whxgdw7pd755rzao6g27mxo2tnljbka5", "compiler": "gcc@=11.1.0", "versions": ["2.10.2"], "os": "ubuntu20.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "+dataman", "~dataspaces", "+fortran", "generator=make", "+hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "+pic", "+png", "+python", "~rocm", "+shared", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["data-vis-sdk", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu20.04-x86_64_v3/gcc-11.1.0/adios2-2.10.2/linux-ubuntu20.04-x86_64_v3-gcc-11.1.0-adios2-2.10.2-whxgdw7pd755rzao6g27mxo2tnljbka5.spack"}, {"hash": "bkfwmv4hxmgrrjgdsfe37g5dynqk2g55", "compiler": "gcc@=11.1.0", "versions": ["2.7.1"], "os": "ubuntu20.04", "platform": "linux", "target": "x86_64_v3", "variants": ["+blosc", "build_system=cmake", "build_type=Release", "+bzip2", "~cuda", "+dataman", "~dataspaces", "+fortran", "generator=make", "+hdf5", "~ipo", "+mpi", "patches=8221073,88b2cd1,9e67deb", "+pic", "+png", "+python", "~rocm", "+shared", "+ssc", "+sst", "+sz", "+zfp"], "stacks": ["data-vis-sdk", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu20.04-x86_64_v3/gcc-11.1.0/adios2-2.7.1/linux-ubuntu20.04-x86_64_v3-gcc-11.1.0-adios2-2.7.1-bkfwmv4hxmgrrjgdsfe37g5dynqk2g55.spack"}, {"hash": "3nbr6e3xjkmcbff7mzdpwcqnnykktbjh", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v1", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "+cuda", "cuda_arch=75", "+dataman", "~dataspaces", "+fortran", "generator=make", "+hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "+pic", "+png", "+python", "~rocm", "+shared", "+sst", "~sycl", "~sz", "+zfp"], "stacks": ["e4s-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-adios2-2.10.2-3nbr6e3xjkmcbff7mzdpwcqnnykktbjh.spack"}, {"hash": "5fmspftaesbospw2db4wi4bfl7snjuel", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v1", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "+dataman", "~dataspaces", "+fortran", "generator=make", "+hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "+pic", "+png", "+python", "~rocm", "+shared", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-adios2-2.10.2-5fmspftaesbospw2db4wi4bfl7snjuel.spack"}, {"hash": "6yovx3lgmkwnochfghfi2rpkjfezluhz", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v1", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "+cuda", "cuda_arch=80", "+dataman", "~dataspaces", "+fortran", "generator=make", "+hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "+pic", "+png", "+python", "~rocm", "+shared", "+sst", "~sycl", "~sz", "+zfp"], "stacks": ["e4s-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-adios2-2.10.2-6yovx3lgmkwnochfghfi2rpkjfezluhz.spack"}, {"hash": "bspas5462kylv6n54wdzsli5c37bvmob", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v1", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "+cuda", "cuda_arch=90", "+dataman", "~dataspaces", "+fortran", "generator=make", "+hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "+pic", "+png", "+python", "~rocm", "+shared", "+sst", "~sycl", "~sz", "+zfp"], "stacks": ["e4s-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-adios2-2.10.2-bspas5462kylv6n54wdzsli5c37bvmob.spack"}, {"hash": "eux4c3pq2t4uddnsfdlbkaytrk7rimbe", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v1", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-adios2-2.10.2-eux4c3pq2t4uddnsfdlbkaytrk7rimbe.spack"}, {"hash": "fdq6xd5jh3evz4bimoy635oanad5shab", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v1", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "+cuda", "cuda_arch=80", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-adios2-2.10.2-fdq6xd5jh3evz4bimoy635oanad5shab.spack"}, {"hash": "fnmg6ia6mjkfigaxcunvm5wymmlrxnbs", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v1", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-adios2-2.10.2-fnmg6ia6mjkfigaxcunvm5wymmlrxnbs.spack"}, {"hash": "obyjmm6drfj7e4o5hmbwctwobu57fv6d", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v1", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "+cuda", "cuda_arch=75", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-adios2-2.10.2-obyjmm6drfj7e4o5hmbwctwobu57fv6d.spack"}, {"hash": "uvjwo7necvymveccbvsjig6hvsqetbp6", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v1", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "+cuda", "cuda_arch=90", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-adios2-2.10.2-uvjwo7necvymveccbvsjig6hvsqetbp6.spack"}, {"hash": "w4n5lv5masujtfkgupzqm6cyp37ph354", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v1", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "~fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-adios2-2.10.2-w4n5lv5masujtfkgupzqm6cyp37ph354.spack"}, {"hash": "6pvz5zliiddqvhtdr5m2weyaaq7q5gof", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v2", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "+dataman", "~dataspaces", "+fortran", "generator=make", "+hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "+pic", "+png", "+python", "~rocm", "+shared", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "e4s-neoverse-v2"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-adios2-2.10.2-6pvz5zliiddqvhtdr5m2weyaaq7q5gof.spack"}, {"hash": "milphpcpbu2xjujn7u4qeci6sivhzpnr", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v2", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "~fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "e4s-neoverse-v2"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-adios2-2.10.2-milphpcpbu2xjujn7u4qeci6sivhzpnr.spack"}, {"hash": "qdwzcil7svzs4jlnqlt7kz6azjsxtfju", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v2", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "e4s-neoverse-v2"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-adios2-2.10.2-qdwzcil7svzs4jlnqlt7kz6azjsxtfju.spack"}, {"hash": "tbxztiadn42jmvrtpd5imzm25glyvzgp", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v2", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "+cuda", "cuda_arch=90", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "e4s-neoverse-v2"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-adios2-2.10.2-tbxztiadn42jmvrtpd5imzm25glyvzgp.spack"}, {"hash": "wa32kryn2z24uk5uhyxtmnm6gkteodrw", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v2", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "e4s-neoverse-v2"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-adios2-2.10.2-wa32kryn2z24uk5uhyxtmnm6gkteodrw.spack"}, {"hash": "3okrsk7knbbwtwj7kfpq3jwma7ogydtq", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "+cuda", "cuda_arch=80", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-adios2-2.10.2-3okrsk7knbbwtwj7kfpq3jwma7ogydtq.spack"}, {"hash": "7ospvo3z6vwtxokcvzkxmctlbvj6fhqp", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-adios2-2.10.2-7ospvo3z6vwtxokcvzkxmctlbvj6fhqp.spack"}, {"hash": "a3rtrwngehpxsfn6cvbdzvsgmbzfzcx2", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-adios2-2.10.2-a3rtrwngehpxsfn6cvbdzvsgmbzfzcx2.spack"}, {"hash": "a5tv6aejz5ljslhwar3u536bl7asqbvy", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["amdgpu_target=gfx908", "~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "+kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "+rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-rocm-external", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-adios2-2.10.2-a5tv6aejz5ljslhwar3u536bl7asqbvy.spack"}, {"hash": "ag5rnra6kbqukqk73alqq7z5ae73pl4d", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["amdgpu_target=gfx90a", "~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "+kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "+rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-rocm-external", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-adios2-2.10.2-ag5rnra6kbqukqk73alqq7z5ae73pl4d.spack"}, {"hash": "ktbnnek245gia7jzcgpgn4b2wrildtox", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "~fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-adios2-2.10.2-ktbnnek245gia7jzcgpgn4b2wrildtox.spack"}, {"hash": "kzrthqcp6b2j7uflsaa6zqaxrgpov6aa", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-adios2-2.10.2-kzrthqcp6b2j7uflsaa6zqaxrgpov6aa.spack"}, {"hash": "l4f3vzaj7rjotjqv4usrkkjlrczfniv7", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-rocm-external", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-adios2-2.10.2-l4f3vzaj7rjotjqv4usrkkjlrczfniv7.spack"}, {"hash": "xevywpsasf3cp6tartrhh2ndjsxbez6v", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "+cuda", "cuda_arch=90", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-adios2-2.10.2-xevywpsasf3cp6tartrhh2ndjsxbez6v.spack"}, {"hash": "zgqoxbs2ruuym2yooid5q7ceha3ere7h", "compiler": "gcc@=11.4.0", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~aws", "+blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "+cuda", "cuda_arch=80", "+dataman", "~dataspaces", "+fortran", "generator=make", "+hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "+pic", "+png", "+python", "~rocm", "+shared", "+sst", "~sycl", "~sz", "+zfp"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/adios2-2.10.2/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-adios2-2.10.2-zgqoxbs2ruuym2yooid5q7ceha3ere7h.spack"}, {"hash": "iuj2d4edl6dhgohvdpnuksh5doxhwils", "compiler": "gcc@=11.4.0", "versions": ["2.7.1"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["+blosc", "build_system=cmake", "build_type=Release", "+bzip2", "~cuda", "~dataspaces", "+fortran", "generator=make", "+hdf5", "~ipo", "+mpi", "patches=8221073,88b2cd1,9e67deb", "~pic", "+png", "+python", "~rocm", "+ssc", "+sst", "+sz", "+zfp"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/adios2-2.7.1/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-adios2-2.7.1-iuj2d4edl6dhgohvdpnuksh5doxhwils.spack"}, {"hash": "jef3tiqh5krdsk52gvmj77yc65lftd7w", "compiler": "gcc@=11.4.0", "versions": ["2.7.1"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["+blosc", "build_system=cmake", "build_type=Release", "+bzip2", "~cuda", "+dataman", "~dataspaces", "+fortran", "generator=make", "+hdf5", "~ipo", "+mpi", "patches=8221073,88b2cd1,9e67deb", "+pic", "+png", "+python", "~rocm", "+shared", "+ssc", "+sst", "+sz", "+zfp"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/adios2-2.7.1/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-adios2-2.7.1-jef3tiqh5krdsk52gvmj77yc65lftd7w.spack"}, {"hash": "tgtyovbu73ag35ibdcyw6bvonjex4q3s", "compiler": "oneapi@=2024.2.1", "versions": ["2.10.2"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~aws", "~blosc2", "build_system=cmake", "build_type=Release", "+bzip2", "~campaign", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~kokkos", "+libcatalyst", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "~sycl", "+sz", "+zfp"], "stacks": ["e4s-oneapi", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.2.1/adios2-2.10.2/linux-ubuntu22.04-x86_64_v3-oneapi-2024.2.1-adios2-2.10.2-tgtyovbu73ag35ibdcyw6bvonjex4q3s.spack"}, {"hash": "2hvs6k4lsyb6yo2nr5awmgvhvvxvvclh", "compiler": "oneapi@=2024.2.1", "versions": ["2.8.3"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["+blosc", "build_system=cmake", "build_type=Release", "+bzip2", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "+sz", "+zfp"], "stacks": ["e4s-oneapi", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.2.1/adios2-2.8.3/linux-ubuntu22.04-x86_64_v3-oneapi-2024.2.1-adios2-2.8.3-2hvs6k4lsyb6yo2nr5awmgvhvvxvvclh.spack"}, {"hash": "gmilsj4x5vrk5ddpuj2wfvvbes25owti", "compiler": "oneapi@=2024.2.1", "versions": ["2.8.3"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["+blosc", "build_system=cmake", "build_type=Release", "+bzip2", "~cuda", "+dataman", "~dataspaces", "+fortran", "generator=make", "+hdf5", "~ipo", "~libpressio", "+mgard", "+mpi", "+pic", "+png", "+python", "~rocm", "+shared", "+sst", "+sz", "+zfp"], "stacks": ["e4s-oneapi", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.2.1/adios2-2.8.3/linux-ubuntu22.04-x86_64_v3-oneapi-2024.2.1-adios2-2.8.3-gmilsj4x5vrk5ddpuj2wfvvbes25owti.spack"}, {"hash": "vhjrhlupqjxbo2yjcvou5amkratlbclw", "compiler": "oneapi@=2024.2.1", "versions": ["2.8.3"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["+blosc", "build_system=cmake", "build_type=Release", "+bzip2", "~cuda", "~dataspaces", "~fortran", "generator=make", "~hdf5", "~ipo", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "+sz", "+zfp"], "stacks": ["e4s-oneapi", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.2.1/adios2-2.8.3/linux-ubuntu22.04-x86_64_v3-oneapi-2024.2.1-adios2-2.8.3-vhjrhlupqjxbo2yjcvou5amkratlbclw.spack"}, {"hash": "vzcyscveyu4vf43lvcjkdbinge5iscuj", "compiler": "oneapi@=2024.2.1", "versions": ["2.8.3"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["+blosc", "build_system=cmake", "build_type=Release", "+bzip2", "~cuda", "~dataspaces", "+fortran", "generator=make", "~hdf5", "~ipo", "~libpressio", "+mgard", "+mpi", "~pic", "+png", "~python", "~rocm", "+sst", "+sz", "+zfp"], "stacks": ["e4s-oneapi", "root"], "size": "-", "tarball": "https://binaries.spack.io/v0.23.0/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.2.1/adios2-2.8.3/linux-ubuntu22.04-x86_64_v3-oneapi-2024.2.1-adios2-2.8.3-vzcyscveyu4vf43lvcjkdbinge5iscuj.spack"}]
---