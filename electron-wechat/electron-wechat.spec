#
# spec file for package electron-wechat
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2021 Sigmond Tsiao <gamebus2011@hotmail.com>
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


Name:           electron-wechat
Version:        0.1.1 
Release:        0
Summary:        The best Wechat Client on Linux/MacOS
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        MIT
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          Productivity/Networking/Talk/Clients
Url:            https://github.com/robbinhan/electron-wechat
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       electron-wechat = %{version}
Obsoletes:      electron-wechat < %{version}

%description
The best Wechat Client on Linux/MacOS

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
cp -rf linux-unpacked %{buildroot}/opt/electron-wechat
cp -f build/icons/16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/electron-wechat.png
cp -f build/icons/32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/electron-wechat.png
cp -f build/icons/128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/electron-wechat.png
cp -f build/icons/256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/electron-wechat.png
cp -f build/icons/512x512.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/electron-wechat.png
ln -s /opt/electron-wechat/electron-wechat %{buildroot}%{_bindir}/electron-wechat
echo "[Desktop Entry]
Name=Freewechat
GenericName=Third party Wechat client
Comment=Wechat desktop application
Exec=electron-wechat %U
Terminal=false
Type=Application
Icon=electron-wechat
StartupWMClass=freechat
X-Desktop-File-Install-Version=%{version}
Categories=Network;WebBrowser;" > "%{buildroot}%{_datadir}/applications/electron-wechat.desktop"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/opt/electron-wechat
%{_bindir}/electron-wechat
%{_datadir}/applications/electron-wechat.desktop
%{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/16x16
%{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/electron-wechat.png
%{_datadir}/icons/hicolor/32x32
%{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/electron-wechat.png
%{_datadir}/icons/hicolor/128x128
%{_datadir}/icons/hicolor/128x128/apps
%{_datadir}/icons/hicolor/128x128/apps/electron-wechat.png
%{_datadir}/icons/hicolor/256x256
%{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/256x256/apps/electron-wechat.png
%{_datadir}/icons/hicolor/512x512
%{_datadir}/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/512x512/apps/electron-wechat.png

%changelog

