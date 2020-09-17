#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libfrei0r
Version  : 1.7
Release  : 4
URL      : file:///insilications/build/clearlinux/packages/libfrei0r/libfrei0r-v1.7.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/libfrei0r/libfrei0r-v1.7.tar.gz
Summary  : minimalistic plugin API for video effects
Group    : Development/Tools
License  : GPL-2.0
Requires: libfrei0r-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cairo
BuildRequires : cairo-dev
BuildRequires : doxygen
BuildRequires : findutils
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-egl)
BuildRequires : pkgconfig(cairo-fc)
BuildRequires : pkgconfig(cairo-ft)
BuildRequires : pkgconfig(cairo-gl)
BuildRequires : pkgconfig(cairo-glx)
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(cairo-pdf)
BuildRequires : pkgconfig(cairo-png)
BuildRequires : pkgconfig(cairo-ps)
BuildRequires : pkgconfig(cairo-script)
BuildRequires : pkgconfig(cairo-svg)
BuildRequires : pkgconfig(cairo-xcb)
BuildRequires : pkgconfig(cairo-xcb-shm)
BuildRequires : pkgconfig(cairo-xlib)
BuildRequires : pkgconfig(cairo-xlib-xcb)
BuildRequires : pkgconfig(cairo-xlib-xrender)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
select0r
This plugin selects a range of colors, and creates a corresponding
alpha channel. It is cascadable, allowing construction of complex
color selection subspaces.

%package dev
Summary: dev components for the libfrei0r package.
Group: Development
Requires: libfrei0r-lib = %{version}-%{release}
Provides: libfrei0r-devel = %{version}-%{release}
Requires: libfrei0r = %{version}-%{release}

%description dev
dev components for the libfrei0r package.


%package doc
Summary: doc components for the libfrei0r package.
Group: Documentation

%description doc
doc components for the libfrei0r package.


%package lib
Summary: lib components for the libfrei0r package.
Group: Libraries

%description lib
lib components for the libfrei0r package.


%prep
%setup -q -n libfrei0r
cd %{_builddir}/libfrei0r

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600336107
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
# -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fPIC"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags1 end
##
%define _lto_cflags 1
##
%autogen  --enable-shared --enable-cpuflags --enable-static
make  %{?_smp_mflags}  V=1 VERBOSE=1


%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1600336107
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/frei0r.h
/usr/lib64/pkgconfig/frei0r.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/frei0r-plugins/AUTHORS
/usr/share/doc/frei0r-plugins/ChangeLog
/usr/share/doc/frei0r-plugins/README.md
/usr/share/doc/frei0r-plugins/TODO

%files lib
%defattr(-,root,root,-)
/usr/lib64/frei0r-1/3dflippo.so
/usr/lib64/frei0r-1/B.so
/usr/lib64/frei0r-1/G.so
/usr/lib64/frei0r-1/IIRblur.so
/usr/lib64/frei0r-1/R.so
/usr/lib64/frei0r-1/RGB.so
/usr/lib64/frei0r-1/addition.so
/usr/lib64/frei0r-1/addition_alpha.so
/usr/lib64/frei0r-1/aech0r.so
/usr/lib64/frei0r-1/alpha0ps.so
/usr/lib64/frei0r-1/alphaatop.so
/usr/lib64/frei0r-1/alphagrad.so
/usr/lib64/frei0r-1/alphain.so
/usr/lib64/frei0r-1/alphainjection.so
/usr/lib64/frei0r-1/alphaout.so
/usr/lib64/frei0r-1/alphaover.so
/usr/lib64/frei0r-1/alphaspot.so
/usr/lib64/frei0r-1/alphaxor.so
/usr/lib64/frei0r-1/balanc0r.so
/usr/lib64/frei0r-1/baltan.so
/usr/lib64/frei0r-1/bgsubtract0r.so
/usr/lib64/frei0r-1/blend.so
/usr/lib64/frei0r-1/bluescreen0r.so
/usr/lib64/frei0r-1/brightness.so
/usr/lib64/frei0r-1/burn.so
/usr/lib64/frei0r-1/bw0r.so
/usr/lib64/frei0r-1/c0rners.so
/usr/lib64/frei0r-1/cairoaffineblend.so
/usr/lib64/frei0r-1/cairoblend.so
/usr/lib64/frei0r-1/cairogradient.so
/usr/lib64/frei0r-1/cairoimagegrid.so
/usr/lib64/frei0r-1/cartoon.so
/usr/lib64/frei0r-1/cluster.so
/usr/lib64/frei0r-1/colgate.so
/usr/lib64/frei0r-1/color_only.so
/usr/lib64/frei0r-1/coloradj_RGB.so
/usr/lib64/frei0r-1/colordistance.so
/usr/lib64/frei0r-1/colorhalftone.so
/usr/lib64/frei0r-1/colorize.so
/usr/lib64/frei0r-1/colortap.so
/usr/lib64/frei0r-1/composition.so
/usr/lib64/frei0r-1/contrast0r.so
/usr/lib64/frei0r-1/curves.so
/usr/lib64/frei0r-1/d90stairsteppingfix.so
/usr/lib64/frei0r-1/darken.so
/usr/lib64/frei0r-1/defish0r.so
/usr/lib64/frei0r-1/delay0r.so
/usr/lib64/frei0r-1/delaygrab.so
/usr/lib64/frei0r-1/difference.so
/usr/lib64/frei0r-1/distort0r.so
/usr/lib64/frei0r-1/dither.so
/usr/lib64/frei0r-1/divide.so
/usr/lib64/frei0r-1/dodge.so
/usr/lib64/frei0r-1/edgeglow.so
/usr/lib64/frei0r-1/elastic_scale.so
/usr/lib64/frei0r-1/emboss.so
/usr/lib64/frei0r-1/equaliz0r.so
/usr/lib64/frei0r-1/flippo.so
/usr/lib64/frei0r-1/gamma.so
/usr/lib64/frei0r-1/glitch0r.so
/usr/lib64/frei0r-1/glow.so
/usr/lib64/frei0r-1/grain_extract.so
/usr/lib64/frei0r-1/grain_merge.so
/usr/lib64/frei0r-1/hardlight.so
/usr/lib64/frei0r-1/hqdn3d.so
/usr/lib64/frei0r-1/hue.so
/usr/lib64/frei0r-1/hueshift0r.so
/usr/lib64/frei0r-1/invert0r.so
/usr/lib64/frei0r-1/ising0r.so
/usr/lib64/frei0r-1/keyspillm0pup.so
/usr/lib64/frei0r-1/lenscorrection.so
/usr/lib64/frei0r-1/letterb0xed.so
/usr/lib64/frei0r-1/levels.so
/usr/lib64/frei0r-1/lighten.so
/usr/lib64/frei0r-1/lightgraffiti.so
/usr/lib64/frei0r-1/lissajous0r.so
/usr/lib64/frei0r-1/luminance.so
/usr/lib64/frei0r-1/mask0mate.so
/usr/lib64/frei0r-1/medians.so
/usr/lib64/frei0r-1/multiply.so
/usr/lib64/frei0r-1/ndvi.so
/usr/lib64/frei0r-1/nervous.so
/usr/lib64/frei0r-1/nois0r.so
/usr/lib64/frei0r-1/normaliz0r.so
/usr/lib64/frei0r-1/nosync0r.so
/usr/lib64/frei0r-1/onecol0r.so
/usr/lib64/frei0r-1/overlay.so
/usr/lib64/frei0r-1/partik0l.so
/usr/lib64/frei0r-1/perspective.so
/usr/lib64/frei0r-1/pixeliz0r.so
/usr/lib64/frei0r-1/plasma.so
/usr/lib64/frei0r-1/posterize.so
/usr/lib64/frei0r-1/pr0be.so
/usr/lib64/frei0r-1/pr0file.so
/usr/lib64/frei0r-1/premultiply.so
/usr/lib64/frei0r-1/primaries.so
/usr/lib64/frei0r-1/rgbnoise.so
/usr/lib64/frei0r-1/rgbsplit0r.so
/usr/lib64/frei0r-1/saturat0r.so
/usr/lib64/frei0r-1/saturation.so
/usr/lib64/frei0r-1/scanline0r.so
/usr/lib64/frei0r-1/screen.so
/usr/lib64/frei0r-1/select0r.so
/usr/lib64/frei0r-1/sharpness.so
/usr/lib64/frei0r-1/sigmoidaltransfer.so
/usr/lib64/frei0r-1/sobel.so
/usr/lib64/frei0r-1/softglow.so
/usr/lib64/frei0r-1/softlight.so
/usr/lib64/frei0r-1/sopsat.so
/usr/lib64/frei0r-1/spillsupress.so
/usr/lib64/frei0r-1/squareblur.so
/usr/lib64/frei0r-1/subtract.so
/usr/lib64/frei0r-1/tehroxx0r.so
/usr/lib64/frei0r-1/test_pat_B.so
/usr/lib64/frei0r-1/test_pat_C.so
/usr/lib64/frei0r-1/test_pat_G.so
/usr/lib64/frei0r-1/test_pat_I.so
/usr/lib64/frei0r-1/test_pat_L.so
/usr/lib64/frei0r-1/test_pat_R.so
/usr/lib64/frei0r-1/three_point_balance.so
/usr/lib64/frei0r-1/threelay0r.so
/usr/lib64/frei0r-1/threshold0r.so
/usr/lib64/frei0r-1/timeout.so
/usr/lib64/frei0r-1/tint0r.so
/usr/lib64/frei0r-1/transparency.so
/usr/lib64/frei0r-1/twolay0r.so
/usr/lib64/frei0r-1/uvmap.so
/usr/lib64/frei0r-1/value.so
/usr/lib64/frei0r-1/vertigo.so
/usr/lib64/frei0r-1/vignette.so
/usr/lib64/frei0r-1/xfade0r.so
