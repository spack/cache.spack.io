---
title: "tcsh"
layout: cache
category: package
meta: {"versions": ["6.22.02"], "compilers": ["gcc@8.3.1", "gcc@9.3.0", "gcc@8.1.0", "gcc@7.5.0", "intel@19.1.3.304", "gcc@7.3.1", "gcc@7.4.0"]}
spec_files: 
 - "tcsh@6.22.02%intel@19.1.3.304 patches=3926150,3a4e60f arch=cray-cnl7-haswell ^ncurses@6.2%intel@19.1.3.304~symlinks+termlib abi=none arch=cray-cnl7-haswell": spec-0.json
 - "tcsh@6.22.02%gcc@8.1.0 patches=3926150,3a4e60f arch=linux-rhel7-ppc64le ^ncurses@6.2%gcc@8.1.0~symlinks+termlib abi=none arch=linux-rhel7-ppc64le": spec-1.json
 - "tcsh@6.22.02%gcc@7.4.0 patches=3926150,3a4e60f arch=linux-rhel7-power9le ^ncurses@6.2%gcc@7.4.0~symlinks+termlib arch=linux-rhel7-power9le": spec-2.json
 - "tcsh@6.22.02%gcc@8.1.0 patches=3926150,3a4e60f arch=linux-rhel7-x86_64 ^ncurses@6.2%gcc@8.1.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64": spec-3.json
 - "tcsh@6.22.02%gcc@8.1.0 patches=3926150,3a4e60f arch=linux-rhel7-ppc64le ^ncurses@6.2%gcc@8.1.0~symlinks+termlib arch=linux-rhel7-ppc64le": spec-4.json
 - "tcsh@6.22.02%gcc@7.5.0 patches=3926150,3a4e60f arch=linux-ubuntu18.04-ppc64le ^ncurses@6.2%gcc@7.5.0~symlinks+termlib abi=none arch=linux-ubuntu18.04-ppc64le": spec-5.json
 - "tcsh@6.22.02%gcc@8.3.1 patches=3926150,3a4e60f arch=linux-rhel8-ppc64le ^ncurses@6.2%gcc@8.3.1~symlinks+termlib abi=none arch=linux-rhel8-ppc64le": spec-6.json
 - "tcsh@6.22.02%gcc@9.3.0 patches=3926150,3a4e60f arch=linux-ubuntu20.04-x86_64 ^ncurses@6.2%gcc@9.3.0~symlinks+termlib arch=linux-ubuntu20.04-x86_64": spec-7.json
 - "tcsh@6.22.02%gcc@7.5.0 patches=3926150,3a4e60f arch=linux-ubuntu18.04-x86_64 ^ncurses@6.2%gcc@7.5.0~symlinks+termlib arch=linux-ubuntu18.04-x86_64": spec-8.json
 - "tcsh@6.22.02%gcc@8.1.0 patches=3926150,3a4e60f arch=linux-rhel7-x86_64 ^ncurses@6.2%gcc@8.1.0~symlinks+termlib arch=linux-rhel7-x86_64": spec-9.json
 - "tcsh@6.22.02%gcc@9.3.0 patches=3926150,3a4e60f arch=linux-ubuntu20.04-x86_64 ^ncurses@6.2%gcc@9.3.0~symlinks+termlib abi=none arch=linux-ubuntu20.04-x86_64": spec-10.json
 - "tcsh@6.22.02%gcc@7.5.0 patches=3926150,3a4e60f arch=linux-ubuntu18.04-x86_64 ^ncurses@6.2%gcc@7.5.0~symlinks+termlib abi=none arch=linux-ubuntu18.04-x86_64": spec-11.json
 - "tcsh@6.22.02%gcc@9.3.0 patches=3926150,3a4e60f arch=linux-ubuntu20.04-ppc64le ^ncurses@6.2%gcc@9.3.0~symlinks+termlib abi=none arch=linux-ubuntu20.04-ppc64le": spec-12.json
 - "tcsh@6.22.02%gcc@8.3.1 patches=3926150,3a4e60f arch=linux-rhel8-ppc64le ^ncurses@6.2%gcc@8.3.1~symlinks+termlib arch=linux-rhel8-ppc64le": spec-13.json
 - "tcsh@6.22.02%gcc@8.3.1 patches=3926150,3a4e60f arch=linux-rhel8-x86_64 ^ncurses@6.2%gcc@8.3.1~symlinks+termlib abi=none arch=linux-rhel8-x86_64": spec-14.json
 - "tcsh@6.22.02%gcc@9.3.0 patches=3926150,3a4e60f arch=linux-rhel7-ppc64le ^ncurses@6.2%gcc@9.3.0~symlinks+termlib abi=none arch=linux-rhel7-ppc64le": spec-15.json
 - "tcsh@6.22.02%gcc@9.3.0 patches=3926150,3a4e60f arch=linux-rhel7-x86_64 ^ncurses@6.2%gcc@9.3.0~symlinks+termlib abi=none arch=linux-rhel7-x86_64": spec-16.json
 - "tcsh@6.22.02%gcc@7.5.0 patches=3926150,3a4e60f arch=linux-ubuntu18.04-ppc64le ^ncurses@6.2%gcc@7.5.0~symlinks+termlib arch=linux-ubuntu18.04-ppc64le": spec-17.json
 - "tcsh@6.22.02%gcc@9.3.0 patches=3926150,3a4e60f arch=linux-ubuntu20.04-ppc64le ^ncurses@6.2%gcc@9.3.0~symlinks+termlib arch=linux-ubuntu20.04-ppc64le": spec-18.json
 - "tcsh@6.22.02%gcc@7.3.1 patches=3926150,3a4e60f arch=linux-amzn2-x86_64 ^ncurses@6.2%gcc@7.3.1~symlinks+termlib arch=linux-amzn2-x86_64": spec-19.json
 - "tcsh@6.22.02%gcc@8.3.1 patches=3926150,3a4e60f arch=linux-rhel8-x86_64 ^ncurses@6.2%gcc@8.3.1~symlinks+termlib arch=linux-rhel8-x86_64": spec-20.json
 - "tcsh@6.22.02%gcc@9.3.0 patches=3926150,3a4e60f arch=cray-cnl7-haswell ^ncurses@6.2%gcc@9.3.0~symlinks+termlib abi=none arch=cray-cnl7-haswell": spec-21.json

---