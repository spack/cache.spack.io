---
title: "bison"
layout: cache
category: package
meta: {"versions": ["3.4.2", "3.7.4", "3.7.6", "3.6.4"], "compilers": ["gcc@8.3.1", "gcc@9.3.0", "gcc@8.1.0", "gcc@7.5.0", "intel@19.1.3.304", "gcc@7.3.1", "gcc@8.4.1", "gcc@7.3.0", "gcc@10.3.0"]}
spec_files: 
 - "bison@3.6.4%gcc@9.3.0 arch=linux-ubuntu20.04-x86_64 ^libsigsegv@2.12%gcc@9.3.0 arch=linux-ubuntu20.04-x86_64 ^m4@1.4.18%gcc@9.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-ubuntu20.04-x86_64": spec-0.json
 - "bison@3.7.6%intel@19.1.3.304 arch=cray-cnl7-haswell ^libsigsegv@2.12%intel@19.1.3.304 arch=cray-cnl7-haswell ^m4@1.4.18%intel@19.1.3.304+sigsegv patches=3877ab5,fc9b616 arch=cray-cnl7-haswell": spec-1.json
 - "bison@3.7.4%gcc@9.3.0 arch=linux-ubuntu20.04-x86_64 ^libsigsegv@2.12%gcc@9.3.0 arch=linux-ubuntu20.04-x86_64 ^m4@1.4.18%gcc@9.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-ubuntu20.04-x86_64": spec-2.json
 - "bison@3.7.4%gcc@7.5.0 arch=linux-ubuntu18.04-ppc64le ^libsigsegv@2.12%gcc@7.5.0 arch=linux-ubuntu18.04-ppc64le ^m4@1.4.18%gcc@7.5.0+sigsegv patches=3877ab5,fc9b616 arch=linux-ubuntu18.04-ppc64le": spec-3.json
 - "bison@3.4.2%gcc@7.3.0 patches=89aa362 arch=linux-ubuntu18.04-x86_64 ^libsigsegv@2.12%gcc@7.3.0 arch=linux-ubuntu18.04-x86_64 ^m4@1.4.18%gcc@7.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-ubuntu18.04-x86_64": spec-4.json
 - "bison@3.4.2%gcc@7.3.0 patches=89aa362 arch=linux-rhel8-x86_64 ^libsigsegv@2.12%gcc@7.3.0 arch=linux-rhel8-x86_64 ^m4@1.4.18%gcc@7.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel8-x86_64": spec-5.json
 - "bison@3.7.4%gcc@8.1.0 arch=linux-rhel7-x86_64 ^libsigsegv@2.12%gcc@8.1.0 arch=linux-rhel7-x86_64 ^m4@1.4.18%gcc@8.1.0+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel7-x86_64": spec-6.json
 - "bison@3.7.6%gcc@8.3.1 arch=linux-rhel8-x86_64 ^libsigsegv@2.12%gcc@8.3.1 arch=linux-rhel8-x86_64 ^m4@1.4.18%gcc@8.3.1+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel8-x86_64": spec-7.json
 - "bison@3.7.4%gcc@8.1.0 arch=linux-rhel7-ppc64le ^libsigsegv@2.12%gcc@8.1.0 arch=linux-rhel7-ppc64le ^m4@1.4.18%gcc@8.1.0+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel7-ppc64le": spec-8.json
 - "bison@3.7.6%gcc@9.3.0 arch=linux-ubuntu20.04-x86_64 ^libsigsegv@2.13%gcc@9.3.0 arch=linux-ubuntu20.04-x86_64 ^m4@1.4.19%gcc@9.3.0+sigsegv arch=linux-ubuntu20.04-x86_64": spec-9.json
 - "bison@3.4.2%gcc@7.3.0 patches=89aa362 arch=linux-rhel7-ppc64le ^libsigsegv@2.12%gcc@7.3.0 arch=linux-rhel7-ppc64le ^m4@1.4.18%gcc@7.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel7-ppc64le": spec-10.json
 - "bison@3.7.6%gcc@9.3.0 arch=linux-ubuntu20.04-ppc64le ^libsigsegv@2.12%gcc@9.3.0 arch=linux-ubuntu20.04-ppc64le ^m4@1.4.18%gcc@9.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-ubuntu20.04-ppc64le": spec-11.json
 - "bison@3.7.6%gcc@10.3.0 arch=linux-ubuntu21.04-ppc64le ^libsigsegv@2.13%gcc@10.3.0 arch=linux-ubuntu21.04-ppc64le ^m4@1.4.19%gcc@10.3.0+sigsegv arch=linux-ubuntu21.04-ppc64le": spec-12.json
 - "bison@3.4.2%gcc@7.3.0 patches=89aa362 arch=linux-rhel7-x86_64 ^libsigsegv@2.12%gcc@7.3.0 arch=linux-rhel7-x86_64 ^m4@1.4.18%gcc@7.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel7-x86_64": spec-13.json
 - "bison@3.7.6%gcc@7.5.0 arch=linux-ubuntu18.04-x86_64 ^libsigsegv@2.13%gcc@7.5.0 arch=linux-ubuntu18.04-x86_64 ^m4@1.4.19%gcc@7.5.0+sigsegv arch=linux-ubuntu18.04-x86_64": spec-14.json
 - "bison@3.7.6%gcc@9.3.0 arch=linux-rhel7-ppc64le ^libsigsegv@2.13%gcc@9.3.0 arch=linux-rhel7-ppc64le ^m4@1.4.19%gcc@9.3.0+sigsegv arch=linux-rhel7-ppc64le": spec-15.json
 - "bison@3.7.6%gcc@8.3.1 arch=linux-rhel8-ppc64le ^libsigsegv@2.13%gcc@8.3.1 arch=linux-rhel8-ppc64le ^m4@1.4.19%gcc@8.3.1+sigsegv arch=linux-rhel8-ppc64le": spec-16.json
 - "bison@3.7.6%gcc@7.5.0 arch=linux-ubuntu18.04-ppc64le ^libsigsegv@2.12%gcc@7.5.0 arch=linux-ubuntu18.04-ppc64le ^m4@1.4.18%gcc@7.5.0+sigsegv patches=3877ab5,fc9b616 arch=linux-ubuntu18.04-ppc64le": spec-17.json
 - "bison@3.7.6%gcc@8.1.0 arch=linux-rhel7-ppc64le ^libsigsegv@2.12%gcc@8.1.0 arch=linux-rhel7-ppc64le ^m4@1.4.18%gcc@8.1.0+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel7-ppc64le": spec-18.json
 - "bison@3.7.6%gcc@8.4.1 arch=linux-rhel8-x86_64 ^libsigsegv@2.13%gcc@8.4.1 arch=linux-rhel8-x86_64 ^m4@1.4.19%gcc@8.4.1+sigsegv arch=linux-rhel8-x86_64": spec-19.json
 - "bison@3.6.4%gcc@8.3.1 arch=linux-rhel8-x86_64 ^libsigsegv@2.12%gcc@8.3.1 arch=linux-rhel8-x86_64 ^m4@1.4.18%gcc@8.3.1+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel8-x86_64": spec-20.json
 - "bison@3.7.4%gcc@8.3.1 arch=linux-rhel8-x86_64 ^libsigsegv@2.12%gcc@8.3.1 arch=linux-rhel8-x86_64 ^m4@1.4.18%gcc@8.3.1+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel8-x86_64": spec-21.json
 - "bison@3.7.6%gcc@8.3.1 arch=linux-rhel8-ppc64le ^libsigsegv@2.12%gcc@8.3.1 arch=linux-rhel8-ppc64le ^m4@1.4.18%gcc@8.3.1+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel8-ppc64le": spec-22.json
 - "bison@3.7.6%gcc@10.3.0 arch=linux-ubuntu21.04-x86_64 ^libsigsegv@2.13%gcc@10.3.0 arch=linux-ubuntu21.04-x86_64 ^m4@1.4.19%gcc@10.3.0+sigsegv arch=linux-ubuntu21.04-x86_64": spec-23.json
 - "bison@3.7.6%gcc@9.3.0 arch=cray-cnl7-haswell ^libsigsegv@2.12%gcc@9.3.0 arch=cray-cnl7-haswell ^m4@1.4.18%gcc@9.3.0+sigsegv patches=3877ab5,fc9b616 arch=cray-cnl7-haswell": spec-24.json
 - "bison@3.4.2%gcc@7.3.0 patches=89aa362 arch=linux-centos8-x86_64 ^libsigsegv@2.12%gcc@7.3.0 arch=linux-centos8-x86_64 ^m4@1.4.18%gcc@7.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-centos8-x86_64": spec-25.json
 - "bison@3.7.6%gcc@7.5.0 arch=linux-ubuntu18.04-ppc64le ^libsigsegv@2.13%gcc@7.5.0 arch=linux-ubuntu18.04-ppc64le ^m4@1.4.19%gcc@7.5.0+sigsegv arch=linux-ubuntu18.04-ppc64le": spec-26.json
 - "bison@3.7.6%gcc@8.4.1 arch=linux-rhel8-ppc64le ^libsigsegv@2.13%gcc@8.4.1 arch=linux-rhel8-ppc64le ^m4@1.4.19%gcc@8.4.1+sigsegv arch=linux-rhel8-ppc64le": spec-27.json
 - "bison@3.4.2%gcc@7.3.0 patches=89aa362 arch=linux-centos7-x86_64 ^libsigsegv@2.12%gcc@7.3.0 arch=linux-centos7-x86_64 ^m4@1.4.18%gcc@7.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-centos7-x86_64": spec-28.json
 - "bison@3.7.6%gcc@8.1.0 arch=linux-rhel7-x86_64 ^libsigsegv@2.12%gcc@8.1.0 arch=linux-rhel7-x86_64 ^m4@1.4.18%gcc@8.1.0+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel7-x86_64": spec-29.json
 - "bison@3.4.2%gcc@7.3.0 patches=89aa362 arch=linux-centos7-ppc64le ^libsigsegv@2.12%gcc@7.3.0 arch=linux-centos7-ppc64le ^m4@1.4.18%gcc@7.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-centos7-ppc64le": spec-30.json
 - "bison@3.7.6%gcc@9.3.0 arch=linux-ubuntu20.04-x86_64 ^libsigsegv@2.12%gcc@9.3.0 arch=linux-ubuntu20.04-x86_64 ^m4@1.4.19%gcc@9.3.0+sigsegv arch=linux-ubuntu20.04-x86_64": spec-31.json
 - "bison@3.6.4%gcc@8.1.0 arch=linux-rhel7-x86_64 ^libsigsegv@2.12%gcc@8.1.0 arch=linux-rhel7-x86_64 ^m4@1.4.18%gcc@8.1.0+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel7-x86_64": spec-32.json
 - "bison@3.7.6%gcc@9.3.0 arch=linux-ubuntu20.04-ppc64le ^libsigsegv@2.13%gcc@9.3.0 arch=linux-ubuntu20.04-ppc64le ^m4@1.4.19%gcc@9.3.0+sigsegv arch=linux-ubuntu20.04-ppc64le": spec-33.json
 - "bison@3.7.4%gcc@7.5.0 arch=linux-ubuntu18.04-x86_64 ^libsigsegv@2.12%gcc@7.5.0 arch=linux-ubuntu18.04-x86_64 ^m4@1.4.18%gcc@7.5.0+sigsegv patches=3877ab5,fc9b616 arch=linux-ubuntu18.04-x86_64": spec-34.json
 - "bison@3.6.4%gcc@7.5.0 arch=linux-ubuntu18.04-x86_64 ^libsigsegv@2.12%gcc@7.5.0 arch=linux-ubuntu18.04-x86_64 ^m4@1.4.18%gcc@7.5.0+sigsegv patches=3877ab5,fc9b616 arch=linux-ubuntu18.04-x86_64": spec-35.json
 - "bison@3.4.2%gcc@7.3.0 patches=89aa362 arch=linux-ubuntu18.04-ppc64le ^libsigsegv@2.12%gcc@7.3.0 arch=linux-ubuntu18.04-ppc64le ^m4@1.4.18%gcc@7.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-ubuntu18.04-ppc64le": spec-36.json
 - "bison@3.7.6%gcc@9.3.0 arch=linux-rhel7-x86_64 ^libsigsegv@2.12%gcc@9.3.0 arch=linux-rhel7-x86_64 ^m4@1.4.18%gcc@9.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel7-x86_64": spec-37.json
 - "bison@3.7.4%gcc@7.3.1 arch=linux-amzn2-x86_64 ^libsigsegv@2.12%gcc@7.3.1 arch=linux-amzn2-x86_64 ^m4@1.4.18%gcc@7.3.1+sigsegv patches=3877ab5,fc9b616 arch=linux-amzn2-x86_64": spec-38.json
 - "bison@3.7.4%gcc@9.3.0 arch=linux-ubuntu20.04-ppc64le ^libsigsegv@2.12%gcc@9.3.0 arch=linux-ubuntu20.04-ppc64le ^m4@1.4.18%gcc@9.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-ubuntu20.04-ppc64le": spec-39.json
 - "bison@3.7.6%gcc@9.3.0 arch=linux-rhel7-x86_64 ^libsigsegv@2.13%gcc@9.3.0 arch=linux-rhel7-x86_64 ^m4@1.4.19%gcc@9.3.0+sigsegv arch=linux-rhel7-x86_64": spec-40.json
 - "bison@3.7.4%gcc@8.3.1 arch=linux-rhel8-ppc64le ^libsigsegv@2.12%gcc@8.3.1 arch=linux-rhel8-ppc64le ^m4@1.4.18%gcc@8.3.1+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel8-ppc64le": spec-41.json
 - "bison@3.7.6%gcc@9.3.0 arch=linux-rhel7-ppc64le ^libsigsegv@2.12%gcc@9.3.0 arch=linux-rhel7-ppc64le ^m4@1.4.18%gcc@9.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-rhel7-ppc64le": spec-42.json
 - "bison@3.7.6%gcc@9.3.0 arch=linux-ubuntu20.04-x86_64 ^libsigsegv@2.12%gcc@9.3.0 arch=linux-ubuntu20.04-x86_64 ^m4@1.4.18%gcc@9.3.0+sigsegv patches=3877ab5,fc9b616 arch=linux-ubuntu20.04-x86_64": spec-43.json
 - "bison@3.7.6%gcc@7.5.0 arch=linux-ubuntu18.04-x86_64 ^libsigsegv@2.12%gcc@7.5.0 arch=linux-ubuntu18.04-x86_64 ^m4@1.4.18%gcc@7.5.0+sigsegv patches=3877ab5,fc9b616 arch=linux-ubuntu18.04-x86_64": spec-44.json
 - "bison@3.7.6%gcc@8.3.1 arch=linux-rhel8-x86_64 ^libsigsegv@2.13%gcc@8.3.1 arch=linux-rhel8-x86_64 ^m4@1.4.19%gcc@8.3.1+sigsegv arch=linux-rhel8-x86_64": spec-45.json

---