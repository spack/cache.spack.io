---
title: "libevent"
layout: cache
category: package
meta: {"versions": ["2.1.12", "2.1.8"], "compilers": ["apple-clang@12.0.0", "gcc@8.3.1", "gcc@9.3.0", "gcc@8.1.0", "gcc@7.5.0", "gcc@7.3.1", "gcc@8.4.1", "gcc@10.3.0"]}
spec_files: 
 - "libevent@2.1.12%gcc@9.3.0+openssl arch=linux-rhel7-ppc64le ^openssl@1.1.1k%gcc@9.3.0~docs+systemcerts arch=linux-rhel7-ppc64le ^zlib@1.2.11%gcc@9.3.0+optimize+pic+shared arch=linux-rhel7-ppc64le": spec-0.json
 - "libevent@2.1.12%gcc@7.5.0+openssl arch=linux-ubuntu18.04-x86_64 ^openssl@1.1.1j%gcc@7.5.0+systemcerts arch=linux-ubuntu18.04-x86_64 ^zlib@1.2.11%gcc@7.5.0+optimize+pic+shared arch=linux-ubuntu18.04-x86_64": spec-1.json
 - "libevent@2.1.12%apple-clang@12.0.0+openssl arch=darwin-catalina-x86_64 ^openssl@1.1.1k%apple-clang@12.0.0~docs+systemcerts arch=darwin-catalina-x86_64 ^zlib@1.2.11%apple-clang@12.0.0+optimize+pic+shared arch=darwin-catalina-x86_64": spec-2.json
 - "libevent@2.1.12%gcc@8.3.1+openssl arch=linux-rhel8-x86_64 ^openssl@1.1.1k%gcc@8.3.1~docs+systemcerts arch=linux-rhel8-x86_64 ^zlib@1.2.11%gcc@8.3.1+optimize+pic+shared arch=linux-rhel8-x86_64": spec-3.json
 - "libevent@2.1.12%gcc@8.1.0+openssl arch=linux-rhel7-x86_64 ^openssl@1.1.1k%gcc@8.1.0~docs+systemcerts arch=linux-rhel7-x86_64 ^zlib@1.2.11%gcc@8.1.0+optimize+pic+shared arch=linux-rhel7-x86_64": spec-4.json
 - "libevent@2.1.12%gcc@8.1.0+openssl arch=linux-rhel7-x86_64 ^openssl@1.1.1j%gcc@8.1.0+systemcerts arch=linux-rhel7-x86_64 ^zlib@1.2.11%gcc@8.1.0+optimize+pic+shared arch=linux-rhel7-x86_64": spec-5.json
 - "libevent@2.1.12%gcc@7.5.0+openssl arch=linux-ubuntu18.04-ppc64le ^openssl@1.1.1k%gcc@7.5.0~docs+systemcerts arch=linux-ubuntu18.04-ppc64le ^zlib@1.2.11%gcc@7.5.0+optimize+pic+shared arch=linux-ubuntu18.04-ppc64le": spec-6.json
 - "libevent@2.1.8%gcc@7.5.0+openssl arch=linux-ubuntu18.04-x86_64 ^openssl@1.1.1i%gcc@7.5.0+systemcerts arch=linux-ubuntu18.04-x86_64 ^zlib@1.2.11%gcc@7.5.0+optimize+pic+shared arch=linux-ubuntu18.04-x86_64": spec-7.json
 - "libevent@2.1.12%gcc@9.3.0+openssl arch=linux-ubuntu20.04-x86_64 ^openssl@1.1.1k%gcc@9.3.0~docs+systemcerts arch=linux-ubuntu20.04-x86_64 ^zlib@1.2.11%gcc@9.3.0+optimize+pic+shared arch=linux-ubuntu20.04-x86_64": spec-8.json
 - "libevent@2.1.12%gcc@9.3.0+openssl arch=linux-ubuntu20.04-x86_64 ^openssl@1.1.1j%gcc@9.3.0+systemcerts arch=linux-ubuntu20.04-x86_64 ^zlib@1.2.11%gcc@9.3.0+optimize+pic+shared arch=linux-ubuntu20.04-x86_64": spec-9.json
 - "libevent@2.1.12%gcc@8.3.1+openssl arch=linux-rhel8-ppc64le ^openssl@1.1.1j%gcc@8.3.1+systemcerts arch=linux-rhel8-ppc64le ^zlib@1.2.11%gcc@8.3.1+optimize+pic+shared arch=linux-rhel8-ppc64le": spec-10.json
 - "libevent@2.1.12%gcc@9.3.0+openssl arch=linux-ubuntu20.04-ppc64le ^openssl@1.1.1j%gcc@9.3.0~docs+systemcerts arch=linux-ubuntu20.04-ppc64le ^zlib@1.2.11%gcc@9.3.0+optimize+pic+shared arch=linux-ubuntu20.04-ppc64le": spec-11.json
 - "libevent@2.1.12%gcc@8.1.0+openssl arch=linux-rhel7-x86_64 ^openssl@1.1.1j%gcc@8.1.0~docs+systemcerts arch=linux-rhel7-x86_64 ^zlib@1.2.11%gcc@8.1.0+optimize+pic+shared arch=linux-rhel7-x86_64": spec-12.json
 - "libevent@2.1.12%gcc@9.3.0+openssl arch=linux-ubuntu20.04-ppc64le ^openssl@1.1.1j%gcc@9.3.0+systemcerts arch=linux-ubuntu20.04-ppc64le ^zlib@1.2.11%gcc@9.3.0+optimize+pic+shared arch=linux-ubuntu20.04-ppc64le": spec-13.json
 - "libevent@2.1.12%gcc@7.5.0+openssl arch=linux-ubuntu18.04-x86_64 ^openssl@1.1.1k%gcc@7.5.0~docs+systemcerts arch=linux-ubuntu18.04-x86_64 ^zlib@1.2.11%gcc@7.5.0+optimize+pic+shared arch=linux-ubuntu18.04-x86_64": spec-14.json
 - "libevent@2.1.12%gcc@8.3.1+openssl arch=linux-rhel8-ppc64le ^openssl@1.1.1j%gcc@8.3.1~docs+systemcerts arch=linux-rhel8-ppc64le ^zlib@1.2.11%gcc@8.3.1+optimize+pic+shared arch=linux-rhel8-ppc64le": spec-15.json
 - "libevent@2.1.12%gcc@8.3.1+openssl arch=linux-rhel8-x86_64 ^openssl@1.1.1j%gcc@8.3.1~docs+systemcerts arch=linux-rhel8-x86_64 ^zlib@1.2.11%gcc@8.3.1+optimize+pic+shared arch=linux-rhel8-x86_64": spec-16.json
 - "libevent@2.1.12%gcc@10.3.0+openssl arch=linux-ubuntu21.04-ppc64le ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-ubuntu21.04-ppc64le ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-ubuntu21.04-ppc64le": spec-17.json
 - "libevent@2.1.12%gcc@8.1.0+openssl arch=linux-rhel7-ppc64le ^openssl@1.1.1k%gcc@8.1.0~docs+systemcerts arch=linux-rhel7-ppc64le ^zlib@1.2.11%gcc@8.1.0+optimize+pic+shared arch=linux-rhel7-ppc64le": spec-18.json
 - "libevent@2.1.12%gcc@7.3.1+openssl arch=linux-amzn2-x86_64 ^openssl@1.1.1j%gcc@7.3.1+systemcerts arch=linux-amzn2-x86_64 ^zlib@1.2.11%gcc@7.3.1+optimize+pic+shared arch=linux-amzn2-x86_64": spec-19.json
 - "libevent@2.1.12%gcc@7.5.0+openssl arch=linux-ubuntu18.04-ppc64le ^openssl@1.1.1j%gcc@7.5.0~docs+systemcerts arch=linux-ubuntu18.04-ppc64le ^zlib@1.2.11%gcc@7.5.0+optimize+pic+shared arch=linux-ubuntu18.04-ppc64le": spec-20.json
 - "libevent@2.1.12%gcc@8.1.0+openssl arch=linux-rhel7-ppc64le ^openssl@1.1.1j%gcc@8.1.0~docs+systemcerts arch=linux-rhel7-ppc64le ^zlib@1.2.11%gcc@8.1.0+optimize+pic+shared arch=linux-rhel7-ppc64le": spec-21.json
 - "libevent@2.1.12%gcc@8.1.0+openssl arch=linux-rhel7-x86_64 ^openssl@1.1.1i%gcc@8.1.0+systemcerts arch=linux-rhel7-x86_64 ^zlib@1.2.11%gcc@8.1.0+optimize+pic+shared arch=linux-rhel7-x86_64": spec-22.json
 - "libevent@2.1.12%gcc@8.4.1+openssl arch=linux-rhel8-ppc64le ^openssl@1.1.1k%gcc@8.4.1~docs+systemcerts arch=linux-rhel8-ppc64le ^zlib@1.2.11%gcc@8.4.1+optimize+pic+shared arch=linux-rhel8-ppc64le": spec-23.json
 - "libevent@2.1.12%gcc@9.3.0+openssl arch=cray-cnl7-haswell ^openssl@1.1.1k%gcc@9.3.0~docs+systemcerts arch=cray-cnl7-haswell ^zlib@1.2.11%gcc@9.3.0+optimize+pic+shared arch=cray-cnl7-haswell": spec-24.json
 - "libevent@2.1.12%gcc@9.3.0+openssl arch=linux-ubuntu20.04-x86_64 ^openssl@1.1.1j%gcc@9.3.0~docs+systemcerts arch=linux-ubuntu20.04-x86_64 ^zlib@1.2.11%gcc@9.3.0+optimize+pic+shared arch=linux-ubuntu20.04-x86_64": spec-25.json
 - "libevent@2.1.12%gcc@8.1.0+openssl arch=linux-rhel7-ppc64le ^openssl@1.1.1j%gcc@8.1.0+systemcerts arch=linux-rhel7-ppc64le ^zlib@1.2.11%gcc@8.1.0+optimize+pic+shared arch=linux-rhel7-ppc64le": spec-26.json
 - "libevent@2.1.12%gcc@9.3.0+openssl arch=linux-ubuntu20.04-ppc64le ^openssl@1.1.1k%gcc@9.3.0~docs+systemcerts arch=linux-ubuntu20.04-ppc64le ^zlib@1.2.11%gcc@9.3.0+optimize+pic+shared arch=linux-ubuntu20.04-ppc64le": spec-27.json
 - "libevent@2.1.12%gcc@7.5.0+openssl arch=linux-ubuntu18.04-x86_64 ^openssl@1.1.1j%gcc@7.5.0~docs+systemcerts arch=linux-ubuntu18.04-x86_64 ^zlib@1.2.11%gcc@7.5.0+optimize+pic+shared arch=linux-ubuntu18.04-x86_64": spec-28.json
 - "libevent@2.1.12%gcc@7.5.0+openssl arch=linux-ubuntu18.04-ppc64le ^openssl@1.1.1j%gcc@7.5.0+systemcerts arch=linux-ubuntu18.04-ppc64le ^zlib@1.2.11%gcc@7.5.0+optimize+pic+shared arch=linux-ubuntu18.04-ppc64le": spec-29.json
 - "libevent@2.1.12%gcc@8.3.1+openssl arch=linux-rhel8-ppc64le ^openssl@1.1.1k%gcc@8.3.1~docs+systemcerts arch=linux-rhel8-ppc64le ^zlib@1.2.11%gcc@8.3.1+optimize+pic+shared arch=linux-rhel8-ppc64le": spec-30.json
 - "libevent@2.1.12%gcc@8.3.1+openssl arch=linux-rhel8-x86_64 ^openssl@1.1.1j%gcc@8.3.1+systemcerts arch=linux-rhel8-x86_64 ^zlib@1.2.11%gcc@8.3.1+optimize+pic+shared arch=linux-rhel8-x86_64": spec-31.json
 - "libevent@2.1.12%gcc@8.3.1+openssl arch=linux-rhel8-ppc64le ^openssl@1.1.1i%gcc@8.3.1+systemcerts arch=linux-rhel8-ppc64le ^zlib@1.2.11%gcc@8.3.1+optimize+pic+shared arch=linux-rhel8-ppc64le": spec-32.json
 - "libevent@2.1.12%gcc@10.3.0+openssl arch=linux-ubuntu21.04-x86_64 ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-ubuntu21.04-x86_64 ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-ubuntu21.04-x86_64": spec-33.json
 - "libevent@2.1.12%gcc@7.5.0+openssl arch=linux-ubuntu18.04-ppc64le ^openssl@1.1.1i%gcc@7.5.0+systemcerts arch=linux-ubuntu18.04-ppc64le ^zlib@1.2.11%gcc@7.5.0+optimize+pic+shared arch=linux-ubuntu18.04-ppc64le": spec-34.json
 - "libevent@2.1.12%gcc@9.3.0+openssl arch=linux-ubuntu20.04-ppc64le ^openssl@1.1.1i%gcc@9.3.0+systemcerts arch=linux-ubuntu20.04-ppc64le ^zlib@1.2.11%gcc@9.3.0+optimize+pic+shared arch=linux-ubuntu20.04-ppc64le": spec-35.json
 - "libevent@2.1.12%gcc@9.3.0+openssl arch=linux-rhel7-x86_64 ^openssl@1.1.1k%gcc@9.3.0~docs+systemcerts arch=linux-rhel7-x86_64 ^zlib@1.2.11%gcc@9.3.0+optimize+pic+shared arch=linux-rhel7-x86_64": spec-36.json
 - "libevent@2.1.12%gcc@7.5.0+openssl arch=linux-ubuntu18.04-x86_64 ^openssl@1.1.1i%gcc@7.5.0+systemcerts arch=linux-ubuntu18.04-x86_64 ^zlib@1.2.11%gcc@7.5.0+optimize+pic+shared arch=linux-ubuntu18.04-x86_64": spec-37.json
 - "libevent@2.1.12%gcc@8.1.0+openssl arch=linux-rhel7-ppc64le ^openssl@1.1.1i%gcc@8.1.0+systemcerts arch=linux-rhel7-ppc64le ^zlib@1.2.11%gcc@8.1.0+optimize+pic+shared arch=linux-rhel7-ppc64le": spec-38.json
 - "libevent@2.1.12%gcc@8.4.1+openssl arch=linux-rhel8-x86_64 ^openssl@1.1.1k%gcc@8.4.1~docs+systemcerts arch=linux-rhel8-x86_64 ^zlib@1.2.11%gcc@8.4.1+optimize+pic+shared arch=linux-rhel8-x86_64": spec-39.json
 - "libevent@2.1.12%gcc@9.3.0+openssl arch=linux-ubuntu20.04-x86_64 ^openssl@1.1.1i%gcc@9.3.0+systemcerts arch=linux-ubuntu20.04-x86_64 ^zlib@1.2.11%gcc@9.3.0+optimize+pic+shared arch=linux-ubuntu20.04-x86_64": spec-40.json
 - "libevent@2.1.12%gcc@8.3.1+openssl arch=linux-rhel8-x86_64 ^openssl@1.1.1i%gcc@8.3.1+systemcerts arch=linux-rhel8-x86_64 ^zlib@1.2.11%gcc@8.3.1+optimize+pic+shared arch=linux-rhel8-x86_64": spec-41.json
 - "libevent@2.1.12%gcc@7.3.1+openssl arch=linux-amzn2-x86_64 ^openssl@1.1.1j%gcc@7.3.1~docs+systemcerts arch=linux-amzn2-x86_64 ^zlib@1.2.11%gcc@7.3.1+optimize+pic+shared arch=linux-amzn2-x86_64": spec-42.json
 - "libevent@2.1.12%gcc@7.3.1+openssl arch=linux-amzn2-x86_64 ^openssl@1.1.1k%gcc@7.3.1~docs+systemcerts arch=linux-amzn2-x86_64 ^zlib@1.2.11%gcc@7.3.1+optimize+pic+shared arch=linux-amzn2-x86_64": spec-43.json

---