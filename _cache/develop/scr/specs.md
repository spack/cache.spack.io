---
title: "scr"
layout: cache
categories: [package, develop]
meta: {"compilers": ["gcc@=11.4.0", "gcc@=7.5.0", "gcc@=9.4.0", "oneapi@=2024.2.1"], "num_specs": 37, "num_specs_by_stack": {"e4s": 6, "e4s-neoverse-v2": 6, "e4s-neoverse_v1": 3, "e4s-oneapi": 6, "e4s-power": 2, "radiuss": 6, "root": 37, "tutorial": 6}, "oss": ["ubuntu18.04", "ubuntu20.04", "ubuntu22.04"], "platforms": ["linux"], "stacks": ["e4s", "e4s-neoverse-v2", "e4s-neoverse_v1", "e4s-oneapi", "e4s-power", "radiuss", "root", "tutorial"], "targets": ["neoverse_v1", "neoverse_v2", "ppc64le", "x86_64_v3"], "versions": ["2.0.0", "3.1.0"]}
spec_details: [{"compiler": "gcc@=7.5.0", "hash": "4wadym3ypxt2wvyw3asyjjptht7r7vd3", "os": "ubuntu18.04", "platform": "linux", "size": "-", "stacks": ["radiuss", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu18.04-x86_64_v3/gcc-7.5.0/scr-3.1.0/linux-ubuntu18.04-x86_64_v3-gcc-7.5.0-scr-3.1.0-4wadym3ypxt2wvyw3asyjjptht7r7vd3.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "5tb3tey4wv54nlxnf3vpr65phr6ongaa", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse-v2", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-scr-3.1.0-5tb3tey4wv54nlxnf3vpr65phr6ongaa.spack", "target": "neoverse_v2", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "64fi2y3cn6gd6y6xpjbbugtxbjmhi3w5", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-3.1.0-64fi2y3cn6gd6y6xpjbbugtxbjmhi3w5.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "oneapi@=2024.2.1", "hash": "7zxxyg3yurjxccxztk6r76qotp4b3nfh", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-oneapi", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.2.1/scr-3.1.0/linux-ubuntu22.04-x86_64_v3-oneapi-2024.2.1-scr-3.1.0-7zxxyg3yurjxccxztk6r76qotp4b3nfh.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "b35whiyk5slwg3qjgrba2hv55qz673qe", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["root", "tutorial"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-2.0.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-2.0.0-b35whiyk5slwg3qjgrba2hv55qz673qe.spack", "target": "x86_64_v3", "variants": ["async_api=NONE", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "+dtcmp", "file_lock=FLOCK", "~fortran", "generator=make", "~ipo", "+libyogrt", "resource_manager=SLURM", "scr_config=scr.conf"], "versions": ["2.0.0"]}, {"compiler": "gcc@=7.5.0", "hash": "ctbw4iombzco26ul6abcqft6t2zreuup", "os": "ubuntu18.04", "platform": "linux", "size": "-", "stacks": ["radiuss", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu18.04-x86_64_v3/gcc-7.5.0/scr-3.1.0/linux-ubuntu18.04-x86_64_v3-gcc-7.5.0-scr-3.1.0-ctbw4iombzco26ul6abcqft6t2zreuup.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=7.5.0", "hash": "cu7qz6liukcmzdwdpjrscgj3a5376nyd", "os": "ubuntu18.04", "platform": "linux", "size": "-", "stacks": ["radiuss", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu18.04-x86_64_v3/gcc-7.5.0/scr-3.1.0/linux-ubuntu18.04-x86_64_v3-gcc-7.5.0-scr-3.1.0-cu7qz6liukcmzdwdpjrscgj3a5376nyd.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "d7iyl6p5re7kmdwh6hj7e2ld6fij3rd7", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-2.0.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-2.0.0-d7iyl6p5re7kmdwh6hj7e2ld6fij3rd7.spack", "target": "x86_64_v3", "variants": ["async_api=NONE", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "+dtcmp", "file_lock=FLOCK", "~fortran", "generator=make", "~ipo", "+libyogrt", "resource_manager=SLURM", "scr_config=scr.conf"], "versions": ["2.0.0"]}, {"compiler": "gcc@=11.4.0", "hash": "ff5l6au36lygwf7k77sbigdbcz3acsv2", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse-v2", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-scr-3.1.0-ff5l6au36lygwf7k77sbigdbcz3acsv2.spack", "target": "neoverse_v2", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=7.5.0", "hash": "fpotlkzovvyzjru7sgjearkeiynbjf4h", "os": "ubuntu18.04", "platform": "linux", "size": "-", "stacks": ["radiuss", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu18.04-x86_64_v3/gcc-7.5.0/scr-3.1.0/linux-ubuntu18.04-x86_64_v3-gcc-7.5.0-scr-3.1.0-fpotlkzovvyzjru7sgjearkeiynbjf4h.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "fqj5m6w7fz54doxv4ajuir5rauknknjy", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse_v1", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-scr-3.1.0-fqj5m6w7fz54doxv4ajuir5rauknknjy.spack", "target": "neoverse_v1", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "gkimukn5peok4tlx6po77cvdgjq4ruur", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-3.1.0-gkimukn5peok4tlx6po77cvdgjq4ruur.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "oneapi@=2024.2.1", "hash": "h4p5w6p4uligepexwqcxqhlu2c4u2ood", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-oneapi", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.2.1/scr-3.1.0/linux-ubuntu22.04-x86_64_v3-oneapi-2024.2.1-scr-3.1.0-h4p5w6p4uligepexwqcxqhlu2c4u2ood.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "hxwqmob4vt4qcd6etza7kvycvhiomd45", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["root", "tutorial"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-2.0.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-2.0.0-hxwqmob4vt4qcd6etza7kvycvhiomd45.spack", "target": "x86_64_v3", "variants": ["async_api=NONE", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "+dtcmp", "file_lock=FLOCK", "~fortran", "generator=make", "~ipo", "+libyogrt", "resource_manager=SLURM", "scr_config=scr.conf"], "versions": ["2.0.0"]}, {"compiler": "gcc@=11.4.0", "hash": "hy5i24wmstihrez72cmrcxx7x6ghk5kd", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse_v1", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-scr-3.1.0-hy5i24wmstihrez72cmrcxx7x6ghk5kd.spack", "target": "neoverse_v1", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=7.5.0", "hash": "itl2ubm7k3szoy6uig2byfwlqbmkrddr", "os": "ubuntu18.04", "platform": "linux", "size": "-", "stacks": ["root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu18.04-x86_64_v3/gcc-7.5.0/scr-3.1.0/linux-ubuntu18.04-x86_64_v3-gcc-7.5.0-scr-3.1.0-itl2ubm7k3szoy6uig2byfwlqbmkrddr.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "oneapi@=2024.2.1", "hash": "j42xxokhv43stg4t73occem6kak5dbzo", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-oneapi", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.2.1/scr-3.1.0/linux-ubuntu22.04-x86_64_v3-oneapi-2024.2.1-scr-3.1.0-j42xxokhv43stg4t73occem6kak5dbzo.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "mfx6y56lpsxn3ltn2hgqheej6th56pne", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse-v2", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-scr-3.1.0-mfx6y56lpsxn3ltn2hgqheej6th56pne.spack", "target": "neoverse_v2", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "mi2bwsfdv2tfq352roagaev4y3nnaauh", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-3.1.0-mi2bwsfdv2tfq352roagaev4y3nnaauh.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=9.4.0", "hash": "o5axc7nepcicppnxqrkrnrcyun7tc577", "os": "ubuntu20.04", "platform": "linux", "size": "-", "stacks": ["e4s-power", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu20.04-ppc64le/gcc-9.4.0/scr-3.1.0/linux-ubuntu20.04-ppc64le-gcc-9.4.0-scr-3.1.0-o5axc7nepcicppnxqrkrnrcyun7tc577.spack", "target": "ppc64le", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "oq3fziczmuiyatmp2eivyky6qg4nxh7n", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse-v2", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-scr-3.1.0-oq3fziczmuiyatmp2eivyky6qg4nxh7n.spack", "target": "neoverse_v2", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=7.5.0", "hash": "oqbtt2wf2kzw7jg2juevlmof56bpgmin", "os": "ubuntu18.04", "platform": "linux", "size": "-", "stacks": ["radiuss", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu18.04-x86_64_v3/gcc-7.5.0/scr-3.1.0/linux-ubuntu18.04-x86_64_v3-gcc-7.5.0-scr-3.1.0-oqbtt2wf2kzw7jg2juevlmof56bpgmin.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "q2yatcprqydicsnpic3picefuhfbasgf", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-3.1.0-q2yatcprqydicsnpic3picefuhfbasgf.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "s2lxe725ohmz7ggye7ydkdaynx6bhcal", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["root", "tutorial"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-2.0.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-2.0.0-s2lxe725ohmz7ggye7ydkdaynx6bhcal.spack", "target": "x86_64_v3", "variants": ["async_api=NONE", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "+dtcmp", "file_lock=FLOCK", "~fortran", "generator=make", "~ipo", "+libyogrt", "resource_manager=SLURM", "scr_config=scr.conf"], "versions": ["2.0.0"]}, {"compiler": "gcc@=11.4.0", "hash": "tapekfhomdibzcgpichrx7ravfwthibd", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse-v2", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-scr-3.1.0-tapekfhomdibzcgpichrx7ravfwthibd.spack", "target": "neoverse_v2", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=9.4.0", "hash": "tu4ydw27dnchm4xy5sueigmulowmghw2", "os": "ubuntu20.04", "platform": "linux", "size": "-", "stacks": ["e4s-power", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu20.04-ppc64le/gcc-9.4.0/scr-3.1.0/linux-ubuntu20.04-ppc64le-gcc-9.4.0-scr-3.1.0-tu4ydw27dnchm4xy5sueigmulowmghw2.spack", "target": "ppc64le", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "oneapi@=2024.2.1", "hash": "tvtdkzamerx2blza2krvg3yxmhmdo4yc", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-oneapi", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.2.1/scr-3.1.0/linux-ubuntu22.04-x86_64_v3-oneapi-2024.2.1-scr-3.1.0-tvtdkzamerx2blza2krvg3yxmhmdo4yc.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "oneapi@=2024.2.1", "hash": "ugj52ok72ij5h4dlmulgikjm5krcnp3y", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-oneapi", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.2.1/scr-3.1.0/linux-ubuntu22.04-x86_64_v3-oneapi-2024.2.1-scr-3.1.0-ugj52ok72ij5h4dlmulgikjm5krcnp3y.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=7.5.0", "hash": "ugvkv53acdgup2vejebbrd4vc7bgpqnc", "os": "ubuntu18.04", "platform": "linux", "size": "-", "stacks": ["radiuss", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu18.04-x86_64_v3/gcc-7.5.0/scr-3.1.0/linux-ubuntu18.04-x86_64_v3-gcc-7.5.0-scr-3.1.0-ugvkv53acdgup2vejebbrd4vc7bgpqnc.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "vdcpncnj644lrws5ig7sfadn3ty4lntp", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse_v1", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-scr-3.1.0-vdcpncnj644lrws5ig7sfadn3ty4lntp.spack", "target": "neoverse_v1", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "vwibqfrxi7mgxhswzgo5brpxkesgqcmo", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-neoverse-v2", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-scr-3.1.0-vwibqfrxi7mgxhswzgo5brpxkesgqcmo.spack", "target": "neoverse_v2", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "wsojtpb3dmzqr4su2fscy2ez465wlrza", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-3.1.0-wsojtpb3dmzqr4su2fscy2ez465wlrza.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "xjfoscoru7mom5injvciqmoa2tcozcby", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-3.1.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-3.1.0-xjfoscoru7mom5injvciqmoa2tcozcby.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}, {"compiler": "gcc@=11.4.0", "hash": "y3pkctsm77hm5c6imejb7xc6ps56emyj", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["root", "tutorial"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-2.0.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-2.0.0-y3pkctsm77hm5c6imejb7xc6ps56emyj.spack", "target": "x86_64_v3", "variants": ["async_api=NONE", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "+dtcmp", "file_lock=FLOCK", "~fortran", "generator=make", "~ipo", "+libyogrt", "resource_manager=SLURM", "scr_config=scr.conf"], "versions": ["2.0.0"]}, {"compiler": "gcc@=11.4.0", "hash": "zx4r44nhjt7rqdictavmj2upoagj33nz", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["root", "tutorial"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-2.0.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-2.0.0-zx4r44nhjt7rqdictavmj2upoagj33nz.spack", "target": "x86_64_v3", "variants": ["async_api=NONE", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "+dtcmp", "file_lock=FLOCK", "~fortran", "generator=make", "~ipo", "+libyogrt", "resource_manager=SLURM", "scr_config=scr.conf"], "versions": ["2.0.0"]}, {"compiler": "gcc@=11.4.0", "hash": "zysrthn3ks6gaogrth4eutyynvpgtmen", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["root", "tutorial"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/scr-2.0.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-scr-2.0.0-zysrthn3ks6gaogrth4eutyynvpgtmen.spack", "target": "x86_64_v3", "variants": ["async_api=NONE", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "+dtcmp", "file_lock=FLOCK", "~fortran", "generator=make", "~ipo", "+libyogrt", "resource_manager=SLURM", "scr_config=scr.conf"], "versions": ["2.0.0"]}, {"compiler": "oneapi@=2024.2.1", "hash": "zz3s4wkzgwucotoyo3acfmyepylmwzio", "os": "ubuntu22.04", "platform": "linux", "size": "-", "stacks": ["e4s-oneapi", "root"], "tarball": "https://binaries.spack.io/develop/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.2.1/scr-3.1.0/linux-ubuntu22.04-x86_64_v3-oneapi-2024.2.1-scr-3.1.0-zz3s4wkzgwucotoyo3acfmyepylmwzio.spack", "target": "x86_64_v3", "variants": ["~bbapi", "build_system=cmake", "build_type=Release", "cache_base=/dev/shm", "cntl_base=/dev/shm", "copy_config=none", "~dw", "+examples", "file_lock=FLOCK", "+fortran", "generator=make", "~ipo", "+libyogrt", "+pdsh", "+pthreads", "resource_manager=SLURM", "scr_config=scr.conf", "+shared", "+tests"], "versions": ["3.1.0"]}]
---