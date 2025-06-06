---
title: "ffmpeg"
layout: cache
categories: [package, develop-2024-03-24]
meta: {"versions": ["6.0"], "compilers": ["gcc@=11.4.0", "gcc@=9.4.0", "oneapi@=2024.0.0"], "oss": ["ubuntu20.04", "ubuntu22.04"], "platforms": ["linux"], "targets": ["neoverse_v1", "neoverse_v2", "ppc64le", "x86_64_v3"], "stacks": ["e4s", "e4s-neoverse-v2", "e4s-neoverse_v1", "e4s-oneapi", "e4s-power", "root"], "num_specs": 5, "num_specs_by_stack": {"e4s-power": 1, "root": 5, "e4s-neoverse_v1": 1, "e4s-neoverse-v2": 1, "e4s": 1, "e4s-oneapi": 1}}
spec_details: [{"hash": "qnuutwhkzpnlflcuz2kb75jt6cytg3cz", "compiler": "gcc@=9.4.0", "versions": ["6.0"], "os": "ubuntu20.04", "platform": "linux", "target": "ppc64le", "variants": ["~X", "build_system=autotools", "+bzlib", "~doc", "~drawtext", "+gpl", "~libaom", "~libmp3lame", "~libopenjpeg", "~libopus", "~libsnappy", "~libspeex", "~libssh", "~libvorbis", "~libvpx", "~libwebp", "~libx264", "~libxml2", "~libzmq", "~lzma", "~nonfree", "~openssl", "patches=416751f,f070ac1", "~sdl2", "+shared", "+version3"], "stacks": ["e4s-power", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2024-03-24/build_cache/linux-ubuntu20.04-ppc64le/gcc-9.4.0/ffmpeg-6.0/linux-ubuntu20.04-ppc64le-gcc-9.4.0-ffmpeg-6.0-qnuutwhkzpnlflcuz2kb75jt6cytg3cz.spack"}, {"hash": "42ltsvnvikow3bu2k2om57oevehevteq", "compiler": "gcc@=11.4.0", "versions": ["6.0"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v1", "variants": ["~X", "build_system=autotools", "+bzlib", "~doc", "~drawtext", "+gpl", "~libaom", "~libmp3lame", "~libopenjpeg", "~libopus", "~libsnappy", "~libspeex", "~libssh", "~libvorbis", "~libvpx", "~libwebp", "~libx264", "~libxml2", "~libzmq", "~lzma", "~nonfree", "~openssl", "patches=416751f,f070ac1", "~sdl2", "+shared", "+version3"], "stacks": ["e4s-neoverse_v1", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2024-03-24/build_cache/linux-ubuntu22.04-neoverse_v1/gcc-11.4.0/ffmpeg-6.0/linux-ubuntu22.04-neoverse_v1-gcc-11.4.0-ffmpeg-6.0-42ltsvnvikow3bu2k2om57oevehevteq.spack"}, {"hash": "33trqef42ewo36twnqr6vbpq45bexfcx", "compiler": "gcc@=11.4.0", "versions": ["6.0"], "os": "ubuntu22.04", "platform": "linux", "target": "neoverse_v2", "variants": ["~X", "build_system=autotools", "+bzlib", "~doc", "~drawtext", "+gpl", "~libaom", "~libmp3lame", "~libopenjpeg", "~libopus", "~libsnappy", "~libspeex", "~libssh", "~libvorbis", "~libvpx", "~libwebp", "~libx264", "~libxml2", "~libzmq", "~lzma", "~nonfree", "~openssl", "patches=416751f,f070ac1", "~sdl2", "+shared", "+version3"], "stacks": ["root", "e4s-neoverse-v2"], "size": "-", "tarball": "https://binaries.spack.io/develop-2024-03-24/build_cache/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/ffmpeg-6.0/linux-ubuntu22.04-neoverse_v2-gcc-11.4.0-ffmpeg-6.0-33trqef42ewo36twnqr6vbpq45bexfcx.spack"}, {"hash": "hppgkgasfhj6zmzev6oqp3lpuumvsb72", "compiler": "gcc@=11.4.0", "versions": ["6.0"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~X", "build_system=autotools", "+bzlib", "~doc", "~drawtext", "+gpl", "~libaom", "~libmp3lame", "~libopenjpeg", "~libopus", "~libsnappy", "~libspeex", "~libssh", "~libvorbis", "~libvpx", "~libwebp", "~libx264", "~libxml2", "~libzmq", "~lzma", "~nonfree", "~openssl", "patches=416751f,f070ac1", "~sdl2", "+shared", "+version3"], "stacks": ["root", "e4s"], "size": "-", "tarball": "https://binaries.spack.io/develop-2024-03-24/build_cache/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/ffmpeg-6.0/linux-ubuntu22.04-x86_64_v3-gcc-11.4.0-ffmpeg-6.0-hppgkgasfhj6zmzev6oqp3lpuumvsb72.spack"}, {"hash": "avwc7auqolwlxrp7jwkq6yviq6opj34o", "compiler": "oneapi@=2024.0.0", "versions": ["6.0"], "os": "ubuntu22.04", "platform": "linux", "target": "x86_64_v3", "variants": ["~X", "build_system=autotools", "+bzlib", "~doc", "~drawtext", "+gpl", "~libaom", "~libmp3lame", "~libopenjpeg", "~libopus", "~libsnappy", "~libspeex", "~libssh", "~libvorbis", "~libvpx", "~libwebp", "~libx264", "~libxml2", "~libzmq", "~lzma", "~nonfree", "~openssl", "patches=416751f,f070ac1", "~sdl2", "+shared", "+version3"], "stacks": ["e4s-oneapi", "root"], "size": "-", "tarball": "https://binaries.spack.io/develop-2024-03-24/build_cache/linux-ubuntu22.04-x86_64_v3/oneapi-2024.0.0/ffmpeg-6.0/linux-ubuntu22.04-x86_64_v3-oneapi-2024.0.0-ffmpeg-6.0-avwc7auqolwlxrp7jwkq6yviq6opj34o.spack"}]
---