---
title: "tioga"
layout: cache
category: package
meta: {"versions": ["develop", "master"], "compilers": ["apple-clang@12.0.0", "gcc@7.4.0"]}
spec_files: 
 - spec-0.json
 - spec-1.json
 - spec-2.json
spec_names:
 - 'tioga@master%gcc@7.4.0~ipo+pic+shared build_type=Release arch=linux-rhel7-power9le ^hwloc@2.4.0%gcc@7.4.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-rhel7-power9le ^libiconv@1.16%gcc@7.4.0 arch=linux-rhel7-power9le ^libpciaccess@0.16%gcc@7.4.0 arch=linux-rhel7-power9le ^libxml2@2.9.8%gcc@7.4.0~python arch=linux-rhel7-power9le ^mpich@3.3.2%gcc@7.4.0~argobots+fortran+hwloc+hydra+libxml2+pci+romio~slurm~verbs~wrapperrpath device=ch3 netmod=tcp patches=eb982de pmi=pmi arch=linux-rhel7-power9le ^xz@5.2.5%gcc@7.4.0+pic arch=linux-rhel7-power9le ^zlib@1.2.11%gcc@7.4.0+optimize+pic+shared arch=linux-rhel7-power9le'
 - 'tioga@develop%apple-clang@12.0.0~cuda~ipo+nodegid+pic~shared~stats~timers build_type=Release cuda_arch=none cxxstd=11 arch=darwin-catalina-x86_64 ^hwloc@2.4.1%apple-clang@12.0.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml~pci+shared arch=darwin-catalina-x86_64 ^libedit@3.1-20210216%apple-clang@12.0.0 arch=darwin-catalina-x86_64 ^libevent@2.1.12%apple-clang@12.0.0+openssl arch=darwin-catalina-x86_64 ^libiconv@1.16%apple-clang@12.0.0 arch=darwin-catalina-x86_64 ^libxml2@2.9.10%apple-clang@12.0.0~python arch=darwin-catalina-x86_64 ^ncurses@6.2%apple-clang@12.0.0~symlinks+termlib abi=none arch=darwin-catalina-x86_64 ^openmpi@4.0.5%apple-clang@12.0.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker~pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=none patches=60ce20b schedulers=none arch=darwin-catalina-x86_64 ^openssh@8.5p1%apple-clang@12.0.0 arch=darwin-catalina-x86_64 ^openssl@1.1.1k%apple-clang@12.0.0~docs+systemcerts arch=darwin-catalina-x86_64 ^xz@5.2.5%apple-clang@12.0.0~pic libs=shared,static arch=darwin-catalina-x86_64 ^zlib@1.2.11%apple-clang@12.0.0+optimize+pic+shared arch=darwin-catalina-x86_64'
 - 'tioga@master%gcc@7.4.0~ipo+pic+shared build_type=Release arch=linux-rhel7-power9le ^spectrum-mpi@10.3.1.2%gcc@7.4.0 arch=linux-rhel7-power9le'
---