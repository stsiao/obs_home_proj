#
# spec file for package wolai
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


Name:           wolai
Version:        1.2.3
Release:        0
Summary:        a new form of document system
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        MIT
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          Productivity/Office/Organizers
Url:            https://www.wolai.com
Source0:         %{name}.AppImage
# BuildRequires:  
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:	wolai = %{version}
Obsoletes:	wolai < %{version}

%description
WOLAI is a new form of document system. It is very different from all the traditional documents and online documents you used in the past. Learning to use WOLAI is equivalent to having a powerful personal and team productivity tool

%prep
chmod +x %{S:0}
%{S:0} --appimage-extract

%build
pushd squashfs-root
mv usr/lib/* ./
rm wolai.png
# mv usr/share/icons/hicolor/0x0/apps/wolai.png ./
# rm -rf usr
rm -rf usr/lib
rm AppRun
rm wolai.desktop
rm .DirIcon
popd

%install
mkdir -p %{buildroot}/opt/
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_datadir}/applications

cp -rf squashfs-root %{buildroot}/opt/com.wolai
chmod 755 %{buildroot}/opt/com.wolai -R
ln -s /opt/com.wolai/wolai %{buildroot}%{_bindir}/wolai

for n in 16x16 32x32 48x48 64x64 128x128 256x256 512x512 1024x1024
do
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$n/apps
	cp %{buildroot}/opt/com.wolai/usr/share/icons/hicolor/$n/apps/wolai.png %{buildroot}%{_datadir}/icons/hicolor/$n/apps/
done

echo "[Desktop Entry]
Name=Wolai 我来
GenericName=Document System
Comment=A new form of document system
Exec=wolai
Terminal=false
Type=Application
Icon=wolai
X-Desktop-File-Install-Version=%{version}
Categories=Office;Utility;" > %{buildroot}%{_datadir}/applications/wolai.desktop

rm -rf %{buildroot}/opt/com.wolai/usr

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/opt/com.wolai
%{_bindir}/wolai
%{_datadir}/applications/wolai.desktop
%{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/16x16
%{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/wolai.png
%{_datadir}/icons/hicolor/32x32
%{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/wolai.png
%{_datadir}/icons/hicolor/128x128
%{_datadir}/icons/hicolor/128x128/apps
%{_datadir}/icons/hicolor/128x128/apps/wolai.png
%{_datadir}/icons/hicolor/256x256
%{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/256x256/apps/wolai.png
%{_datadir}/icons/hicolor/512x512
%{_datadir}/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/512x512/apps/wolai.png

%changelog

