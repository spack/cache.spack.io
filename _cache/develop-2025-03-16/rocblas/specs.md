---
title: "rocblas"
layout: cache
categories: [package, develop-2025-03-16]
meta: {"compilers": ["gcc@=11.4.0", "gcc@=13.2.0"], "num_specs": 2, "num_specs_by_stack": {"e4s": 1, "ml-linux-x86_64-rocm": 1, "root": 2}, "oss": ["ubuntu22.04", "ubuntu24.04"], "platforms": ["linux"], "stacks": ["e4s", "ml-linux-x86_64-rocm", "root"], "targets": ["x86_64_v3"], "versions": ["6.1.2", "6.3.2"]}
spec_details: [{"compiler": "gcc@=11.4.0", "hash": "65mff2fwjunr3gnuownyidim2ixzsaky", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "target": "x86_64_v3", "variants": ["amdgpu_target=auto", "~asan", "build_system=cmake", "build_type=Release", "generator=make", "~ipo", "+tensile"], "versions": ["6.3.2"]}, {"compiler": "gcc@=13.2.0", "hash": "me4k66cz2mv4bebfyncdhnztdn6dh7wh", "os": "ubuntu24.04", "platform": "linux", "size": "-", "stacks": ["ml-linux-x86_64-rocm", "root"], "target": "x86_64_v3", "variants": ["amdgpu_target=gfx90a", "~asan", "build_system=cmake", "build_type=Release", "generator=make", "~ipo", "+tensile"], "versions": ["6.1.2"]}]
---