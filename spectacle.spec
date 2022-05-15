#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : spectacle
Version  : 22.04.1
Release  : 39
URL      : https://download.kde.org/stable/release-service/22.04.1/src/spectacle-22.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.1/src/spectacle-22.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.1/src/spectacle-22.04.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1
Requires: spectacle-bin = %{version}-%{release}
Requires: spectacle-data = %{version}-%{release}
Requires: spectacle-license = %{version}-%{release}
Requires: spectacle-locales = %{version}-%{release}
Requires: spectacle-man = %{version}-%{release}
Requires: spectacle-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kdoctools-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kwayland-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : purpose-dev
BuildRequires : qtx11extras-dev

%description
# Spectacle - The KDE Screenshot Utility
Spectacle is a screenshot taking utility for the KDE desktop. Spectacle
can also be used in non-KDE X11 desktop environments.

%package bin
Summary: bin components for the spectacle package.
Group: Binaries
Requires: spectacle-data = %{version}-%{release}
Requires: spectacle-license = %{version}-%{release}
Requires: spectacle-services = %{version}-%{release}

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
Requires: spectacle-man = %{version}-%{release}

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


%package man
Summary: man components for the spectacle package.
Group: Default

%description man
man components for the spectacle package.


%package services
Summary: services components for the spectacle package.
Group: Systemd services

%description services
services components for the spectacle package.


%prep
%setup -q -n spectacle-22.04.1
cd %{_builddir}/spectacle-22.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652633730
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1652633730
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/spectacle
cp %{_builddir}/spectacle-22.04.1/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/spectacle/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/spectacle-22.04.1/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/spectacle/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe
cp %{_builddir}/spectacle-22.04.1/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/spectacle/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc
cp %{_builddir}/spectacle-22.04.1/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/spectacle/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/spectacle-22.04.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/spectacle/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/spectacle-22.04.1/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/spectacle/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98
cp %{_builddir}/spectacle-22.04.1/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/spectacle/a4c60b3fefda228cd7439d3565df043192fef137
cp %{_builddir}/spectacle-22.04.1/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/spectacle/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
cp %{_builddir}/spectacle-22.04.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/spectacle/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/spectacle-22.04.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/spectacle/7d9831e05094ce723947d729c2a46a09d6e90275
pushd clr-build
%make_install
popd
%find_lang spectacle

%files
%defattr(-,root,root,-)
/usr/lib64/kconf_update_bin/spectacle-migrate-rememberregion
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
/usr/share/kconf_update/50-clipboard_settings_change.py
/usr/share/kconf_update/spectacle_clipboard.upd
/usr/share/kconf_update/spectacle_newConfig.upd
/usr/share/kconf_update/spectacle_rememberregion.upd
/usr/share/kconf_update/spectacle_shortcuts.upd
/usr/share/kglobalaccel/org.kde.spectacle.desktop
/usr/share/knotifications5/spectacle.notifyrc
/usr/share/metainfo/org.kde.spectacle.appdata.xml
/usr/share/qlogging-categories5/spectacle.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/spectacle/Annotate.png
/usr/share/doc/HTML/ca/spectacle/ApplicationPreferences.png
/usr/share/doc/HTML/ca/spectacle/MainWindow.png
/usr/share/doc/HTML/ca/spectacle/SaveOptions.png
/usr/share/doc/HTML/ca/spectacle/index.cache.bz2
/usr/share/doc/HTML/ca/spectacle/index.docbook
/usr/share/doc/HTML/de/spectacle/index.cache.bz2
/usr/share/doc/HTML/de/spectacle/index.docbook
/usr/share/doc/HTML/en/spectacle/Annotate.png
/usr/share/doc/HTML/en/spectacle/ApplicationPreferences.png
/usr/share/doc/HTML/en/spectacle/MainWindow.png
/usr/share/doc/HTML/en/spectacle/SaveOptions.png
/usr/share/doc/HTML/en/spectacle/index.cache.bz2
/usr/share/doc/HTML/en/spectacle/index.docbook
/usr/share/doc/HTML/es/spectacle/index.cache.bz2
/usr/share/doc/HTML/es/spectacle/index.docbook
/usr/share/doc/HTML/it/spectacle/ApplicationPreferences.png
/usr/share/doc/HTML/it/spectacle/MainWindow.png
/usr/share/doc/HTML/it/spectacle/SaveOptions.png
/usr/share/doc/HTML/it/spectacle/index.cache.bz2
/usr/share/doc/HTML/it/spectacle/index.docbook
/usr/share/doc/HTML/nl/spectacle/index.cache.bz2
/usr/share/doc/HTML/nl/spectacle/index.docbook
/usr/share/doc/HTML/pt/spectacle/index.cache.bz2
/usr/share/doc/HTML/pt/spectacle/index.docbook
/usr/share/doc/HTML/pt_BR/spectacle/index.cache.bz2
/usr/share/doc/HTML/pt_BR/spectacle/index.docbook
/usr/share/doc/HTML/ru/spectacle/index.cache.bz2
/usr/share/doc/HTML/ru/spectacle/index.docbook
/usr/share/doc/HTML/sv/spectacle/index.cache.bz2
/usr/share/doc/HTML/sv/spectacle/index.docbook
/usr/share/doc/HTML/uk/spectacle/Annotate.png
/usr/share/doc/HTML/uk/spectacle/ApplicationPreferences.png
/usr/share/doc/HTML/uk/spectacle/MainWindow.png
/usr/share/doc/HTML/uk/spectacle/SaveOptions.png
/usr/share/doc/HTML/uk/spectacle/index.cache.bz2
/usr/share/doc/HTML/uk/spectacle/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/spectacle/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/spectacle/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/spectacle/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98
/usr/share/package-licenses/spectacle/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/spectacle/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/spectacle/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/spectacle/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc
/usr/share/package-licenses/spectacle/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/spectacle.1
/usr/share/man/de/man1/spectacle.1
/usr/share/man/es/man1/spectacle.1
/usr/share/man/it/man1/spectacle.1
/usr/share/man/man1/spectacle.1
/usr/share/man/nl/man1/spectacle.1
/usr/share/man/sv/man1/spectacle.1
/usr/share/man/uk/man1/spectacle.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/app-org.kde.spectacle.service

%files locales -f spectacle.lang
%defattr(-,root,root,-)

