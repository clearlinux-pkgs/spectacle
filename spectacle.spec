#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : spectacle
Version  : 19.08.2
Release  : 12
URL      : https://download.kde.org/stable/applications/19.08.2/src/spectacle-19.08.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.2/src/spectacle-19.08.2.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.2/src/spectacle-19.08.2.tar.xz.sig
Summary  : KDE screenshot capture utility
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: spectacle-bin = %{version}-%{release}
Requires: spectacle-data = %{version}-%{release}
Requires: spectacle-license = %{version}-%{release}
Requires: spectacle-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kwayland-dev
BuildRequires : libkipi-dev
BuildRequires : purpose-dev

%description
Spectacle - The KDE Screenshot Utility
Spectacle is screenshot taking utility for the KDE desktop. Spectacle
can also be used in non-KDE X11 desktop environments.

%package bin
Summary: bin components for the spectacle package.
Group: Binaries
Requires: spectacle-data = %{version}-%{release}
Requires: spectacle-license = %{version}-%{release}

%description bin
bin components for the spectacle package.


%package data
Summary: data components for the spectacle package.
Group: Data

%description data
data components for the spectacle package.


%package doc
Summary: doc components for the spectacle package.
Group: Documentation

%description doc
doc components for the spectacle package.


%package license
Summary: license components for the spectacle package.
Group: Default

%description license
license components for the spectacle package.


%package locales
Summary: locales components for the spectacle package.
Group: Default

%description locales
locales components for the spectacle package.


%prep
%setup -q -n spectacle-19.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570784953
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570784953
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/spectacle
cp COPYING %{buildroot}/usr/share/package-licenses/spectacle/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/spectacle/COPYING.DOC
cp COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/spectacle/COPYING.LGPL-2
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/spectacle/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang spectacle

%files
%defattr(-,root,root,-)
/usr/lib64/kconf_update_bin/spectacle-migrate-shortcuts

%files bin
%defattr(-,root,root,-)
/usr/bin/spectacle

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.spectacle.desktop
/usr/share/dbus-1/interfaces/org.kde.Spectacle.xml
/usr/share/dbus-1/services/org.kde.Spectacle.service
/usr/share/icons/hicolor/16x16/apps/spectacle.png
/usr/share/icons/hicolor/22x22/apps/spectacle.png
/usr/share/icons/hicolor/32x32/apps/spectacle.png
/usr/share/icons/hicolor/48x48/apps/spectacle.png
/usr/share/icons/hicolor/scalable/apps/spectacle.svgz
/usr/share/kconf_update/spectacle_shortcuts.upd
/usr/share/kglobalaccel/org.kde.spectacle.desktop
/usr/share/knotifications5/spectacle.notifyrc
/usr/share/metainfo/org.kde.spectacle.appdata.xml
/usr/share/qlogging-categories5/spectacle.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/spectacle/ApplicationPreferences.png
/usr/share/doc/HTML/ca/spectacle/MainWindow.png
/usr/share/doc/HTML/ca/spectacle/SaveOptions.png
/usr/share/doc/HTML/ca/spectacle/index.cache.bz2
/usr/share/doc/HTML/ca/spectacle/index.docbook
/usr/share/doc/HTML/de/spectacle/index.cache.bz2
/usr/share/doc/HTML/de/spectacle/index.docbook
/usr/share/doc/HTML/en/spectacle/ApplicationPreferences.png
/usr/share/doc/HTML/en/spectacle/MainWindow.png
/usr/share/doc/HTML/en/spectacle/SaveOptions.png
/usr/share/doc/HTML/en/spectacle/index.cache.bz2
/usr/share/doc/HTML/en/spectacle/index.docbook
/usr/share/doc/HTML/es/spectacle/index.cache.bz2
/usr/share/doc/HTML/es/spectacle/index.docbook
/usr/share/doc/HTML/it/spectacle/index.cache.bz2
/usr/share/doc/HTML/it/spectacle/index.docbook
/usr/share/doc/HTML/nl/spectacle/index.cache.bz2
/usr/share/doc/HTML/nl/spectacle/index.docbook
/usr/share/doc/HTML/pt/spectacle/index.cache.bz2
/usr/share/doc/HTML/pt/spectacle/index.docbook
/usr/share/doc/HTML/pt_BR/spectacle/index.cache.bz2
/usr/share/doc/HTML/pt_BR/spectacle/index.docbook
/usr/share/doc/HTML/sv/spectacle/index.cache.bz2
/usr/share/doc/HTML/sv/spectacle/index.docbook
/usr/share/doc/HTML/uk/spectacle/ApplicationPreferences.png
/usr/share/doc/HTML/uk/spectacle/MainWindow.png
/usr/share/doc/HTML/uk/spectacle/SaveOptions.png
/usr/share/doc/HTML/uk/spectacle/index.cache.bz2
/usr/share/doc/HTML/uk/spectacle/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/spectacle/COPYING
/usr/share/package-licenses/spectacle/COPYING.DOC
/usr/share/package-licenses/spectacle/COPYING.LGPL-2
/usr/share/package-licenses/spectacle/COPYING.LIB

%files locales -f spectacle.lang
%defattr(-,root,root,-)

