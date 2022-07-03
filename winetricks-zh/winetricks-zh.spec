#
# spec file for package winetricks-zh
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           winetricks-zh
Version:        20210206.1
Release:        0
Summary:        A way to work around problems in WINE( add some Chinese applications)
License:        LGPL-2.1-or-later
Group:          System/Emulators/PC
URL:            https://github.com/hillwoodroc/winetricks-zh
Source0:        %{name}.sh.in
Requires:       wine
# some recommends for winetricks:
Recommends:     cabextract
Recommends:     unzip
Provides:       winetricks-zh = %{version}
ExclusiveArch:  x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Winetricks is a way to work around problems in Wine.

It has a menu of supported games/apps for which it can do all the
workarounds automatically. It also allows the installation of missing
DLLs and tweaking of various WINE settings.

This version adds some Chinese applications.

%prep

%build

%install
%suse_install_update_script %{SOURCE0}
install -d %{buildroot}%{_localstatedir}/adm/update-messages
touch %{buildroot}%{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-1
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/applications/
install -d %{buildroot}%{_datadir}/icons/
install -d %{buildroot}%{_datadir}/icons/hicolor/
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

touch %{buildroot}%{_bindir}/%{name}
touch %{buildroot}%{_datadir}/applications/%{name}.desktop
touch %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_localstatedir}/adm/update-scripts/*
%{_localstatedir}/adm/update-messages/*

%dir %{_datadir}/applications/
%dir %{_datadir}/icons/
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/

%ghost %{_bindir}/%{name}
%ghost %{_datadir}/applications/%{name}.desktop
%ghost %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
