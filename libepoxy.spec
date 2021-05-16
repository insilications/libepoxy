#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libepoxy
Version  : 1.5.7
Release  : 41
URL      : file:///aot/build/clearlinux/packages/libepoxy/libepoxy-v1.5.7.tar.gz
Source0  : file:///aot/build/clearlinux/packages/libepoxy/libepoxy-v1.5.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: libepoxy-lib = %{version}-%{release}
BuildRequires : ImageMagick-dev
BuildRequires : Sphinx
BuildRequires : Z3-dev
BuildRequires : Z3-staticdev
BuildRequires : acl
BuildRequires : acl-dev
BuildRequires : acl-staticdev
BuildRequires : alsa-firmware
BuildRequires : alsa-lib-dev
BuildRequires : alsa-lib-lib
BuildRequires : alsa-plugins
BuildRequires : alsa-plugins-lib
BuildRequires : alsa-tools
BuildRequires : alsa-ucm-conf
BuildRequires : alsa-utils
BuildRequires : asciidoctor
BuildRequires : binutils
BuildRequires : binutils-dev
BuildRequires : binutils-staticdev
BuildRequires : brotli
BuildRequires : brotli-dev
BuildRequires : brotli-staticdev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : buildreq-qmake
BuildRequires : bzip2
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : cairo
BuildRequires : cairo-dev
BuildRequires : cairo-lib
BuildRequires : ccache
BuildRequires : clazy
BuildRequires : cmake
BuildRequires : cppcheck
BuildRequires : cuda
BuildRequires : cuda-dev
BuildRequires : cuda-staticdev
BuildRequires : curl-dev
BuildRequires : dbus
BuildRequires : dbus-broker
BuildRequires : dbus-dev
BuildRequires : dbus-glib
BuildRequires : dbus-glib-dev
BuildRequires : dbus-python
BuildRequires : doxygen
BuildRequires : e2fsprogs-dev
BuildRequires : elfutils-dev
BuildRequires : evtest
BuildRequires : expat-dev
BuildRequires : expat-dev32
BuildRequires : expat-staticdev
BuildRequires : findutils
BuildRequires : fontconfig-data
BuildRequires : fontconfig-dev
BuildRequires : fontconfig-lib
BuildRequires : freetype-dev
BuildRequires : freetype-lib
BuildRequires : fribidi-dev
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb
BuildRequires : gdb-dev
BuildRequires : gettext
BuildRequires : glib
BuildRequires : glib-bin
BuildRequires : glib-data
BuildRequires : glib-dev
BuildRequires : glib-dev32
BuildRequires : glib-lib
BuildRequires : glibc
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-staticdev
BuildRequires : glu
BuildRequires : glu-dev
BuildRequires : gmp
BuildRequires : gmp-dev
BuildRequires : gmp-staticdev
BuildRequires : gnutls
BuildRequires : gnutls-dev
BuildRequires : googletest
BuildRequires : googletest-dev
BuildRequires : graphite
BuildRequires : graphite-dev
BuildRequires : gsm-dev
BuildRequires : gtk+-data
BuildRequires : gtk+-lib
BuildRequires : gtk3-lib
BuildRequires : harfbuzz-dev
BuildRequires : harfbuzz-lib
BuildRequires : icu4c-lib
BuildRequires : jack2
BuildRequires : jack2-dev
BuildRequires : jsoncpp
BuildRequires : jsoncpp-dev
BuildRequires : jsoncpp-lib
BuildRequires : jsoncpp-staticdev
BuildRequires : keyutils
BuildRequires : keyutils-dev
BuildRequires : krb5
BuildRequires : krb5-dev
BuildRequires : lcms2-dev
BuildRequires : lcms2-staticdev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-data
BuildRequires : libX11-dev
BuildRequires : libX11-lib
BuildRequires : libXScrnSaver
BuildRequires : libXScrnSaver-dev
BuildRequires : libXScrnSaver-lib
BuildRequires : libXau-dev
BuildRequires : libXau-lib
BuildRequires : libXcursor-dev
BuildRequires : libXcursor-lib
BuildRequires : libXdamage-dev
BuildRequires : libXdamage-lib
BuildRequires : libXdmcp-dev
BuildRequires : libXdmcp-lib
BuildRequires : libXext-dev
BuildRequires : libXext-lib
BuildRequires : libXfont2-dev
BuildRequires : libXft-dev
BuildRequires : libXft-lib
BuildRequires : libXi-dev
BuildRequires : libXi-lib
BuildRequires : libXrender-dev
BuildRequires : libXrender-lib
BuildRequires : libXtst-dev
BuildRequires : libXtst-lib
BuildRequires : libXxf86vm-dev
BuildRequires : libXxf86vm-dev32
BuildRequires : libXxf86vm-lib
BuildRequires : libarchive
BuildRequires : libarchive-dev
BuildRequires : libarchive-staticdev
BuildRequires : libatomic_ops-dev
BuildRequires : libatomic_ops-staticdev
BuildRequires : libcap
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libconfig-dev
BuildRequires : libdrm
BuildRequires : libdrm-dev
BuildRequires : libdrm-lib
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libepoxy
BuildRequires : libepoxy-dev
BuildRequires : libffi
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libgcrypt
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error
BuildRequires : libgpg-error-dev
BuildRequires : libidn2
BuildRequires : libidn2-dev
BuildRequires : libidn2-staticdev
BuildRequires : libinput-data
BuildRequires : libinput-dev
BuildRequires : libinput-lib
BuildRequires : libinput-libexec
BuildRequires : libjpeg-turbo-dev
BuildRequires : libogg
BuildRequires : libogg-dev
BuildRequires : libpciaccess
BuildRequires : libpciaccess-dev
BuildRequires : libplacebo
BuildRequires : libplacebo-dev
BuildRequires : libpng-dev
BuildRequires : libpng-lib
BuildRequires : libsamplerate-dev
BuildRequires : libsamplerate-dev32
BuildRequires : libsamplerate-staticdev
BuildRequires : libsamplerate-staticdev32
BuildRequires : libstdc++
BuildRequires : libstdc++-dev
BuildRequires : libtasn1-dev
BuildRequires : libunistring-dev
BuildRequires : libunistring-staticdev
BuildRequires : libunwind
BuildRequires : libunwind-dev
BuildRequires : libunwind-dev32
BuildRequires : libusb
BuildRequires : libusb-dev
BuildRequires : libusb-dev32
BuildRequires : libva
BuildRequires : libva-dev
BuildRequires : libva-lib
BuildRequires : libvdpau
BuildRequires : libvdpau-dev
BuildRequires : libvorbis
BuildRequires : libvorbis-dev
BuildRequires : libwebp-dev
BuildRequires : libxcb-dev
BuildRequires : libxcb-lib
BuildRequires : libxkbcommon
BuildRequires : libxkbcommon-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt-bin
BuildRequires : libxvid-staticdev
BuildRequires : libzimg-dev
BuildRequires : libzimg-staticdev
BuildRequires : lz4
BuildRequires : lz4-dev
BuildRequires : lz4-staticdev
BuildRequires : lzo
BuildRequires : lzo-dev
BuildRequires : lzo-staticdev
BuildRequires : md4c
BuildRequires : md4c-dev
BuildRequires : md4c-staticdev
BuildRequires : mediasdk-dev
BuildRequires : mesa
BuildRequires : mesa-demos
BuildRequires : mesa-dev
BuildRequires : mesa-lib
BuildRequires : mm-common-dev
BuildRequires : nasm
BuildRequires : nasm-bin
BuildRequires : ncurses-dev
BuildRequires : nettle
BuildRequires : nettle-dev
BuildRequires : ninja
BuildRequires : not-ffmpeg
BuildRequires : not-ffmpeg-dev
BuildRequires : numlockx
BuildRequires : nvidia
BuildRequires : nvidia-dev
BuildRequires : nvidia-lib
BuildRequires : opencl-headers
BuildRequires : opencl-headers-dev
BuildRequires : openjpeg-dev
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : openssl-lib
BuildRequires : openssl-staticdev
BuildRequires : orc-dev
BuildRequires : orc-staticdev
BuildRequires : p11-kit
BuildRequires : p11-kit-dev
BuildRequires : pacrunner
BuildRequires : pacrunner-dev
BuildRequires : pango-lib
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : perl-Config-General
BuildRequires : perl-Config-Tiny
BuildRequires : perl-Crypt-SSLeay
BuildRequires : perl-DBI
BuildRequires : perl-DateTime-TimeZone
BuildRequires : perl-Encode-Locale
BuildRequires : perl-Error
BuildRequires : perl-File-Listing
BuildRequires : perl-HTML-Parser
BuildRequires : perl-HTML-Tagset
BuildRequires : perl-HTTP-Cookies
BuildRequires : perl-HTTP-Date
BuildRequires : perl-HTTP-Message
BuildRequires : perl-HTTP-Negotiate
BuildRequires : perl-IO-HTML
BuildRequires : perl-LWP-MediaTypes
BuildRequires : perl-LWP-Protocol-https
BuildRequires : perl-Params-Validate
BuildRequires : perl-Test-Simple
BuildRequires : perl-Try-Tiny
BuildRequires : perl-URI
BuildRequires : perl-XML-NamespaceSupport
BuildRequires : perl-XML-Parser
BuildRequires : perl-libwww-perl
BuildRequires : perl-man
BuildRequires : pixman
BuildRequires : pixman-dev
BuildRequires : pixman-lib
BuildRequires : pixman-staticdev
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(32egl)
BuildRequires : pkgconfig(32glesv1_cm)
BuildRequires : pkgconfig(32glesv2)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(alsa-topology)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dri)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gdm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glesv1_cm)
BuildRequires : pkgconfig(glesv2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(glu)
BuildRequires : pkgconfig(gmock)
BuildRequires : pkgconfig(gmock_main)
BuildRequires : pkgconfig(gtest)
BuildRequires : pkgconfig(gtest_main)
BuildRequires : pkgconfig(ibus-1.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(libunwind-coredump)
BuildRequires : pkgconfig(libunwind-generic)
BuildRequires : pkgconfig(libunwind-ptrace)
BuildRequires : pkgconfig(libunwind-setjmp)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(osmesa)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(vulkan)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xatracker)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xmu)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xpm)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xscrnsaver)
BuildRequires : pkgconfig(xt)
BuildRequires : pkgconfig(zlib)
BuildRequires : pulseaudio
BuildRequires : pulseaudio-dev
BuildRequires : python3
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : setxkbmap
BuildRequires : shaderc
BuildRequires : shaderc-dev
BuildRequires : shaderc-staticdev
BuildRequires : shared-mime-info
BuildRequires : snappy-dev
BuildRequires : solid-dev
BuildRequires : sonnet-dev
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : texinfo
BuildRequires : util-linux
BuildRequires : util-linux-dev
BuildRequires : util-linux-staticdev
BuildRequires : valgrind
BuildRequires : valgrind-dev
BuildRequires : wayland
BuildRequires : wayland-dev
BuildRequires : weston
BuildRequires : wmctrl
BuildRequires : xauth
BuildRequires : xcb-proto
BuildRequires : xcb-proto-dev
BuildRequires : xcb-util-cursor-dev
BuildRequires : xcb-util-dev
BuildRequires : xcb-util-image-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
BuildRequires : xcb-util-xrm-dev
BuildRequires : xclip
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-gtk
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-user-dirs
BuildRequires : xdg-user-dirs-gtk
BuildRequires : xdg-utils
BuildRequires : xdotool
BuildRequires : xdpyinfo
BuildRequires : xf86-input-libinput
BuildRequires : xf86-video-amdgpu
BuildRequires : xf86-video-ati
BuildRequires : xf86-video-fbdev
BuildRequires : xf86-video-nouveau
BuildRequires : xf86-video-qxl
BuildRequires : xf86-video-vboxvideo
BuildRequires : xf86-video-vesa
BuildRequires : xf86-video-vmware
BuildRequires : xfontsel
BuildRequires : xhost
BuildRequires : xinit
BuildRequires : xinput
BuildRequires : xkbcomp
BuildRequires : xkeyboard-config
BuildRequires : xkill
BuildRequires : xmodmap
BuildRequires : xorg-server
BuildRequires : xorg-server-dev
BuildRequires : xorgproto
BuildRequires : xorgproto-dev
BuildRequires : xprop
BuildRequires : xrandr
BuildRequires : xrdb
BuildRequires : xrdp
BuildRequires : xrestop
BuildRequires : xscreensaver
BuildRequires : xsel
BuildRequires : xset
BuildRequires : xsetroot
BuildRequires : xvfb-run
BuildRequires : xwd
BuildRequires : xwininfo
BuildRequires : xz
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
![Ubuntu](https://github.com/anholt/libepoxy/workflows/Ubuntu/badge.svg)
![macOS](https://github.com/anholt/libepoxy/workflows/macOS/badge.svg)
![MSVC Build](https://github.com/anholt/libepoxy/workflows/MSVC%20Build/badge.svg)
![MSYS2 Build](https://github.com/anholt/libepoxy/workflows/MSYS2%20Build/badge.svg)
[![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

%package dev
Summary: dev components for the libepoxy package.
Group: Development
Requires: libepoxy-lib = %{version}-%{release}
Provides: libepoxy-devel = %{version}-%{release}
Requires: libepoxy = %{version}-%{release}

%description dev
dev components for the libepoxy package.


%package dev32
Summary: dev32 components for the libepoxy package.
Group: Default
Requires: libepoxy-lib32 = %{version}-%{release}
Requires: libepoxy-dev = %{version}-%{release}

%description dev32
dev32 components for the libepoxy package.


%package lib
Summary: lib components for the libepoxy package.
Group: Libraries

%description lib
lib components for the libepoxy package.


%package lib32
Summary: lib32 components for the libepoxy package.
Group: Default

%description lib32
lib32 components for the libepoxy package.


%package staticdev
Summary: staticdev components for the libepoxy package.
Group: Default
Requires: libepoxy-dev = %{version}-%{release}

%description staticdev
staticdev components for the libepoxy package.


%package staticdev32
Summary: staticdev32 components for the libepoxy package.
Group: Default
Requires: libepoxy-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the libepoxy package.


%prep
%setup -q -n libepoxy
cd %{_builddir}/libepoxy
pushd ..
cp -a libepoxy build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621175559
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FCFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export LDFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
meson --libdir=lib64 --prefix=/usr --buildtype=release -Ddefault_library=both  -Ddefault_library=both \
-Dglx=yes \
-Degl=no \
-Dx11=true \
-Dtests=true \
-Ddocs=false builddir
ninja --verbose %{?_smp_mflags} -v -C builddir

export DISPLAY=:0
#export __GL_ALLOW_UNOFFICIAL_PROTOCOL=1
export __GL_SYNC_TO_VBLANK=0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
export LD_LIBRARY_PATH="/usr/cuda/lib64:/usr/cuda/targets/x86_64-linux/lib:/usr/nvidia/lib64:/usr/nvidia/lib:/usr/nvidia/lib/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
export LIBRARY_PATH="/usr/cuda/lib64:/usr/cuda/targets/x86_64-linux/lib:/usr/nvidia/lib64:/usr/nvidia/lib:/usr/nvidia/lib/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:../"
export PATH="/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export $(dbus-launch)
meson test --verbose --num-processes 16 -C builddir || :
find builddir/ -type f,l -not -name '*.gcno' -not -name 'statuspgo*' -delete -print
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
meson --libdir=lib64 --prefix=/usr --buildtype=release -Ddefault_library=both  -Ddefault_library=both \
-Dglx=yes \
-Degl=no \
-Dx11=true \
-Dtests=false \
-Ddocs=false builddir
ninja --verbose %{?_smp_mflags} -v -C builddir
pushd ../build32/
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=release -Ddefault_library=both  -Ddefault_library=both \
-Dglx=yes \
-Dx11=true \
-Dtests=false \
-Ddocs=false builddir
ninja --verbose %{?_smp_mflags} -v -C builddir
popd

%install
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/epoxy/common.h
/usr/include/epoxy/egl.h
/usr/include/epoxy/egl_generated.h
/usr/include/epoxy/gl.h
/usr/include/epoxy/gl_generated.h
/usr/include/epoxy/glx.h
/usr/include/epoxy/glx_generated.h
/usr/lib64/libepoxy.so
/usr/lib64/pkgconfig/epoxy.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libepoxy.so
/usr/lib32/pkgconfig/32epoxy.pc
/usr/lib32/pkgconfig/epoxy.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libepoxy.so.0
/usr/lib64/libepoxy.so.0.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libepoxy.so.0
/usr/lib32/libepoxy.so.0.0.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libepoxy.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libepoxy.a
