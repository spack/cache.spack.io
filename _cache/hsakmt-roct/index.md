---
title: "hsakmt-roct"
layout: cache
category: package
meta: {"versions": ["3.9.0", "4.1.0", "4.0.0", "4.2.0"], "compilers": ["gcc@8.3.1", "gcc@9.3.0", "gcc@8.1.0", "gcc@7.5.0", "gcc@8.4.1", "gcc@10.3.0"]}
spec_files: 
 - "hsakmt-roct@4.0.0%gcc@9.3.0~ipo build_type=Release arch=linux-ubuntu20.04-x86_64 ^numactl@2.0.14%gcc@9.3.0 patches=4e1d78c,62fc8a8 arch=linux-ubuntu20.04-x86_64": spec-0.json
 - "hsakmt-roct@4.1.0%gcc@8.3.1~ipo+shared build_type=Release arch=linux-rhel8-x86_64 ^numactl@2.0.14%gcc@8.3.1 patches=4e1d78c,62fc8a8 arch=linux-rhel8-x86_64": spec-1.json
 - "hsakmt-roct@4.0.0%gcc@8.3.1~ipo build_type=Release arch=linux-rhel8-x86_64 ^numactl@2.0.14%gcc@8.3.1 patches=4e1d78c arch=linux-rhel8-x86_64": spec-2.json
 - "hsakmt-roct@4.0.0%gcc@7.5.0~ipo build_type=Release arch=linux-ubuntu18.04-x86_64 ^numactl@2.0.14%gcc@7.5.0 patches=4e1d78c,62fc8a8 arch=linux-ubuntu18.04-x86_64": spec-3.json
 - "hsakmt-roct@4.2.0%gcc@8.3.1~ipo+shared build_type=Release arch=linux-rhel8-x86_64 ^numactl@2.0.14%gcc@8.3.1 patches=4e1d78c,62fc8a8 arch=linux-rhel8-x86_64": spec-4.json
 - "hsakmt-roct@4.0.0%gcc@8.1.0~ipo build_type=Release arch=linux-rhel7-x86_64 ^numactl@2.0.14%gcc@8.1.0 patches=4e1d78c arch=linux-rhel7-x86_64": spec-5.json
 - "hsakmt-roct@4.0.0%gcc@8.3.1~ipo build_type=Release arch=linux-rhel8-x86_64 ^numactl@2.0.14%gcc@8.3.1 patches=4e1d78c,62fc8a8 arch=linux-rhel8-x86_64": spec-6.json
 - "hsakmt-roct@4.1.0%gcc@9.3.0~ipo build_type=Release arch=linux-ubuntu20.04-x86_64 ^numactl@2.0.14%gcc@9.3.0 patches=4e1d78c,62fc8a8 arch=linux-ubuntu20.04-x86_64": spec-7.json
 - "hsakmt-roct@4.0.0%gcc@9.3.0~ipo build_type=Release arch=linux-ubuntu20.04-x86_64 ^numactl@2.0.14%gcc@9.3.0 patches=4e1d78c arch=linux-ubuntu20.04-x86_64": spec-8.json
 - "hsakmt-roct@4.0.0%gcc@8.1.0~ipo build_type=Release arch=linux-rhel7-x86_64 ^numactl@2.0.14%gcc@8.1.0 patches=4e1d78c,62fc8a8 arch=linux-rhel7-x86_64": spec-9.json
 - "hsakmt-roct@4.1.0%gcc@8.1.0~ipo build_type=Release arch=linux-rhel7-x86_64 ^numactl@2.0.14%gcc@8.1.0 patches=4e1d78c,62fc8a8 arch=linux-rhel7-x86_64": spec-10.json
 - "hsakmt-roct@4.0.0%gcc@7.5.0~ipo build_type=Release arch=linux-ubuntu18.04-x86_64 ^numactl@2.0.14%gcc@7.5.0 patches=4e1d78c arch=linux-ubuntu18.04-x86_64": spec-11.json
 - "hsakmt-roct@4.1.0%gcc@7.5.0~ipo build_type=Release arch=linux-ubuntu18.04-x86_64 ^numactl@2.0.14%gcc@7.5.0 patches=4e1d78c,62fc8a8 arch=linux-ubuntu18.04-x86_64": spec-12.json
 - "hsakmt-roct@4.1.0%gcc@8.3.1~ipo build_type=Release arch=linux-rhel8-x86_64 ^numactl@2.0.14%gcc@8.3.1 patches=4e1d78c,62fc8a8 arch=linux-rhel8-x86_64": spec-13.json
 - "hsakmt-roct@3.9.0%gcc@7.5.0~ipo build_type=Release arch=linux-ubuntu18.04-x86_64 ^numactl@2.0.14%gcc@7.5.0 patches=4e1d78c arch=linux-ubuntu18.04-x86_64": spec-14.json
 - "hsakmt-roct@4.2.0%gcc@9.3.0~ipo+shared build_type=Release arch=linux-rhel7-x86_64 ^numactl@2.0.14%gcc@9.3.0 patches=4e1d78c,62fc8a8 arch=linux-rhel7-x86_64": spec-15.json
 - "hsakmt-roct@3.9.0%gcc@9.3.0~ipo build_type=Release arch=linux-ubuntu20.04-x86_64 ^numactl@2.0.14%gcc@9.3.0 patches=4e1d78c arch=linux-ubuntu20.04-x86_64": spec-16.json
 - "hsakmt-roct@4.2.0%gcc@9.3.0~ipo+shared build_type=Release arch=linux-ubuntu20.04-x86_64 ^numactl@2.0.14%gcc@9.3.0 patches=4e1d78c,62fc8a8 arch=linux-ubuntu20.04-x86_64": spec-17.json
 - "hsakmt-roct@4.2.0%gcc@10.3.0~ipo+shared build_type=Release arch=linux-ubuntu21.04-x86_64 ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78c,62fc8a8 arch=linux-ubuntu21.04-x86_64": spec-18.json
 - "hsakmt-roct@4.2.0%gcc@7.5.0~ipo+shared build_type=Release arch=linux-ubuntu18.04-x86_64 ^numactl@2.0.14%gcc@7.5.0 patches=4e1d78c,62fc8a8 arch=linux-ubuntu18.04-x86_64": spec-19.json
 - "hsakmt-roct@4.1.0%gcc@9.3.0~ipo build_type=Release arch=linux-rhel7-x86_64 ^numactl@2.0.14%gcc@9.3.0 patches=4e1d78c,62fc8a8 arch=linux-rhel7-x86_64": spec-20.json
 - "hsakmt-roct@3.9.0%gcc@8.3.1~ipo build_type=Release arch=linux-rhel8-x86_64 ^numactl@2.0.14%gcc@8.3.1 patches=4e1d78c arch=linux-rhel8-x86_64": spec-21.json
 - "hsakmt-roct@4.1.0%gcc@9.3.0~ipo+shared build_type=Release arch=linux-rhel7-x86_64 ^numactl@2.0.14%gcc@9.3.0 patches=4e1d78c,62fc8a8 arch=linux-rhel7-x86_64": spec-22.json
 - "hsakmt-roct@4.1.0%gcc@7.5.0~ipo+shared build_type=Release arch=linux-ubuntu18.04-x86_64 ^numactl@2.0.14%gcc@7.5.0 patches=4e1d78c,62fc8a8 arch=linux-ubuntu18.04-x86_64": spec-23.json
 - "hsakmt-roct@3.9.0%gcc@8.1.0~ipo build_type=Release arch=linux-rhel7-x86_64 ^numactl@2.0.14%gcc@8.1.0 patches=4e1d78c arch=linux-rhel7-x86_64": spec-24.json
 - "hsakmt-roct@4.2.0%gcc@8.4.1~ipo+shared build_type=Release arch=linux-rhel8-x86_64 ^numactl@2.0.14%gcc@8.4.1 patches=4e1d78c,62fc8a8 arch=linux-rhel8-x86_64": spec-25.json
 - "hsakmt-roct@4.1.0%gcc@9.3.0~ipo+shared build_type=Release arch=linux-ubuntu20.04-x86_64 ^numactl@2.0.14%gcc@9.3.0 patches=4e1d78c,62fc8a8 arch=linux-ubuntu20.04-x86_64": spec-26.json

---