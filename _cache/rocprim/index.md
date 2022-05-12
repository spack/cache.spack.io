---
title: "rocprim"
layout: cache
category: package
meta: {"versions": ["4.1.0"], "compilers": ["gcc@8.3.1", "gcc@7.5.0", "gcc@9.3.0"]}
spec_files: 
 - "rocprim@4.1.0%gcc@9.3.0~ipo build_type=Release arch=linux-rhel7-x86_64 ^numactl@2.0.14%gcc@9.3.0 patches=4e1d78c,62fc8a8 arch=linux-rhel7-x86_64": spec-0.json
 - "rocprim@4.1.0%gcc@7.5.0~ipo build_type=Release arch=linux-ubuntu18.04-x86_64 ^numactl@2.0.14%gcc@7.5.0 patches=4e1d78c,62fc8a8 arch=linux-ubuntu18.04-x86_64": spec-1.json
 - "rocprim@4.1.0%gcc@9.3.0~ipo build_type=Release arch=linux-ubuntu20.04-x86_64 ^numactl@2.0.14%gcc@9.3.0 patches=4e1d78c,62fc8a8 arch=linux-ubuntu20.04-x86_64": spec-2.json
 - "rocprim@4.1.0%gcc@8.3.1~ipo build_type=Release arch=linux-rhel8-x86_64 ^numactl@2.0.14%gcc@8.3.1 patches=4e1d78c,62fc8a8 arch=linux-rhel8-x86_64": spec-3.json

---