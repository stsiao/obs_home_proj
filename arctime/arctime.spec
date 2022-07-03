#
# spec file for package arctime
#
# Copyright (c) 2020 Sigmond Tsiao <gamebus2011@hotmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.links2linux.org/
#


Name:           arctime
Version:        2.2.1
Release:        0
Summary:    Arctime installer
License:        SUSE-NonFree
Group:          Productivity/Text/Editors
Url:                https://arctime.org/
Source1:        %{name}.sh.in
Requires:       java-1_8_0-openjdk
Requires:       vlc
Requires:       vlc-codecs
Provides:       arctime = %{version}
ExclusiveArch:  x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Installer script for Arctime.
DO NOT UPDATE, there's an import bug on version > 2.2.1.

%prep

%build

%install
%suse_install_update_script %{SOURCE1}
install -d %{buildroot}%{_localstatedir}/adm/update-messages
touch %{buildroot}%{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-1
install -d %{buildroot}/opt/org.arctime
install -d %{buildroot}/opt/org.arctime/ArcTime_lib
install -d %{buildroot}/opt/org.arctime/resources
install -d %{buildroot}/opt/org.arctime/resources/help
install -d %{buildroot}/opt/org.arctime/tools
install -d %{buildroot}/opt/org.arctime/tools/config
install -d %{buildroot}/opt/org.arctime/tools/x64
install -d %{buildroot}/opt/org.arctime/tools/x86
install -d %{buildroot}%{_datadir}/applications/
install -d %{buildroot}%{_datadir}/icons/
install -d %{buildroot}%{_datadir}/icons/hicolor/
install -d %{buildroot}%{_datadir}/icons/hicolor/16x16/
install -d %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/
install -d %{buildroot}%{_datadir}/icons/hicolor/24x24/
install -d %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
install -d %{buildroot}%{_datadir}/icons/hicolor/48x48/
install -d %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

touch %{buildroot}/opt/org.arctime/arctime
touch %{buildroot}/opt/org.arctime/ArcTime.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/bcprov-jdk15on-159.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/commons-codec-1.9.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/commons-configuration2-2.1.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/commons-io-2.4.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/commons-lang2-2.3.3.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/commons-lang3-3.3.2.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/commons-logging-1.2.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/commons-net-2.0.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/commons-validator-1.4.0.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/darcula.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/dom4j-1.6.1.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/fluent-hc-4.5.1.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/gson-2.7.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/httpclient-4.5.1.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/httpclient-cache-4.5.1.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/httpclient-win-4.5.1.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/httpcore-4.4.3.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/httpmime-4.5.1.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/iconloader-20170615.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/iconloader.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/icu4j-61_1.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/ImageFilters.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/jaxen-1.1-beta-6.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/jdom-bin-2.0.3.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/jfugue-4.0.3.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/jgoodies-forms-1.8.0.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/jna-4.1.0.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/jna-platform-4.1.0.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/jsoup-1.10.2.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/jxl.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/MacWidgets.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/montemedia.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/oshi-core-3.5.0.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/pngj-2.1.1.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/sclasses.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/slf4j-api-1.7.10.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/slf4j-simple-1.7.13.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/slf4j-sp-2.0.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/swingx-all-1.6.5-1.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/threetenbp-1.3.6.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/thumbnailator-0.4.7-all.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/vlcj-3.10.1.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/zero-allocation-hashing-0.8.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/zxing-core-3.3.1.jar
touch %{buildroot}/opt/org.arctime/ArcTime_lib/zxing-javase-3.3.1.jar
touch %{buildroot}/opt/org.arctime/Linux中的安装与使用方法.txt
touch %{buildroot}/opt/org.arctime/resources/AssStyles.txt
touch %{buildroot}/opt/org.arctime/resources/fontawesome-webfont.ttf
touch %{buildroot}/opt/org.arctime/resources/help/Introduction.txt
touch %{buildroot}/opt/org.arctime/resources/Roboto-Regular.ttf
touch %{buildroot}/opt/org.arctime/resources/SpecialCharacter.txt
touch %{buildroot}/opt/org.arctime/resources/xaet
touch %{buildroot}/opt/org.arctime/run.sh
touch %{buildroot}/opt/org.arctime/tools/config/vlcpath.txt
touch "%{buildroot}/opt/org.arctime/tools/GPL LICENSE.txt"
touch %{buildroot}/opt/org.arctime/tools/x64/ffmpeg-linux64
touch %{buildroot}/opt/org.arctime/tools/x64/ffprobe-linux64
touch %{buildroot}/opt/org.arctime/tools/x86/ffmpeg-linux32
touch %{buildroot}/opt/org.arctime/tools/x86/ffprobe-linux32
touch %{buildroot}%{_datadir}/applications/arctime.desktop
touch %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/arctime.png
touch %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/arctime.png
touch %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/arctime.png
touch %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/arctime.png

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_localstatedir}/adm/update-scripts/*
%{_localstatedir}/adm/update-messages/*
%dir /opt/org.arctime
%dir /opt/org.arctime/ArcTime_lib
%dir /opt/org.arctime/resources
%dir /opt/org.arctime/resources/help
%dir /opt/org.arctime/tools
%dir /opt/org.arctime/tools/config
%dir /opt/org.arctime/tools/x64
%dir /opt/org.arctime/tools/x86
%dir %{_datadir}/applications/
%dir %{_datadir}/icons/
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/16x16/
%dir %{_datadir}/icons/hicolor/16x16/apps/
%dir %{_datadir}/icons/hicolor/24x24/
%dir %{_datadir}/icons/hicolor/24x24/apps/
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/32x32/apps/
%dir %{_datadir}/icons/hicolor/48x48/
%dir %{_datadir}/icons/hicolor/48x48/apps/
%ghost /opt/org.arctime/arctime
%ghost /opt/org.arctime/ArcTime.jar
%ghost /opt/org.arctime/ArcTime_lib/bcprov-jdk15on-159.jar
%ghost /opt/org.arctime/ArcTime_lib/commons-codec-1.9.jar
%ghost /opt/org.arctime/ArcTime_lib/commons-configuration2-2.1.jar
%ghost /opt/org.arctime/ArcTime_lib/commons-io-2.4.jar
%ghost /opt/org.arctime/ArcTime_lib/commons-lang2-2.3.3.jar
%ghost /opt/org.arctime/ArcTime_lib/commons-lang3-3.3.2.jar
%ghost /opt/org.arctime/ArcTime_lib/commons-logging-1.2.jar
%ghost /opt/org.arctime/ArcTime_lib/commons-net-2.0.jar
%ghost /opt/org.arctime/ArcTime_lib/commons-validator-1.4.0.jar
%ghost /opt/org.arctime/ArcTime_lib/darcula.jar
%ghost /opt/org.arctime/ArcTime_lib/dom4j-1.6.1.jar
%ghost /opt/org.arctime/ArcTime_lib/fluent-hc-4.5.1.jar
%ghost /opt/org.arctime/ArcTime_lib/gson-2.7.jar
%ghost /opt/org.arctime/ArcTime_lib/httpclient-4.5.1.jar
%ghost /opt/org.arctime/ArcTime_lib/httpclient-cache-4.5.1.jar
%ghost /opt/org.arctime/ArcTime_lib/httpclient-win-4.5.1.jar
%ghost /opt/org.arctime/ArcTime_lib/httpcore-4.4.3.jar
%ghost /opt/org.arctime/ArcTime_lib/httpmime-4.5.1.jar
%ghost /opt/org.arctime/ArcTime_lib/iconloader-20170615.jar
%ghost /opt/org.arctime/ArcTime_lib/iconloader.jar
%ghost /opt/org.arctime/ArcTime_lib/icu4j-61_1.jar
%ghost /opt/org.arctime/ArcTime_lib/ImageFilters.jar
%ghost /opt/org.arctime/ArcTime_lib/jaxen-1.1-beta-6.jar
%ghost /opt/org.arctime/ArcTime_lib/jdom-bin-2.0.3.jar
%ghost /opt/org.arctime/ArcTime_lib/jfugue-4.0.3.jar
%ghost /opt/org.arctime/ArcTime_lib/jgoodies-forms-1.8.0.jar
%ghost /opt/org.arctime/ArcTime_lib/jna-4.1.0.jar
%ghost /opt/org.arctime/ArcTime_lib/jna-platform-4.1.0.jar
%ghost /opt/org.arctime/ArcTime_lib/jsoup-1.10.2.jar
%ghost /opt/org.arctime/ArcTime_lib/jxl.jar
%ghost /opt/org.arctime/ArcTime_lib/MacWidgets.jar
%ghost /opt/org.arctime/ArcTime_lib/montemedia.jar
%ghost /opt/org.arctime/ArcTime_lib/oshi-core-3.5.0.jar
%ghost /opt/org.arctime/ArcTime_lib/pngj-2.1.1.jar
%ghost /opt/org.arctime/ArcTime_lib/sclasses.jar
%ghost /opt/org.arctime/ArcTime_lib/slf4j-api-1.7.10.jar
%ghost /opt/org.arctime/ArcTime_lib/slf4j-simple-1.7.13.jar
%ghost /opt/org.arctime/ArcTime_lib/slf4j-sp-2.0.jar
%ghost /opt/org.arctime/ArcTime_lib/swingx-all-1.6.5-1.jar
%ghost /opt/org.arctime/ArcTime_lib/threetenbp-1.3.6.jar
%ghost /opt/org.arctime/ArcTime_lib/thumbnailator-0.4.7-all.jar
%ghost /opt/org.arctime/ArcTime_lib/vlcj-3.10.1.jar
%ghost /opt/org.arctime/ArcTime_lib/zero-allocation-hashing-0.8.jar
%ghost /opt/org.arctime/ArcTime_lib/zxing-core-3.3.1.jar
%ghost /opt/org.arctime/ArcTime_lib/zxing-javase-3.3.1.jar
%ghost /opt/org.arctime/Linux中的安装与使用方法.txt
%ghost /opt/org.arctime/resources/AssStyles.txt
%ghost /opt/org.arctime/resources/fontawesome-webfont.ttf
%ghost /opt/org.arctime/resources/help/Introduction.txt
%ghost /opt/org.arctime/resources/Roboto-Regular.ttf
%ghost /opt/org.arctime/resources/SpecialCharacter.txt
%ghost /opt/org.arctime/resources/xaet
%ghost /opt/org.arctime/run.sh
%ghost /opt/org.arctime/tools/config/vlcpath.txt
%ghost "/opt/org.arctime/tools/GPL LICENSE.txt"
%ghost /opt/org.arctime/tools/x64/ffmpeg-linux64
%ghost /opt/org.arctime/tools/x64/ffprobe-linux64
%ghost /opt/org.arctime/tools/x86/ffmpeg-linux32
%ghost /opt/org.arctime/tools/x86/ffprobe-linux32
%ghost %{_datadir}/applications/arctime.desktop
%ghost %{_datadir}/icons/hicolor/16x16/apps/arctime.png
%ghost %{_datadir}/icons/hicolor/24x24/apps/arctime.png
%ghost %{_datadir}/icons/hicolor/32x32/apps/arctime.png
%ghost %{_datadir}/icons/hicolor/48x48/apps/arctime.png

%changelog
