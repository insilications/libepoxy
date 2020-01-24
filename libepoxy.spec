#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libepoxy
Version  : 1.5.4
Release  : 34
URL      : https://github.com/anholt/libepoxy/releases/download/1.5.4/libepoxy-1.5.4.tar.xz
Source0  : https://github.com/anholt/libepoxy/releases/download/1.5.4/libepoxy-1.5.4.tar.xz
Summary  : Library handling OpenGL function pointer management
Group    : Development/Tools
License  : MIT
Requires: libepoxy-lib = %{version}-%{release}
Requires: libepoxy-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32egl)
BuildRequires : pkgconfig(32gl)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : python3-dev

%description
[![Build Status](https://travis-ci.org/anholt/libepoxy.svg?branch=master)](https://travis-ci.org/anholt/libepoxy)
[![Build status](https://ci.appveyor.com/api/projects/status/xv6y5jurt5v5ngjx/branch/master?svg=true)](https://ci.appveyor.com/project/ebassi/libepoxy/branch/master)

%package dev
Summary: dev components for the libepoxy package.
Group: Development
Requires: libepoxy-lib = %{version}-%{release}
Provides: libepoxy-devel = %{version}-%{release}
Requires: libepoxy = %{version}-%{release}
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
Requires: libepoxy-license = %{version}-%{release}

%description lib
lib components for the libepoxy package.


%package lib32
Summary: lib32 components for the libepoxy package.
Group: Default
Requires: libepoxy-license = %{version}-%{release}

%description lib32
lib32 components for the libepoxy package.


%package license
Summary: license components for the libepoxy package.
Group: Default

%description license
license components for the libepoxy package.


%package staticdev
Summary: staticdev components for the libepoxy package.
Group: Default
Requires: libepoxy-dev = %{version}-%{release}
Requires: libepoxy-dev = %{version}-%{release}

%description staticdev
staticdev components for the libepoxy package.


%package staticdev32
Summary: staticdev32 components for the libepoxy package.
Group: Default
Requires: libepoxy-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the libepoxy package.


%prep
%setup -q -n libepoxy-1.5.4
cd %{_builddir}/libepoxy-1.5.4
pushd ..
cp -a libepoxy-1.5.4 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579876453
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%autogen  --enable-static --enable-glx=yes
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen  --enable-static --enable-glx=yes  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1579876453
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libepoxy
cp %{_builddir}/libepoxy-1.5.4/COPYING %{buildroot}/usr/share/package-licenses/libepoxy/00f34512740377ad1f155eaa15936e472661c5e3
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libepoxy/00f34512740377ad1f155eaa15936e472661c5e3

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libepoxy.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libepoxy.a
