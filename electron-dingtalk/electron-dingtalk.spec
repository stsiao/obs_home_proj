#
# spec file for package electron-dingtalk
#
# Copyright (c) 2022 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2021-2022 Sigmond Tsiao <gamebus2011@hotmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           electron-dingtalk
Version:        2.1.20
Release:        0
Summary:        Dingtalk desktop version.
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        MIT
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          Productivity/Networking/Talk/Clients
Url:            https://github.com/nashaofu/dingtalk
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       electron-dingtalk = %{version}
Obsoletes:      electron-dingtalk < %{version}

%description
Dingtalk desktop version, based on electron, Windows, Linux, MacOS supported.

%prep
%setup -q

%build

%install
install -d %{buildroot}/opt
install -d %{buildroot}%{_datadir}/applications/
install -d %{buildroot}%{_datadir}/icons/
install -d %{buildroot}%{_datadir}/icons/hicolor/
install -d %{buildroot}%{_datadir}/icons/hicolor/16x16/
install -d %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
install -d %{buildroot}%{_datadir}/icons/hicolor/128x128/
install -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -d %{buildroot}%{_datadir}/icons/hicolor/256x256/
install -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -d %{buildroot}%{_datadir}/icons/hicolor/512x512/
install -d %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/
install -d %{buildroot}%{_bindir}
cp -rf linux-unpacked %{buildroot}/opt/electron-dingtalk
cp -f resources/icons/16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/electron-dingtalk.png
cp -f resources/icons/32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/electron-dingtalk.png
cp -f resources/icons/128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/electron-dingtalk.png
cp -f resources/icons/256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/electron-dingtalk.png
cp -f resources/icons/512x512.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/electron-dingtalk.png
ln -s /opt/electron-dingtalk/dingtalk %{buildroot}%{_bindir}/electron-dingtalk
echo "[Desktop Entry]
Name=钉钉
GenericName=Third party Dingtalk client
Comment=Dingtalk desktop application
Exec=electron-dingtalk %U
Terminal=false
Type=Application
Icon=electron-dingtalk
X-Desktop-File-Install-Version=%{version}
Categories=Network;WebBrowser;" > "%{buildroot}%{_datadir}/applications/electron-dingtalk.desktop"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/opt/electron-dingtalk
%{_bindir}/electron-dingtalk
%{_datadir}/applications/electron-dingtalk.desktop
%{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/16x16
%{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/electron-dingtalk.png
%{_datadir}/icons/hicolor/32x32
%{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/electron-dingtalk.png
%{_datadir}/icons/hicolor/128x128
%{_datadir}/icons/hicolor/128x128/apps
%{_datadir}/icons/hicolor/128x128/apps/electron-dingtalk.png
%{_datadir}/icons/hicolor/256x256
%{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/256x256/apps/electron-dingtalk.png
%{_datadir}/icons/hicolor/512x512
%{_datadir}/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/512x512/apps/electron-dingtalk.png

%changelog

