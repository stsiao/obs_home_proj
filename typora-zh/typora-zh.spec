#
# spec file for package typora-zh
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


Name:           typora-zh
Version:        0.9.98
Release:        0
Summary:        Typora installer(Mirror in China)
License:        SUSE-NonFree
Group:          Productivity/Text/Editors
Url:            https://www.typora.io/
Source1:        %{name}.sh.in
Requires:       libXss1
Recommends:     pandoc
Conflicts:       typora
Provides:       typora-zh = %{version}
ExclusiveArch:  x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
installer script for Typora (Mirror in China)

%prep

%build

%install
%suse_install_update_script %{SOURCE1}
install -d %{buildroot}%{_localstatedir}/adm/update-messages
touch %{buildroot}%{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-1
install -d %{buildroot}/opt/io.typora
install -d %{buildroot}/opt/io.typora/locales
install -d %{buildroot}/opt/io.typora/resources
install -d %{buildroot}/opt/io.typora/resources/app
install -d %{buildroot}/opt/io.typora/resources/app/app
install -d %{buildroot}/opt/io.typora/resources/app/app/editor
install -d %{buildroot}/opt/io.typora/resources/app/app/window
install -d %{buildroot}/opt/io.typora/resources/app/asserts
install -d %{buildroot}/opt/io.typora/resources/app/asserts/icon
install -d %{buildroot}/opt/io.typora/resources/app/Docs
install -d %{buildroot}/opt/io.typora/resources/app/Docs/img
install -d %{buildroot}/opt/io.typora/resources/app/html
install -d %{buildroot}/opt/io.typora/resources/app/locales
install -d %{buildroot}/opt/io.typora/resources/app/locales/Base.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/ca-ES.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/cs-CZ.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/da-DK.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/de-CH.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/de-DE.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/el-GR.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/es-ES.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/fa-IR.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/fr-FR.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/gl-ES.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/hr-HR.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/hu-HU.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/id-ID.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/it-IT.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/ja-JP.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/ko-KR.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/nl-NL.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/pl-PL.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/pt-BR.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/pt-PT.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/ru-RU.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/sk-SK.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/sv-SE.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/tr-TR.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/uk-UA.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/vi-VN.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/zh-Hans.lproj
install -d %{buildroot}/opt/io.typora/resources/app/locales/zh-Hant.lproj
install -d %{buildroot}/opt/io.typora/resources/app/node_modules
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/chokidar
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/chokidar/node_modules
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/chokidar/node_modules/fsevents
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/chokidar/node_modules/fsevents/build
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/chokidar/node_modules/fsevents/build/Release
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/pathwatcher
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/pathwatcher/build
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/pathwatcher/build/Release
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/build
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/build/Release
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/node_modules
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/node_modules/cld
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/node_modules/cld/build
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/node_modules/cld/build/Release
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/vendor
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/vendor/hunspell_dictionaries
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/vscode-ripgrep
install -d %{buildroot}/opt/io.typora/resources/app/node_modules/vscode-ripgrep/bin
install -d %{buildroot}/opt/io.typora/resources/app/setting-dist
install -d %{buildroot}/opt/io.typora/resources/app/setting-dist/static
install -d %{buildroot}/opt/io.typora/resources/app/setting-dist/static/css
install -d %{buildroot}/opt/io.typora/resources/app/setting-dist/static/js
install -d %{buildroot}/opt/io.typora/resources/app/setting-dist/static/media
install -d %{buildroot}/opt/io.typora/resources/app/style
install -d %{buildroot}/opt/io.typora/resources/app/style/font-awesome-4.1.0
install -d %{buildroot}/opt/io.typora/resources/app/style/font-awesome-4.1.0/css
install -d %{buildroot}/opt/io.typora/resources/app/style/font-awesome-4.1.0/fonts
install -d %{buildroot}/opt/io.typora/resources/app/style/ionicons-2.0.1
install -d %{buildroot}/opt/io.typora/resources/app/style/ionicons-2.0.1/css
install -d %{buildroot}/opt/io.typora/resources/app/style/ionicons-2.0.1/fonts
install -d %{buildroot}/opt/io.typora/resources/app/style/themes
install -d %{buildroot}/opt/io.typora/resources/app/style/themes/github
install -d %{buildroot}/opt/io.typora/resources/app/style/themes/newsprint
install -d %{buildroot}/opt/io.typora/resources/app/style/themes/night
install -d %{buildroot}/opt/io.typora/resources/app/style/themes/pixyll
install -d %{buildroot}/opt/io.typora/resources/app/style/typora-icon
install -d %{buildroot}/opt/io.typora/resources/app/style/typora-icon/fonts
install -d %{buildroot}/opt/io.typora/resources/app/updater
install -d %{buildroot}/opt/io.typora/swiftshader
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
touch "%{buildroot}/opt/io.typora/version"
touch "%{buildroot}/opt/io.typora/snapshot_blob.bin"
touch "%{buildroot}/opt/io.typora/libEGL.so"
touch "%{buildroot}/opt/io.typora/libvulkan.so"
touch "%{buildroot}/opt/io.typora/resources/app/setting-dist/electron.css"
touch "%{buildroot}/opt/io.typora/resources/app/setting-dist/cocoa.css"
touch "%{buildroot}/opt/io.typora/resources/app/setting-dist/asset-manifest.json"
touch "%{buildroot}/opt/io.typora/resources/app/setting-dist/index.html"
touch "%{buildroot}/opt/io.typora/resources/app/setting-dist/static/js/main.c969bb3a.js"
touch "%{buildroot}/opt/io.typora/resources/app/setting-dist/static/css/main.d4f22f34.css"
touch "%{buildroot}/opt/io.typora/resources/app/setting-dist/static/media/photon-entypo.bf614256.woff"
touch "%{buildroot}/opt/io.typora/resources/app/setting-dist/static/media/photon-entypo.1382c29c.ttf"
touch "%{buildroot}/opt/io.typora/resources/app/setting-dist/static/media/photon-entypo.2614e058.eot"
touch "%{buildroot}/opt/io.typora/resources/app/node_modules/vscode-ripgrep/bin/rg"
touch "%{buildroot}/opt/io.typora/resources/app/node_modules/chokidar/node_modules/fsevents/build/Release/fse.node"
touch "%{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/node_modules/cld/build/Release/cld.node"
touch "%{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/build/Release/spellchecker.node"
touch "%{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/vendor/hunspell_dictionaries/en_US.aff"
touch "%{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/vendor/hunspell_dictionaries/en_GB.aff"
touch "%{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/vendor/hunspell_dictionaries/en_US.dic"
touch "%{buildroot}/opt/io.typora/resources/app/node_modules/spellchecker/vendor/hunspell_dictionaries/en_GB.dic"
touch "%{buildroot}/opt/io.typora/resources/app/node_modules/pathwatcher/build/Release/pathwatcher.node"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Custom Font.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Use Typora From Shell or cmd.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Draw Diagrams With Markdown.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Table Editing.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Code Fences Language Support.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20161117_2.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20160816_2.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Touch Bar Shot 2017-02-28 at 00.40.32.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/table-edit.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/pandoc-win.PNG"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/general.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20160814_1.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20161117_6.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20160921_2.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20160502_1.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/drag-img.gif"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/ipic.jpg"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/1.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/sshot-2.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20160816_4.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20160816_1.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20160814_5.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20161027_2.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20160816_3.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/sshot-1.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20160921_1.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20160814_7.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/img/Snip20160816_5.png"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/License Agreement.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Privacy Policy.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Install and Use Pandoc.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Change Log.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/DO NOT ADD FILES HERE"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Quick Start.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Custom Themes.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Credits.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/More Documents.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Custom Shortcut Keys.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Auto Save, Version Control and Recovery.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Markdown Reference.md"
touch "%{buildroot}/opt/io.typora/resources/app/Docs/Use Images in Typora.md"
touch "%{buildroot}/opt/io.typora/resources/app/node_modules.asar"
touch "%{buildroot}/opt/io.typora/resources/app/atom.asar"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/app-bk.ico"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/icon/icon_256x256@2x.png"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/icon/icon_32x32@2x.png"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/icon/icon_512x512@2x.png"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/icon/icon_128x128@2x.png"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/icon/icon_32x32.png"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/icon/icon_128x128.png"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/icon/icon_256x256.png"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/icon/icon_512x512.png"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/icon/icon_16x16.png"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/icon/icon_16x16@2x.png"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/file.ico"
touch "%{buildroot}/opt/io.typora/resources/app/asserts/app.ico"
touch "%{buildroot}/opt/io.typora/resources/app/app/finder-worker.js"
touch "%{buildroot}/opt/io.typora/resources/app/app/window/frame.js"
touch "%{buildroot}/opt/io.typora/resources/app/app/editor/EmojiSearchMap.js"
touch "%{buildroot}/opt/io.typora/resources/app/style/codemirror.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/base-control.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/bg.png"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/night/cursor.png"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/night/mermaid.dark.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/night/credit.html"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/night/codeblock.dark.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/night/sourcemode.dark.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/night/cursor@2x.png"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/newsprint/pt-serif-v11-latin-700.woff2"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/newsprint/pt-serif-v11-latin-italic.woff2"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/newsprint/pt-serif-v11-latin-700italic.woff2"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/newsprint/pt-serif-v11-latin-regular.woff2"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/pixyll.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/newsprint.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/pixyll/merriweather-v19-latin-700italic.woff"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/pixyll/lato-v14-latin-300italic.woff"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/pixyll/lato-v14-latin-900italic.woff"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/pixyll/lato-v14-latin-300.woff"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/pixyll/merriweather-v19-latin-300.woff"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/pixyll/merriweather-v19-latin-700.woff"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/pixyll/merriweather-v19-latin-300italic.woff"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/pixyll/lato-v14-latin-900.woff"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/Readme.md"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/night.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/github/open-sans-v17-latin-ext_latin-700.woff2"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/github/open-sans-v17-latin-ext_latin-regular.woff2"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/github/open-sans-v17-latin-ext_latin-italic.woff2"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/github/open-sans-v17-latin-ext_latin-700italic.woff2"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/whitey.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/themes/github.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/cubes.png"
touch "%{buildroot}/opt/io.typora/resources/app/style/windows-folder-icon.png"
touch "%{buildroot}/opt/io.typora/resources/app/style/typora-icon/Read Me.txt"
touch "%{buildroot}/opt/io.typora/resources/app/style/typora-icon/fonts/typora-icon.ttf"
touch "%{buildroot}/opt/io.typora/resources/app/style/typora-icon/fonts/typora-icon.woff"
touch "%{buildroot}/opt/io.typora/resources/app/style/typora-icon/fonts/typora-icon.eot"
touch "%{buildroot}/opt/io.typora/resources/app/style/typora-icon/fonts/typora-icon.svg"
touch "%{buildroot}/opt/io.typora/resources/app/style/typora-icon/selection.json"
touch "%{buildroot}/opt/io.typora/resources/app/style/typora-icon/style.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/base.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/Raleway-latin-ext.woff2"
touch "%{buildroot}/opt/io.typora/resources/app/style/ionicons-2.0.1/css/ionicons.min.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/ionicons-2.0.1/css/ionicons.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/ionicons-2.0.1/fonts/ionicons.ttf"
touch "%{buildroot}/opt/io.typora/resources/app/style/ionicons-2.0.1/fonts/ionicons.woff"
touch "%{buildroot}/opt/io.typora/resources/app/style/ionicons-2.0.1/fonts/ionicons.eot"
touch "%{buildroot}/opt/io.typora/resources/app/style/ionicons-2.0.1/fonts/ionicons.svg"
touch "%{buildroot}/opt/io.typora/resources/app/style/ionicons-2.0.1/readme.md"
touch "%{buildroot}/opt/io.typora/resources/app/style/ionicons-2.0.1/LICENSE"
touch "%{buildroot}/opt/io.typora/resources/app/style/typora-file-icon.png"
touch "%{buildroot}/opt/io.typora/resources/app/style/Raleway-latin.woff2"
touch "%{buildroot}/opt/io.typora/resources/app/style/megamenu.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/window.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/font-awesome-4.1.0/css/font-awesome.min.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/font-awesome-4.1.0/css/font-awesome.css"
touch "%{buildroot}/opt/io.typora/resources/app/style/font-awesome-4.1.0/fonts/fontawesome-webfont.woff"
touch "%{buildroot}/opt/io.typora/resources/app/style/font-awesome-4.1.0/fonts/fontawesome-webfont.svg"
touch "%{buildroot}/opt/io.typora/resources/app/style/font-awesome-4.1.0/fonts/fontawesome-webfont.ttf"
touch "%{buildroot}/opt/io.typora/resources/app/style/font-awesome-4.1.0/fonts/FontAwesome.otf"
touch "%{buildroot}/opt/io.typora/resources/app/style/font-awesome-4.1.0/fonts/fontawesome-webfont.eot"
touch "%{buildroot}/opt/io.typora/resources/app/html/preview.html"
touch "%{buildroot}/opt/io.typora/resources/app/lib.asar"
touch "%{buildroot}/opt/io.typora/resources/app/updater/updater.html"
touch "%{buildroot}/opt/io.typora/resources/app/locales/fa-IR.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/fa-IR.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/fa-IR.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/ru-RU.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/ru-RU.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/ru-RU.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/es-ES.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/es-ES.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/es-ES.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/ko-KR.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/ko-KR.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/ko-KR.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/sv-SE.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/sv-SE.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/sv-SE.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/uk-UA.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/uk-UA.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/uk-UA.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/ja-JP.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/ja-JP.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/ja-JP.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/hr-HR.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/hr-HR.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/hr-HR.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/ca-ES.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/ca-ES.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/ca-ES.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/zh-Hans.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/zh-Hans.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/zh-Hans.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/vi-VN.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/vi-VN.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/vi-VN.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/it-IT.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/it-IT.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/it-IT.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/de-DE.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/de-DE.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/de-DE.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/tr-TR.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/tr-TR.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/tr-TR.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/pt-PT.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/pt-PT.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/pt-PT.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/el-GR.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/el-GR.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/el-GR.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/id-ID.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/id-ID.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/id-ID.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/nl-NL.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/nl-NL.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/nl-NL.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/sk-SK.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/sk-SK.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/sk-SK.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/de-CH.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/de-CH.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/de-CH.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/cs-CZ.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/cs-CZ.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/cs-CZ.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/da-DK.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/da-DK.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/da-DK.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/pl-PL.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/pl-PL.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/pl-PL.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/pt-BR.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/pt-BR.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/pt-BR.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/zh-Hant.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/zh-Hant.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/zh-Hant.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/hu-HU.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/hu-HU.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/hu-HU.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/gl-ES.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/gl-ES.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/gl-ES.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/fr-FR.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/fr-FR.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/fr-FR.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/Base.lproj/Panel.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/Base.lproj/Menu.json"
touch "%{buildroot}/opt/io.typora/resources/app/locales/Base.lproj/Front.json"
touch "%{buildroot}/opt/io.typora/resources/app/package.json"
touch "%{buildroot}/opt/io.typora/resources/app/conf.default.json"
touch "%{buildroot}/opt/io.typora/resources/app/window.html"
touch "%{buildroot}/opt/io.typora/v8_context_snapshot.bin"
touch "%{buildroot}/opt/io.typora/libffmpeg.so"
touch "%{buildroot}/opt/io.typora/Typora"
touch "%{buildroot}/opt/io.typora/libvk_swiftshader.so"
touch "%{buildroot}/opt/io.typora/swiftshader/libEGL.so"
touch "%{buildroot}/opt/io.typora/swiftshader/libGLESv2.so"
touch "%{buildroot}/opt/io.typora/DO NOT ADD FILES HERE.md"
touch "%{buildroot}/opt/io.typora/icudtl.dat"
touch "%{buildroot}/opt/io.typora/locales/sw.pak"
touch "%{buildroot}/opt/io.typora/locales/hi.pak"
touch "%{buildroot}/opt/io.typora/locales/nb.pak"
touch "%{buildroot}/opt/io.typora/locales/ta.pak"
touch "%{buildroot}/opt/io.typora/locales/sk.pak"
touch "%{buildroot}/opt/io.typora/locales/es-419.pak"
touch "%{buildroot}/opt/io.typora/locales/lt.pak"
touch "%{buildroot}/opt/io.typora/locales/te.pak"
touch "%{buildroot}/opt/io.typora/locales/nl.pak"
touch "%{buildroot}/opt/io.typora/locales/vi.pak"
touch "%{buildroot}/opt/io.typora/locales/pt-BR.pak"
touch "%{buildroot}/opt/io.typora/locales/ro.pak"
touch "%{buildroot}/opt/io.typora/locales/de.pak"
touch "%{buildroot}/opt/io.typora/locales/da.pak"
touch "%{buildroot}/opt/io.typora/locales/hu.pak"
touch "%{buildroot}/opt/io.typora/locales/et.pak"
touch "%{buildroot}/opt/io.typora/locales/ko.pak"
touch "%{buildroot}/opt/io.typora/locales/ca.pak"
touch "%{buildroot}/opt/io.typora/locales/it.pak"
touch "%{buildroot}/opt/io.typora/locales/fr.pak"
touch "%{buildroot}/opt/io.typora/locales/ru.pak"
touch "%{buildroot}/opt/io.typora/locales/he.pak"
touch "%{buildroot}/opt/io.typora/locales/sl.pak"
touch "%{buildroot}/opt/io.typora/locales/zh-CN.pak"
touch "%{buildroot}/opt/io.typora/locales/pl.pak"
touch "%{buildroot}/opt/io.typora/locales/lv.pak"
touch "%{buildroot}/opt/io.typora/locales/am.pak"
touch "%{buildroot}/opt/io.typora/locales/hr.pak"
touch "%{buildroot}/opt/io.typora/locales/el.pak"
touch "%{buildroot}/opt/io.typora/locales/ml.pak"
touch "%{buildroot}/opt/io.typora/locales/uk.pak"
touch "%{buildroot}/opt/io.typora/locales/ms.pak"
touch "%{buildroot}/opt/io.typora/locales/mr.pak"
touch "%{buildroot}/opt/io.typora/locales/id.pak"
touch "%{buildroot}/opt/io.typora/locales/tr.pak"
touch "%{buildroot}/opt/io.typora/locales/bn.pak"
touch "%{buildroot}/opt/io.typora/locales/fi.pak"
touch "%{buildroot}/opt/io.typora/locales/sv.pak"
touch "%{buildroot}/opt/io.typora/locales/fil.pak"
touch "%{buildroot}/opt/io.typora/locales/cs.pak"
touch "%{buildroot}/opt/io.typora/locales/en-GB.pak"
touch "%{buildroot}/opt/io.typora/locales/pt-PT.pak"
touch "%{buildroot}/opt/io.typora/locales/kn.pak"
touch "%{buildroot}/opt/io.typora/locales/es.pak"
touch "%{buildroot}/opt/io.typora/locales/gu.pak"
touch "%{buildroot}/opt/io.typora/locales/ar.pak"
touch "%{buildroot}/opt/io.typora/locales/sr.pak"
touch "%{buildroot}/opt/io.typora/locales/th.pak"
touch "%{buildroot}/opt/io.typora/locales/ja.pak"
touch "%{buildroot}/opt/io.typora/locales/zh-TW.pak"
touch "%{buildroot}/opt/io.typora/locales/bg.pak"
touch "%{buildroot}/opt/io.typora/locales/en-US.pak"
touch "%{buildroot}/opt/io.typora/locales/fa.pak"
touch "%{buildroot}/opt/io.typora/LICENSES.chromium.html"
touch "%{buildroot}/opt/io.typora/chrome-sandbox"
touch "%{buildroot}/opt/io.typora/LICENSE"
touch "%{buildroot}/opt/io.typora/libGLESv2.so"
touch "%{buildroot}/opt/io.typora/vk_swiftshader_icd.json"
touch "%{buildroot}/opt/io.typora/chrome_200_percent.pak"
touch "%{buildroot}/opt/io.typora/resources.pak"
touch "%{buildroot}/opt/io.typora/chrome_100_percent.pak"
touch %{buildroot}%{_datadir}/applications/typora.desktop
touch %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/typora.png
touch %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/typora.png
touch %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/typora.png
touch %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/typora.png
touch %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/typora.png

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_localstatedir}/adm/update-scripts/*
%{_localstatedir}/adm/update-messages/*
%dir /opt/io.typora
%dir /opt/io.typora/locales
%dir /opt/io.typora/resources
%dir /opt/io.typora/resources/app
%dir /opt/io.typora/resources/app/app
%dir /opt/io.typora/resources/app/app/editor
%dir /opt/io.typora/resources/app/app/window
%dir /opt/io.typora/resources/app/asserts
%dir /opt/io.typora/resources/app/asserts/icon
%dir /opt/io.typora/resources/app/Docs
%dir /opt/io.typora/resources/app/Docs/img
%dir /opt/io.typora/resources/app/html
%dir /opt/io.typora/resources/app/locales
%dir /opt/io.typora/resources/app/locales/Base.lproj
%dir /opt/io.typora/resources/app/locales/ca-ES.lproj
%dir /opt/io.typora/resources/app/locales/cs-CZ.lproj
%dir /opt/io.typora/resources/app/locales/da-DK.lproj
%dir /opt/io.typora/resources/app/locales/de-CH.lproj
%dir /opt/io.typora/resources/app/locales/de-DE.lproj
%dir /opt/io.typora/resources/app/locales/el-GR.lproj
%dir /opt/io.typora/resources/app/locales/es-ES.lproj
%dir /opt/io.typora/resources/app/locales/fa-IR.lproj
%dir /opt/io.typora/resources/app/locales/fr-FR.lproj
%dir /opt/io.typora/resources/app/locales/gl-ES.lproj
%dir /opt/io.typora/resources/app/locales/hr-HR.lproj
%dir /opt/io.typora/resources/app/locales/hu-HU.lproj
%dir /opt/io.typora/resources/app/locales/id-ID.lproj
%dir /opt/io.typora/resources/app/locales/it-IT.lproj
%dir /opt/io.typora/resources/app/locales/ja-JP.lproj
%dir /opt/io.typora/resources/app/locales/ko-KR.lproj
%dir /opt/io.typora/resources/app/locales/nl-NL.lproj
%dir /opt/io.typora/resources/app/locales/pl-PL.lproj
%dir /opt/io.typora/resources/app/locales/pt-BR.lproj
%dir /opt/io.typora/resources/app/locales/pt-PT.lproj
%dir /opt/io.typora/resources/app/locales/ru-RU.lproj
%dir /opt/io.typora/resources/app/locales/sk-SK.lproj
%dir /opt/io.typora/resources/app/locales/sv-SE.lproj
%dir /opt/io.typora/resources/app/locales/tr-TR.lproj
%dir /opt/io.typora/resources/app/locales/uk-UA.lproj
%dir /opt/io.typora/resources/app/locales/vi-VN.lproj
%dir /opt/io.typora/resources/app/locales/zh-Hans.lproj
%dir /opt/io.typora/resources/app/locales/zh-Hant.lproj
%dir /opt/io.typora/resources/app/node_modules
%dir /opt/io.typora/resources/app/node_modules/chokidar
%dir /opt/io.typora/resources/app/node_modules/chokidar/node_modules
%dir /opt/io.typora/resources/app/node_modules/chokidar/node_modules/fsevents
%dir /opt/io.typora/resources/app/node_modules/chokidar/node_modules/fsevents/build
%dir /opt/io.typora/resources/app/node_modules/chokidar/node_modules/fsevents/build/Release
%dir /opt/io.typora/resources/app/node_modules/pathwatcher
%dir /opt/io.typora/resources/app/node_modules/pathwatcher/build
%dir /opt/io.typora/resources/app/node_modules/pathwatcher/build/Release
%dir /opt/io.typora/resources/app/node_modules/spellchecker
%dir /opt/io.typora/resources/app/node_modules/spellchecker/build
%dir /opt/io.typora/resources/app/node_modules/spellchecker/build/Release
%dir /opt/io.typora/resources/app/node_modules/spellchecker/node_modules
%dir /opt/io.typora/resources/app/node_modules/spellchecker/node_modules/cld
%dir /opt/io.typora/resources/app/node_modules/spellchecker/node_modules/cld/build
%dir /opt/io.typora/resources/app/node_modules/spellchecker/node_modules/cld/build/Release
%dir /opt/io.typora/resources/app/node_modules/spellchecker/vendor
%dir /opt/io.typora/resources/app/node_modules/spellchecker/vendor/hunspell_dictionaries
%dir /opt/io.typora/resources/app/node_modules/vscode-ripgrep
%dir /opt/io.typora/resources/app/node_modules/vscode-ripgrep/bin
%dir /opt/io.typora/resources/app/setting-dist
%dir /opt/io.typora/resources/app/setting-dist/static
%dir /opt/io.typora/resources/app/setting-dist/static/css
%dir /opt/io.typora/resources/app/setting-dist/static/js
%dir /opt/io.typora/resources/app/setting-dist/static/media
%dir /opt/io.typora/resources/app/style
%dir /opt/io.typora/resources/app/style/font-awesome-4.1.0
%dir /opt/io.typora/resources/app/style/font-awesome-4.1.0/css
%dir /opt/io.typora/resources/app/style/font-awesome-4.1.0/fonts
%dir /opt/io.typora/resources/app/style/ionicons-2.0.1
%dir /opt/io.typora/resources/app/style/ionicons-2.0.1/css
%dir /opt/io.typora/resources/app/style/ionicons-2.0.1/fonts
%dir /opt/io.typora/resources/app/style/themes
%dir /opt/io.typora/resources/app/style/themes/github
%dir /opt/io.typora/resources/app/style/themes/newsprint
%dir /opt/io.typora/resources/app/style/themes/night
%dir /opt/io.typora/resources/app/style/themes/pixyll
%dir /opt/io.typora/resources/app/style/typora-icon
%dir /opt/io.typora/resources/app/style/typora-icon/fonts
%dir /opt/io.typora/resources/app/updater
%dir /opt/io.typora/swiftshader
%dir %{_datadir}/icons/
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/16x16/
%dir %{_datadir}/icons/hicolor/16x16/apps/
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/32x32/apps/
%dir %{_datadir}/icons/hicolor/128x128/
%dir %{_datadir}/icons/hicolor/128x128/apps/
%dir %{_datadir}/icons/hicolor/256x256/
%dir %{_datadir}/icons/hicolor/256x256/apps/
%dir %{_datadir}/icons/hicolor/512x512/
%dir %{_datadir}/icons/hicolor/512x512/apps/
%dir %{_datadir}/applications/
%ghost %{_bindir}/typora
%ghost "%{_datadir}/applications/typora.desktop"
%ghost "%{_datadir}/icons/hicolor/16x16/apps/typora.png"
%ghost "%{_datadir}/icons/hicolor/32x32/apps/typora.png"
%ghost "%{_datadir}/icons/hicolor/128x128/apps/typora.png"
%ghost "%{_datadir}/icons/hicolor/256x256/apps/typora.png"
%ghost "%{_datadir}/icons/hicolor/512x512/apps/typora.png"
%ghost "/opt/io.typora/version"
%ghost "/opt/io.typora/snapshot_blob.bin"
%ghost "/opt/io.typora/libEGL.so"
%ghost "/opt/io.typora/libvulkan.so"
%ghost "/opt/io.typora/resources/app/setting-dist/electron.css"
%ghost "/opt/io.typora/resources/app/setting-dist/cocoa.css"
%ghost "/opt/io.typora/resources/app/setting-dist/asset-manifest.json"
%ghost "/opt/io.typora/resources/app/setting-dist/index.html"
%ghost "/opt/io.typora/resources/app/setting-dist/static/js/main.c969bb3a.js"
%ghost "/opt/io.typora/resources/app/setting-dist/static/css/main.d4f22f34.css"
%ghost "/opt/io.typora/resources/app/setting-dist/static/media/photon-entypo.bf614256.woff"
%ghost "/opt/io.typora/resources/app/setting-dist/static/media/photon-entypo.1382c29c.ttf"
%ghost "/opt/io.typora/resources/app/setting-dist/static/media/photon-entypo.2614e058.eot"
%ghost "/opt/io.typora/resources/app/node_modules/vscode-ripgrep/bin/rg"
%ghost "/opt/io.typora/resources/app/node_modules/chokidar/node_modules/fsevents/build/Release/fse.node"
%ghost "/opt/io.typora/resources/app/node_modules/spellchecker/node_modules/cld/build/Release/cld.node"
%ghost "/opt/io.typora/resources/app/node_modules/spellchecker/build/Release/spellchecker.node"
%ghost "/opt/io.typora/resources/app/node_modules/spellchecker/vendor/hunspell_dictionaries/en_US.aff"
%ghost "/opt/io.typora/resources/app/node_modules/spellchecker/vendor/hunspell_dictionaries/en_GB.aff"
%ghost "/opt/io.typora/resources/app/node_modules/spellchecker/vendor/hunspell_dictionaries/en_US.dic"
%ghost "/opt/io.typora/resources/app/node_modules/spellchecker/vendor/hunspell_dictionaries/en_GB.dic"
%ghost "/opt/io.typora/resources/app/node_modules/pathwatcher/build/Release/pathwatcher.node"
%ghost "/opt/io.typora/resources/app/Docs/Custom Font.md"
%ghost "/opt/io.typora/resources/app/Docs/Use Typora From Shell or cmd.md"
%ghost "/opt/io.typora/resources/app/Docs/Draw Diagrams With Markdown.md"
%ghost "/opt/io.typora/resources/app/Docs/Table Editing.md"
%ghost "/opt/io.typora/resources/app/Docs/Code Fences Language Support.md"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20161117_2.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20160816_2.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Touch Bar Shot 2017-02-28 at 00.40.32.png"
%ghost "/opt/io.typora/resources/app/Docs/img/table-edit.png"
%ghost "/opt/io.typora/resources/app/Docs/img/pandoc-win.PNG"
%ghost "/opt/io.typora/resources/app/Docs/img/general.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20160814_1.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20161117_6.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20160921_2.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20160502_1.png"
%ghost "/opt/io.typora/resources/app/Docs/img/drag-img.gif"
%ghost "/opt/io.typora/resources/app/Docs/img/ipic.jpg"
%ghost "/opt/io.typora/resources/app/Docs/img/1.png"
%ghost "/opt/io.typora/resources/app/Docs/img/sshot-2.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20160816_4.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20160816_1.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20160814_5.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20161027_2.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20160816_3.png"
%ghost "/opt/io.typora/resources/app/Docs/img/sshot-1.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20160921_1.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20160814_7.png"
%ghost "/opt/io.typora/resources/app/Docs/img/Snip20160816_5.png"
%ghost "/opt/io.typora/resources/app/Docs/License Agreement.md"
%ghost "/opt/io.typora/resources/app/Docs/Privacy Policy.md"
%ghost "/opt/io.typora/resources/app/Docs/Install and Use Pandoc.md"
%ghost "/opt/io.typora/resources/app/Docs/Change Log.md"
%ghost "/opt/io.typora/resources/app/Docs/DO NOT ADD FILES HERE"
%ghost "/opt/io.typora/resources/app/Docs/Quick Start.md"
%ghost "/opt/io.typora/resources/app/Docs/Custom Themes.md"
%ghost "/opt/io.typora/resources/app/Docs/Credits.md"
%ghost "/opt/io.typora/resources/app/Docs/More Documents.md"
%ghost "/opt/io.typora/resources/app/Docs/Custom Shortcut Keys.md"
%ghost "/opt/io.typora/resources/app/Docs/Auto Save, Version Control and Recovery.md"
%ghost "/opt/io.typora/resources/app/Docs/Markdown Reference.md"
%ghost "/opt/io.typora/resources/app/Docs/Use Images in Typora.md"
%ghost "/opt/io.typora/resources/app/node_modules.asar"
%ghost "/opt/io.typora/resources/app/atom.asar"
%ghost "/opt/io.typora/resources/app/asserts/app-bk.ico"
%ghost "/opt/io.typora/resources/app/asserts/icon/icon_256x256@2x.png"
%ghost "/opt/io.typora/resources/app/asserts/icon/icon_32x32@2x.png"
%ghost "/opt/io.typora/resources/app/asserts/icon/icon_512x512@2x.png"
%ghost "/opt/io.typora/resources/app/asserts/icon/icon_128x128@2x.png"
%ghost "/opt/io.typora/resources/app/asserts/icon/icon_32x32.png"
%ghost "/opt/io.typora/resources/app/asserts/icon/icon_128x128.png"
%ghost "/opt/io.typora/resources/app/asserts/icon/icon_256x256.png"
%ghost "/opt/io.typora/resources/app/asserts/icon/icon_512x512.png"
%ghost "/opt/io.typora/resources/app/asserts/icon/icon_16x16.png"
%ghost "/opt/io.typora/resources/app/asserts/icon/icon_16x16@2x.png"
%ghost "/opt/io.typora/resources/app/asserts/file.ico"
%ghost "/opt/io.typora/resources/app/asserts/app.ico"
%ghost "/opt/io.typora/resources/app/app/finder-worker.js"
%ghost "/opt/io.typora/resources/app/app/window/frame.js"
%ghost "/opt/io.typora/resources/app/app/editor/EmojiSearchMap.js"
%ghost "/opt/io.typora/resources/app/style/codemirror.css"
%ghost "/opt/io.typora/resources/app/style/base-control.css"
%ghost "/opt/io.typora/resources/app/style/bg.png"
%ghost "/opt/io.typora/resources/app/style/themes/night/cursor.png"
%ghost "/opt/io.typora/resources/app/style/themes/night/mermaid.dark.css"
%ghost "/opt/io.typora/resources/app/style/themes/night/credit.html"
%ghost "/opt/io.typora/resources/app/style/themes/night/codeblock.dark.css"
%ghost "/opt/io.typora/resources/app/style/themes/night/sourcemode.dark.css"
%ghost "/opt/io.typora/resources/app/style/themes/night/cursor@2x.png"
%ghost "/opt/io.typora/resources/app/style/themes/newsprint/pt-serif-v11-latin-700.woff2"
%ghost "/opt/io.typora/resources/app/style/themes/newsprint/pt-serif-v11-latin-italic.woff2"
%ghost "/opt/io.typora/resources/app/style/themes/newsprint/pt-serif-v11-latin-700italic.woff2"
%ghost "/opt/io.typora/resources/app/style/themes/newsprint/pt-serif-v11-latin-regular.woff2"
%ghost "/opt/io.typora/resources/app/style/themes/pixyll.css"
%ghost "/opt/io.typora/resources/app/style/themes/newsprint.css"
%ghost "/opt/io.typora/resources/app/style/themes/pixyll/merriweather-v19-latin-700italic.woff"
%ghost "/opt/io.typora/resources/app/style/themes/pixyll/lato-v14-latin-300italic.woff"
%ghost "/opt/io.typora/resources/app/style/themes/pixyll/lato-v14-latin-900italic.woff"
%ghost "/opt/io.typora/resources/app/style/themes/pixyll/lato-v14-latin-300.woff"
%ghost "/opt/io.typora/resources/app/style/themes/pixyll/merriweather-v19-latin-300.woff"
%ghost "/opt/io.typora/resources/app/style/themes/pixyll/merriweather-v19-latin-700.woff"
%ghost "/opt/io.typora/resources/app/style/themes/pixyll/merriweather-v19-latin-300italic.woff"
%ghost "/opt/io.typora/resources/app/style/themes/pixyll/lato-v14-latin-900.woff"
%ghost "/opt/io.typora/resources/app/style/themes/Readme.md"
%ghost "/opt/io.typora/resources/app/style/themes/night.css"
%ghost "/opt/io.typora/resources/app/style/themes/github/open-sans-v17-latin-ext_latin-700.woff2"
%ghost "/opt/io.typora/resources/app/style/themes/github/open-sans-v17-latin-ext_latin-regular.woff2"
%ghost "/opt/io.typora/resources/app/style/themes/github/open-sans-v17-latin-ext_latin-italic.woff2"
%ghost "/opt/io.typora/resources/app/style/themes/github/open-sans-v17-latin-ext_latin-700italic.woff2"
%ghost "/opt/io.typora/resources/app/style/themes/whitey.css"
%ghost "/opt/io.typora/resources/app/style/themes/github.css"
%ghost "/opt/io.typora/resources/app/style/cubes.png"
%ghost "/opt/io.typora/resources/app/style/windows-folder-icon.png"
%ghost "/opt/io.typora/resources/app/style/typora-icon/Read Me.txt"
%ghost "/opt/io.typora/resources/app/style/typora-icon/fonts/typora-icon.ttf"
%ghost "/opt/io.typora/resources/app/style/typora-icon/fonts/typora-icon.woff"
%ghost "/opt/io.typora/resources/app/style/typora-icon/fonts/typora-icon.eot"
%ghost "/opt/io.typora/resources/app/style/typora-icon/fonts/typora-icon.svg"
%ghost "/opt/io.typora/resources/app/style/typora-icon/selection.json"
%ghost "/opt/io.typora/resources/app/style/typora-icon/style.css"
%ghost "/opt/io.typora/resources/app/style/base.css"
%ghost "/opt/io.typora/resources/app/style/Raleway-latin-ext.woff2"
%ghost "/opt/io.typora/resources/app/style/ionicons-2.0.1/css/ionicons.min.css"
%ghost "/opt/io.typora/resources/app/style/ionicons-2.0.1/css/ionicons.css"
%ghost "/opt/io.typora/resources/app/style/ionicons-2.0.1/fonts/ionicons.ttf"
%ghost "/opt/io.typora/resources/app/style/ionicons-2.0.1/fonts/ionicons.woff"
%ghost "/opt/io.typora/resources/app/style/ionicons-2.0.1/fonts/ionicons.eot"
%ghost "/opt/io.typora/resources/app/style/ionicons-2.0.1/fonts/ionicons.svg"
%ghost "/opt/io.typora/resources/app/style/ionicons-2.0.1/readme.md"
%ghost "/opt/io.typora/resources/app/style/ionicons-2.0.1/LICENSE"
%ghost "/opt/io.typora/resources/app/style/typora-file-icon.png"
%ghost "/opt/io.typora/resources/app/style/Raleway-latin.woff2"
%ghost "/opt/io.typora/resources/app/style/megamenu.css"
%ghost "/opt/io.typora/resources/app/style/window.css"
%ghost "/opt/io.typora/resources/app/style/font-awesome-4.1.0/css/font-awesome.min.css"
%ghost "/opt/io.typora/resources/app/style/font-awesome-4.1.0/css/font-awesome.css"
%ghost "/opt/io.typora/resources/app/style/font-awesome-4.1.0/fonts/fontawesome-webfont.woff"
%ghost "/opt/io.typora/resources/app/style/font-awesome-4.1.0/fonts/fontawesome-webfont.svg"
%ghost "/opt/io.typora/resources/app/style/font-awesome-4.1.0/fonts/fontawesome-webfont.ttf"
%ghost "/opt/io.typora/resources/app/style/font-awesome-4.1.0/fonts/FontAwesome.otf"
%ghost "/opt/io.typora/resources/app/style/font-awesome-4.1.0/fonts/fontawesome-webfont.eot"
%ghost "/opt/io.typora/resources/app/html/preview.html"
%ghost "/opt/io.typora/resources/app/lib.asar"
%ghost "/opt/io.typora/resources/app/updater/updater.html"
%ghost "/opt/io.typora/resources/app/locales/fa-IR.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/fa-IR.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/fa-IR.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/ru-RU.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/ru-RU.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/ru-RU.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/es-ES.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/es-ES.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/es-ES.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/ko-KR.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/ko-KR.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/ko-KR.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/sv-SE.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/sv-SE.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/sv-SE.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/uk-UA.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/uk-UA.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/uk-UA.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/ja-JP.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/ja-JP.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/ja-JP.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/hr-HR.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/hr-HR.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/hr-HR.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/ca-ES.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/ca-ES.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/ca-ES.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/zh-Hans.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/zh-Hans.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/zh-Hans.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/vi-VN.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/vi-VN.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/vi-VN.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/it-IT.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/it-IT.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/it-IT.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/de-DE.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/de-DE.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/de-DE.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/tr-TR.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/tr-TR.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/tr-TR.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/pt-PT.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/pt-PT.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/pt-PT.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/el-GR.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/el-GR.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/el-GR.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/id-ID.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/id-ID.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/id-ID.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/nl-NL.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/nl-NL.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/nl-NL.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/sk-SK.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/sk-SK.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/sk-SK.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/de-CH.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/de-CH.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/de-CH.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/cs-CZ.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/cs-CZ.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/cs-CZ.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/da-DK.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/da-DK.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/da-DK.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/pl-PL.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/pl-PL.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/pl-PL.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/pt-BR.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/pt-BR.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/pt-BR.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/zh-Hant.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/zh-Hant.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/zh-Hant.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/hu-HU.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/hu-HU.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/hu-HU.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/gl-ES.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/gl-ES.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/gl-ES.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/fr-FR.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/fr-FR.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/fr-FR.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/locales/Base.lproj/Panel.json"
%ghost "/opt/io.typora/resources/app/locales/Base.lproj/Menu.json"
%ghost "/opt/io.typora/resources/app/locales/Base.lproj/Front.json"
%ghost "/opt/io.typora/resources/app/package.json"
%ghost "/opt/io.typora/resources/app/conf.default.json"
%ghost "/opt/io.typora/resources/app/window.html"
%ghost "/opt/io.typora/v8_context_snapshot.bin"
%ghost "/opt/io.typora/libffmpeg.so"
%ghost "/opt/io.typora/Typora"
%ghost "/opt/io.typora/libvk_swiftshader.so"
%ghost "/opt/io.typora/swiftshader/libEGL.so"
%ghost "/opt/io.typora/swiftshader/libGLESv2.so"
%ghost "/opt/io.typora/DO NOT ADD FILES HERE.md"
%ghost "/opt/io.typora/icudtl.dat"
%ghost "/opt/io.typora/locales/sw.pak"
%ghost "/opt/io.typora/locales/hi.pak"
%ghost "/opt/io.typora/locales/nb.pak"
%ghost "/opt/io.typora/locales/ta.pak"
%ghost "/opt/io.typora/locales/sk.pak"
%ghost "/opt/io.typora/locales/es-419.pak"
%ghost "/opt/io.typora/locales/lt.pak"
%ghost "/opt/io.typora/locales/te.pak"
%ghost "/opt/io.typora/locales/nl.pak"
%ghost "/opt/io.typora/locales/vi.pak"
%ghost "/opt/io.typora/locales/pt-BR.pak"
%ghost "/opt/io.typora/locales/ro.pak"
%ghost "/opt/io.typora/locales/de.pak"
%ghost "/opt/io.typora/locales/da.pak"
%ghost "/opt/io.typora/locales/hu.pak"
%ghost "/opt/io.typora/locales/et.pak"
%ghost "/opt/io.typora/locales/ko.pak"
%ghost "/opt/io.typora/locales/ca.pak"
%ghost "/opt/io.typora/locales/it.pak"
%ghost "/opt/io.typora/locales/fr.pak"
%ghost "/opt/io.typora/locales/ru.pak"
%ghost "/opt/io.typora/locales/he.pak"
%ghost "/opt/io.typora/locales/sl.pak"
%ghost "/opt/io.typora/locales/zh-CN.pak"
%ghost "/opt/io.typora/locales/pl.pak"
%ghost "/opt/io.typora/locales/lv.pak"
%ghost "/opt/io.typora/locales/am.pak"
%ghost "/opt/io.typora/locales/hr.pak"
%ghost "/opt/io.typora/locales/el.pak"
%ghost "/opt/io.typora/locales/ml.pak"
%ghost "/opt/io.typora/locales/uk.pak"
%ghost "/opt/io.typora/locales/ms.pak"
%ghost "/opt/io.typora/locales/mr.pak"
%ghost "/opt/io.typora/locales/id.pak"
%ghost "/opt/io.typora/locales/tr.pak"
%ghost "/opt/io.typora/locales/bn.pak"
%ghost "/opt/io.typora/locales/fi.pak"
%ghost "/opt/io.typora/locales/sv.pak"
%ghost "/opt/io.typora/locales/fil.pak"
%ghost "/opt/io.typora/locales/cs.pak"
%ghost "/opt/io.typora/locales/en-GB.pak"
%ghost "/opt/io.typora/locales/pt-PT.pak"
%ghost "/opt/io.typora/locales/kn.pak"
%ghost "/opt/io.typora/locales/es.pak"
%ghost "/opt/io.typora/locales/gu.pak"
%ghost "/opt/io.typora/locales/ar.pak"
%ghost "/opt/io.typora/locales/sr.pak"
%ghost "/opt/io.typora/locales/th.pak"
%ghost "/opt/io.typora/locales/ja.pak"
%ghost "/opt/io.typora/locales/zh-TW.pak"
%ghost "/opt/io.typora/locales/bg.pak"
%ghost "/opt/io.typora/locales/en-US.pak"
%ghost "/opt/io.typora/locales/fa.pak"
%ghost "/opt/io.typora/LICENSES.chromium.html"
%ghost "/opt/io.typora/chrome-sandbox"
%ghost "/opt/io.typora/LICENSE"
%ghost "/opt/io.typora/libGLESv2.so"
%ghost "/opt/io.typora/vk_swiftshader_icd.json"
%ghost "/opt/io.typora/chrome_200_percent.pak"
%ghost "/opt/io.typora/resources.pak"
%ghost "/opt/io.typora/chrome_100_percent.pak"

%changelog
