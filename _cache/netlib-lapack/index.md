---
title: "netlib-lapack"
layout: cache
category: package
meta: {"versions": ["3.8.0", "3.9.1"], "compilers": ["apple-clang@12.0.0", "gcc@8.4.0", "gcc@9.3.0", "gcc@7.3.1", "gcc@6.4.0", "gcc@7.3.0", "gcc@7.4.0"]}
spec_files: 
 - "netlib-lapack@3.9.1%apple-clang@12.0.0~external-blas~ipo+lapacke+shared~xblas build_type=Release arch=darwin-catalina-x86_64": spec-0.json
 - "netlib-lapack@3.8.0%gcc@7.4.0~external-blas~ipo+lapacke+shared~xblas build_type=Release patches=5c79286,ad3d41f arch=linux-rhel7-power9le": spec-1.json
 - "netlib-lapack@3.8.0%gcc@8.4.0~external-blas+lapacke+shared~xblas build_type=RelWithDebInfo patches=5c79286,ad3d41f arch=linux-rhel7-sandybridge": spec-2.json
 - "netlib-lapack@3.8.0%gcc@7.3.1~external-blas~ipo+lapacke+shared~xblas build_type=Release patches=5c79286,ad3d41f arch=linux-amzn2-x86_64": spec-3.json
 - "netlib-lapack@3.8.0%gcc@6.4.0~external-blas+lapacke+shared~xblas build_type=RelWithDebInfo patches=5c79286,ad3d41f arch=linux-rhel7-power9le": spec-4.json
 - "netlib-lapack@3.8.0%gcc@9.3.0~external-blas~ipo+lapacke+shared~xblas build_type=Release patches=5c79286,ad3d41f arch=linux-ubuntu20.04-x86_64": spec-5.json
 - "netlib-lapack@3.8.0%gcc@7.3.0~external-blas+lapacke+shared~xblas build_type=RelWithDebInfo patches=5c79286,ad3d41f arch=linux-rhel7-x86_64": spec-6.json

---