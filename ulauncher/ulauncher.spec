#
# spec file for package ulauncher
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


Name:           ulauncher
Version:        5.14.3
Release:        0
Summary:        Linux Application Launcher
License:        GPL-3.0-only
URL:            https://ulauncher.io/
Source:         https://github.com/Ulauncher/Ulauncher/releases/download/%{version}/%{name}_%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  fdupes
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Levenshtein
BuildRequires:  pkgconfig(pygobject-2.0)
BuildRequires:  update-desktop-files
BuildRequires:  python3-distutils-extra
BuildRequires:  systemd-rpm-macros
Requires:       typelib(Keybinder) = 3.0
Requires:       python3-Levenshtein
Requires:       python3-pyinotify
Requires:       typelib(WebKit2) = 4.0
Recommends:     libappindicator-gtk3
BuildArch:      noarch

%description
Ulauncher is a fast application launcher for Linux. It's is written in Python, using GTK+.

%prep
%autosetup -n %{name}

%build
%python3_build

%install
install -D -m 0644 build/share/applications/ulauncher.desktop \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
%python3_install
install -Dpm0644 ulauncher.service %{buildroot}%{_userunitdir}/ulauncher.service
rm %{buildroot}%{_datadir}/doc/ulauncher/README.md
%suse_update_desktop_file -r %{name} "Utility;Accessibility"
%fdupes %{buildroot}/%{_prefix}

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-toggle
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*/
%{_datadir}/icons/*/*/*/*.svg
%{python3_sitelib}/%{name}-*-py*.egg-info
%{python3_sitelib}/%{name}/
%{_userunitdir}/%{name}.service

%changelog
