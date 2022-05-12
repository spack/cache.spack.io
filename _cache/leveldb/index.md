---
title: "leveldb"
layout: cache
category: package
meta: {"versions": ["1.22"], "compilers": ["gcc@8.3.1", "gcc@9.3.0", "gcc@8.1.0", "gcc@7.5.0", "gcc@7.3.0", "gcc@7.4.0"]}
spec_files: 
 - "leveldb@1.22%gcc@8.3.1+shared build_type=RelWithDebInfo arch=linux-centos8-ppc64le ^snappy@1.1.8%gcc@8.3.1+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-centos8-ppc64le": spec-0.json
 - "leveldb@1.22%gcc@8.1.0+shared build_type=RelWithDebInfo arch=linux-centos7-x86_64 ^snappy@1.1.8%gcc@8.1.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-centos7-x86_64": spec-1.json
 - "leveldb@1.22%gcc@7.5.0+shared build_type=RelWithDebInfo arch=linux-ubuntu18.04-ppc64le ^snappy@1.1.8%gcc@7.5.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu18.04-ppc64le": spec-2.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-rhel7-ppc64le ^snappy@1.1.8%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel7-ppc64le": spec-3.json
 - "leveldb@1.22%gcc@8.3.1+shared build_type=RelWithDebInfo arch=linux-rhel8-x86_64 ^snappy@1.1.8%gcc@8.3.1+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel8-x86_64": spec-4.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-ubuntu18.04-ppc64le ^snappy@1.1.7%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu18.04-ppc64le": spec-5.json
 - "leveldb@1.22%gcc@8.1.0+shared build_type=RelWithDebInfo arch=linux-centos7-ppc64le ^snappy@1.1.8%gcc@8.1.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-centos7-ppc64le": spec-6.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-rhel8-x86_64 ^snappy@1.1.7%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel8-x86_64": spec-7.json
 - "leveldb@1.22%gcc@7.5.0~ipo+shared build_type=RelWithDebInfo arch=linux-ubuntu18.04-x86_64 ^snappy@1.1.8%gcc@7.5.0~ipo+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu18.04-x86_64": spec-8.json
 - "leveldb@1.22%gcc@7.5.0+shared build_type=RelWithDebInfo arch=linux-ubuntu18.04-x86_64 ^snappy@1.1.8%gcc@7.5.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu18.04-x86_64": spec-9.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-ubuntu18.04-x86_64 ^snappy@1.1.7%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu18.04-x86_64": spec-10.json
 - "leveldb@1.22%gcc@8.3.1~ipo+shared build_type=RelWithDebInfo arch=linux-rhel8-ppc64le ^snappy@1.1.8%gcc@8.3.1~ipo+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel8-ppc64le": spec-11.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-rhel7-x86_64 ^snappy@1.1.8%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel7-x86_64": spec-12.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-rhel7-ppc64le ^snappy@1.1.7%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel7-ppc64le": spec-13.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-centos8-x86_64 ^snappy@1.1.7%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-centos8-x86_64": spec-14.json
 - "leveldb@1.22%gcc@9.3.0+shared build_type=RelWithDebInfo arch=linux-ubuntu20.04-x86_64 ^snappy@1.1.7%gcc@9.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu20.04-x86_64": spec-15.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-rhel8-x86_64 ^snappy@1.1.8%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel8-x86_64": spec-16.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-centos8-x86_64 ^snappy@1.1.8%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-centos8-x86_64": spec-17.json
 - "leveldb@1.22%gcc@9.3.0+shared build_type=RelWithDebInfo arch=linux-ubuntu20.04-ppc64le ^snappy@1.1.8%gcc@9.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu20.04-ppc64le": spec-18.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-centos7-x86_64 ^snappy@1.1.7%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-centos7-x86_64": spec-19.json
 - "leveldb@1.22%gcc@8.3.1+shared build_type=RelWithDebInfo arch=linux-rhel8-aarch64 ^snappy@1.1.8%gcc@8.3.1+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel8-aarch64": spec-20.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-ubuntu18.04-ppc64le ^snappy@1.1.8%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu18.04-ppc64le": spec-21.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-ubuntu18.04-x86_64 ^snappy@1.1.8%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu18.04-x86_64": spec-22.json
 - "leveldb@1.22%gcc@9.3.0+shared build_type=RelWithDebInfo arch=linux-ubuntu20.04-x86_64 ^snappy@1.1.8%gcc@9.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu20.04-x86_64": spec-23.json
 - "leveldb@1.22%gcc@9.3.0+shared build_type=RelWithDebInfo arch=linux-ubuntu20.04-ppc64le ^snappy@1.1.7%gcc@9.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu20.04-ppc64le": spec-24.json
 - "leveldb@1.22%gcc@8.1.0+shared build_type=RelWithDebInfo arch=linux-rhel7-ppc64le ^snappy@1.1.8%gcc@8.1.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel7-ppc64le": spec-25.json
 - "leveldb@1.22%gcc@8.3.1+shared build_type=RelWithDebInfo arch=linux-centos8-ppc64le ^snappy@1.1.7%gcc@8.3.1+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-centos8-ppc64le": spec-26.json
 - "leveldb@1.22%gcc@8.1.0+shared build_type=RelWithDebInfo arch=linux-rhel7-ppc64le ^snappy@1.1.8%gcc@8.1.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel7-ppc64le": spec-27.json
 - "leveldb@1.22%gcc@8.3.1+shared build_type=RelWithDebInfo arch=linux-centos8-x86_64 ^snappy@1.1.8%gcc@8.3.1+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-centos8-x86_64": spec-28.json
 - "leveldb@1.22%gcc@8.1.0~ipo+shared build_type=RelWithDebInfo arch=linux-rhel7-ppc64le ^snappy@1.1.8%gcc@8.1.0~ipo+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel7-ppc64le": spec-29.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-rhel7-x86_64 ^snappy@1.1.7%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel7-x86_64": spec-30.json
 - "leveldb@1.22%gcc@8.1.0+shared build_type=RelWithDebInfo arch=linux-rhel7-x86_64 ^snappy@1.1.8%gcc@8.1.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel7-x86_64": spec-31.json
 - "leveldb@1.22%gcc@8.1.0~ipo+shared build_type=RelWithDebInfo arch=linux-rhel7-x86_64 ^snappy@1.1.8%gcc@8.1.0~ipo+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel7-x86_64": spec-32.json
 - "leveldb@1.22%gcc@9.3.0~ipo+shared build_type=RelWithDebInfo arch=linux-ubuntu20.04-ppc64le ^snappy@1.1.8%gcc@9.3.0~ipo+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu20.04-ppc64le": spec-33.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-centos7-x86_64 ^snappy@1.1.8%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-centos7-x86_64": spec-34.json
 - "leveldb@1.22%gcc@8.3.1+shared build_type=RelWithDebInfo arch=linux-rhel8-ppc64le ^snappy@1.1.8%gcc@8.3.1+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel8-ppc64le": spec-35.json
 - "leveldb@1.22%gcc@7.3.0+shared build_type=RelWithDebInfo arch=linux-centos7-ppc64le ^snappy@1.1.7%gcc@7.3.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-centos7-ppc64le": spec-36.json
 - "leveldb@1.22%gcc@7.5.0+shared build_type=RelWithDebInfo arch=linux-ubuntu18.04-aarch64 ^snappy@1.1.8%gcc@7.5.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu18.04-aarch64": spec-37.json
 - "leveldb@1.22%gcc@7.5.0+shared build_type=RelWithDebInfo arch=linux-ubuntu18.04-x86_64 ^snappy@1.1.8%gcc@7.5.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu18.04-x86_64": spec-38.json
 - "leveldb@1.22%gcc@7.5.0+shared build_type=RelWithDebInfo arch=linux-ubuntu18.04-ppc64le ^snappy@1.1.8%gcc@7.5.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu18.04-ppc64le": spec-39.json
 - "leveldb@1.22%gcc@7.5.0~ipo+shared build_type=RelWithDebInfo arch=linux-ubuntu18.04-ppc64le ^snappy@1.1.8%gcc@7.5.0~ipo+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu18.04-ppc64le": spec-40.json
 - "leveldb@1.22%gcc@9.3.0~ipo+shared build_type=RelWithDebInfo arch=linux-ubuntu20.04-x86_64 ^snappy@1.1.8%gcc@9.3.0~ipo+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu20.04-x86_64": spec-41.json
 - "leveldb@1.22%gcc@8.3.1~ipo+shared build_type=RelWithDebInfo arch=linux-rhel8-x86_64 ^snappy@1.1.8%gcc@8.3.1~ipo+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel8-x86_64": spec-42.json
 - "leveldb@1.22%gcc@7.4.0+shared build_type=RelWithDebInfo arch=linux-ubuntu18.04-x86_64 ^snappy@1.1.7%gcc@7.4.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-ubuntu18.04-x86_64": spec-43.json
 - "leveldb@1.22%gcc@8.1.0+shared build_type=RelWithDebInfo arch=linux-rhel7-x86_64 ^snappy@1.1.8%gcc@8.1.0+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel7-x86_64": spec-44.json
 - "leveldb@1.22%gcc@8.3.1+shared build_type=RelWithDebInfo arch=linux-rhel8-ppc64le ^snappy@1.1.7%gcc@8.3.1+pic+shared build_type=RelWithDebInfo patches=c9cfecb arch=linux-rhel8-ppc64le": spec-45.json

---