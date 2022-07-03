#
# spec file for package bilibili-danmuji
#
# Copyright (c) 2022 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bilibili-danmuji
Version:        2.0
Release:        0
Summary:        Bilibili live bullet chat assistant
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        GPL-3.0-only
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          Productivity/Networking/Web/Utilities
Url:            https://github.com/huihui486/bilibili-danmuji
Source0:        %{name}-%{version}.tar.bz2
Source1:        aiowebsocket.tar.bz2
Patch0:		00-about-path.diff
Patch1:		00-conf-path.diff
Patch2:		01-about-to-home.diff
Patch3:		01-log-to-home.diff
Requires:       python3-openpyxl
Requires:       python3-qt5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description
BiliBili live bullet chat assistant with Python + websocket and pyqt5. Support to modify window size, transparency, bullet screen size, color, font, etc.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3

%build
tar -jxvf %{S:1}

%install
mkdir -p %{buildroot}/opt/
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_datadir}/applications

cp -rf ../%{name}-%{version} %{buildroot}/opt/huihui486.%{name}
chmod 755 %{buildroot}/opt/huihui486.%{name} -R

for n in 16x16 32x32 128x128 256x256 512x512
do
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$n/apps
	cp %{buildroot}/opt/huihui486.%{name}/config/icon.jpg %{buildroot}%{_datadir}/icons/hicolor/$n/apps/%{name}.png
done

echo "[Desktop Entry]
Name=B站直播弹幕姬
GenericName=弹幕助手
Comment=哔哩哔哩直播弹幕助手
Exec=bash -c 'cd /opt/huihui486.%{name} && python3 start.py'
Terminal=false
Type=Application
Icon=%{name}
X-Desktop-File-Install-Version=%{version}
Categories=Network;Chat;" > %{buildroot}%{_datadir}/applications/%{name}.desktop

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/opt/huihui486.%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/16x16
%{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32
%{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128
%{_datadir}/icons/hicolor/128x128/apps
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256
%{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512
%{_datadir}/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png


%changelog

