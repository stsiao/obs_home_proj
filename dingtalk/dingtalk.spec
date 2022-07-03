#
# spec file for package dingtalk
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


Name:           dingtalk
Version:        3.5.5
Release:        0
Summary:        Dingtalk official Linux experimental version.
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        MIT
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          Productivity/Networking/Talk/Clients
Url:            https://www.dingtalk.com/
Source0:        dingtalk_%{version}-Beta.0_amd64.deb
Source1:	libpango.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       dingtalk = %{version}
Obsoletes:      dingtalk < %{version}

%description
Dingtalk, produced by Alibaba, is an intelligent mobile office platform for global enterprise organizations, including PC, iPad and mobile version. This is the official Linux experimental version.
Copyright from https://aur.archlinux.org/packages/dingtalk-linux

%prep
ar -vx %{S:0}
tar -xvf data.tar.xz
tar -xjvf %{S:1}

%build
rm -rf opt/dingtalk/node_modules/.package_versions.json
rm -rf opt/dingtalk/node_modules/@ali/ding-download/.gitlab-ci.yml
rm -rf opt/dingtalk/node_modules/@ali/ding-download/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/ding-download/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-screen-projection/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-screen-projection/node_modules/@ali/ding-download/.gitlab-ci.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-screen-projection/node_modules/@ali/ding-download/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-screen-projection/node_modules/@ali/ding-download/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-screen-projection/node_modules/fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/klaw/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/@ali/ding-download/.gitlab-ci.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/@ali/ding-download/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/@ali/ding-download/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/debug/.jshintrc
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/debug/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/debug/node_modules/ms/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/binary/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/binary/.travis.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/binary/node_modules/chainsaw/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/binary/node_modules/chainsaw/node_modules/traverse/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/mkpath/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/nopt/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/nopt/.travis.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/readable-stream/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/readable-stream/node_modules/string_decoder/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/touch/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/touch/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/node-fetch/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/node-fetch/.travis.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/node-fetch/node_modules/encoding/.prettierrc.js
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/node-fetch/node_modules/encoding/.travis.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/node-fetch/node_modules/encoding/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/node-fetch/node_modules/encoding/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/semver/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/semver/.travis.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/tmp/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/tmp/.travis.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/.vscode
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/.vscode
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/@ali/ding-download/.gitlab-ci.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/@ali/ding-download/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/@ali/ding-download/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/klaw/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/.dntrc
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/doc/.build.sh
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-video/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-video/node_modules/@ali/ding-download/.gitlab-ci.yml
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-video/node_modules/@ali/ding-download/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-video/node_modules/@ali/ding-download/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-video/node_modules/fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-video/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-video/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-video/node_modules/fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-video/node_modules/fs-extra/node_modules/klaw/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-video/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-video/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/@ali/mac-crash-reporter/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/safechat/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/safechat/node_modules/@ali/ding-download/.gitlab-ci.yml
rm -rf opt/dingtalk/node_modules/@ali/safechat/node_modules/@ali/ding-download/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/safechat/node_modules/@ali/ding-download/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/safechat/node_modules/fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/safechat/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/safechat/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/@ali/safechat/node_modules/fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/safechat/node_modules/fs-extra/node_modules/klaw/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/safechat/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/safechat/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/window-talk/.npmignore
rm -rf opt/dingtalk/node_modules/@ali/window-talk/node_modules/wolfy87-eventemitter/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_ding-download@1.0.15@@ali/ding-download/.gitlab-ci.yml
rm -rf opt/dingtalk/node_modules/_@ali_ding-download@1.0.15@@ali/ding-download/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_ding-download@1.0.15@@ali/ding-download/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-screen-projection@1.1.0-Beta.3@@ali/dingtalk-screen-projection/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-screen-projection@1.1.0-Beta.3@@ali/dingtalk-screen-projection/node_modules/@ali/ding-download/.gitlab-ci.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-screen-projection@1.1.0-Beta.3@@ali/dingtalk-screen-projection/node_modules/@ali/ding-download/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-screen-projection@1.1.0-Beta.3@@ali/dingtalk-screen-projection/node_modules/@ali/ding-download/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-screen-projection@1.1.0-Beta.3@@ali/dingtalk-screen-projection/node_modules/fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-screen-projection@1.1.0-Beta.3@@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-screen-projection@1.1.0-Beta.3@@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-screen-projection@1.1.0-Beta.3@@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-screen-projection@1.1.0-Beta.3@@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/klaw/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-screen-projection@1.1.0-Beta.3@@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-screen-projection@1.1.0-Beta.3@@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/@ali/ding-download/.gitlab-ci.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/@ali/ding-download/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/@ali/ding-download/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/debug/.jshintrc
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/debug/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/debug/node_modules/ms/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/binary/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/binary/.travis.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/binary/node_modules/chainsaw/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/binary/node_modules/chainsaw/node_modules/traverse/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/mkpath/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/nopt/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/nopt/.travis.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/readable-stream/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/readable-stream/node_modules/string_decoder/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/touch/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/touch/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/node-fetch/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/node-fetch/.travis.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/node-fetch/node_modules/encoding/.prettierrc.js
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/node-fetch/node_modules/encoding/.travis.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/node-fetch/node_modules/encoding/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/node-fetch/node_modules/encoding/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/semver/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/semver/.travis.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/tmp/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/tmp/.travis.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/.vscode
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/.vscode
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/@ali/ding-download/.gitlab-ci.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/@ali/ding-download/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/@ali/ding-download/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/klaw/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/.dntrc
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/doc/.build.sh
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-video@2.3.0@@ali/dingtalk-video/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-video@2.3.0@@ali/dingtalk-video/node_modules/@ali/ding-download/.gitlab-ci.yml
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-video@2.3.0@@ali/dingtalk-video/node_modules/@ali/ding-download/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-video@2.3.0@@ali/dingtalk-video/node_modules/@ali/ding-download/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-video@2.3.0@@ali/dingtalk-video/node_modules/fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-video@2.3.0@@ali/dingtalk-video/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-video@2.3.0@@ali/dingtalk-video/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-video@2.3.0@@ali/dingtalk-video/node_modules/fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-video@2.3.0@@ali/dingtalk-video/node_modules/fs-extra/node_modules/klaw/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-video@2.3.0@@ali/dingtalk-video/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-video@2.3.0@@ali/dingtalk-video/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/_@ali_mac-crash-reporter@1.0.2@@ali/mac-crash-reporter/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_safechat@0.4.12@@ali/safechat/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_safechat@0.4.12@@ali/safechat/node_modules/@ali/ding-download/.gitlab-ci.yml
rm -rf opt/dingtalk/node_modules/_@ali_safechat@0.4.12@@ali/safechat/node_modules/@ali/ding-download/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_safechat@0.4.12@@ali/safechat/node_modules/@ali/ding-download/node_modules/@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_safechat@0.4.12@@ali/safechat/node_modules/fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_safechat@0.4.12@@ali/safechat/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_safechat@0.4.12@@ali/safechat/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_@ali_safechat@0.4.12@@ali/safechat/node_modules/fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_safechat@0.4.12@@ali/safechat/node_modules/fs-extra/node_modules/klaw/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_safechat@0.4.12@@ali/safechat/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_safechat@0.4.12@@ali/safechat/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/_@ali_ssl-root-cas@1.1.10@@ali/ssl-root-cas/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_window-talk@0.0.5@@ali/window-talk/.npmignore
rm -rf opt/dingtalk/node_modules/_@ali_window-talk@0.0.5@@ali/window-talk/node_modules/wolfy87-eventemitter/.npmignore
rm -rf opt/dingtalk/node_modules/_balanced-match@1.0.0@balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/_binary@0.3.0@binary/.npmignore
rm -rf opt/dingtalk/node_modules/_binary@0.3.0@binary/.travis.yml
rm -rf opt/dingtalk/node_modules/_binary@0.3.0@binary/node_modules/chainsaw/.npmignore
rm -rf opt/dingtalk/node_modules/_binary@0.3.0@binary/node_modules/chainsaw/node_modules/traverse/.npmignore
rm -rf opt/dingtalk/node_modules/_brace-expansion@1.1.11@brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/_brace-expansion@1.1.11@brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/_chainsaw@0.1.0@chainsaw/.npmignore
rm -rf opt/dingtalk/node_modules/_chainsaw@0.1.0@chainsaw/node_modules/traverse/.npmignore
rm -rf opt/dingtalk/node_modules/_concat-map@0.0.1@concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/_debug@2.2.0@debug/.jshintrc
rm -rf opt/dingtalk/node_modules/_debug@2.2.0@debug/.npmignore
rm -rf opt/dingtalk/node_modules/_debug@2.2.0@debug/node_modules/ms/.npmignore
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/binary/.npmignore
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/binary/.travis.yml
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/binary/node_modules/chainsaw/.npmignore
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/binary/node_modules/chainsaw/node_modules/traverse/.npmignore
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/mkpath/.npmignore
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/nopt/.npmignore
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/nopt/.travis.yml
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/readable-stream/.npmignore
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/readable-stream/node_modules/string_decoder/.npmignore
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/touch/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/touch/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_encoding@0.1.13@encoding/.prettierrc.js
rm -rf opt/dingtalk/node_modules/_encoding@0.1.13@encoding/.travis.yml
rm -rf opt/dingtalk/node_modules/_encoding@0.1.13@encoding/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/_encoding@0.1.13@encoding/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/_fs-extra@0.24.0@fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/_fs-extra@0.24.0@fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_fs-extra@0.24.0@fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_fs-extra@0.24.0@fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/_fs-extra@0.24.0@fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/_fs-extra@0.24.0@fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/_fs-extra@0.26.7@fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/_fs-extra@0.26.7@fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_fs-extra@0.26.7@fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_fs-extra@0.26.7@fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/_fs-extra@0.26.7@fs-extra/node_modules/klaw/.npmignore
rm -rf opt/dingtalk/node_modules/_fs-extra@0.26.7@fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/_fs-extra@0.26.7@fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/_glob@7.1.6@glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/_glob@7.1.6@glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/_iconv-lite@0.6.2@iconv-lite/.github
rm -rf opt/dingtalk/node_modules/_iconv-lite@0.6.2@iconv-lite/.github
rm -rf opt/dingtalk/node_modules/_jsonfile@2.4.0@jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/_klaw@1.3.1@klaw/.npmignore
rm -rf opt/dingtalk/node_modules/_minimatch@3.0.4@minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/_minimatch@3.0.4@minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/_mkpath@0.1.0@mkpath/.npmignore
rm -rf opt/dingtalk/node_modules/_ms@0.7.1@ms/.npmignore
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/.dntrc
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/doc/.build.sh
rm -rf opt/dingtalk/node_modules/_node-fetch@1.5.3@node-fetch/.npmignore
rm -rf opt/dingtalk/node_modules/_node-fetch@1.5.3@node-fetch/.travis.yml
rm -rf opt/dingtalk/node_modules/_node-fetch@1.5.3@node-fetch/node_modules/encoding/.prettierrc.js
rm -rf opt/dingtalk/node_modules/_node-fetch@1.5.3@node-fetch/node_modules/encoding/.travis.yml
rm -rf opt/dingtalk/node_modules/_node-fetch@1.5.3@node-fetch/node_modules/encoding/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/_node-fetch@1.5.3@node-fetch/node_modules/encoding/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/_nopt@3.0.6@nopt/.npmignore
rm -rf opt/dingtalk/node_modules/_nopt@3.0.6@nopt/.travis.yml
rm -rf opt/dingtalk/node_modules/_readable-stream@1.1.14@readable-stream/.npmignore
rm -rf opt/dingtalk/node_modules/_readable-stream@1.1.14@readable-stream/node_modules/string_decoder/.npmignore
rm -rf opt/dingtalk/node_modules/_rimraf@2.7.1@rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/_rimraf@2.7.1@rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/_semver@5.0.3@semver/.npmignore
rm -rf opt/dingtalk/node_modules/_semver@5.0.3@semver/.travis.yml
rm -rf opt/dingtalk/node_modules/_string_decoder@0.10.31@string_decoder/.npmignore
rm -rf opt/dingtalk/node_modules/_tmp@0.0.27@tmp/.npmignore
rm -rf opt/dingtalk/node_modules/_tmp@0.0.27@tmp/.travis.yml
rm -rf opt/dingtalk/node_modules/_touch@0.0.3@touch/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_touch@0.0.3@touch/node_modules/.bin
rm -rf opt/dingtalk/node_modules/_traverse@0.3.9@traverse/.npmignore
rm -rf opt/dingtalk/node_modules/_wolfy87-eventemitter@4.3.0@wolfy87-eventemitter/.npmignore
rm -rf opt/dingtalk/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/binary/.npmignore
rm -rf opt/dingtalk/node_modules/binary/.travis.yml
rm -rf opt/dingtalk/node_modules/binary/node_modules/chainsaw/.npmignore
rm -rf opt/dingtalk/node_modules/binary/node_modules/chainsaw/node_modules/traverse/.npmignore
rm -rf opt/dingtalk/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/chainsaw/.npmignore
rm -rf opt/dingtalk/node_modules/chainsaw/node_modules/traverse/.npmignore
rm -rf opt/dingtalk/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/debug/.jshintrc
rm -rf opt/dingtalk/node_modules/debug/.npmignore
rm -rf opt/dingtalk/node_modules/debug/node_modules/ms/.npmignore
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/.bin
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/.bin
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/binary/.npmignore
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/binary/.travis.yml
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/binary/node_modules/chainsaw/.npmignore
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/binary/node_modules/chainsaw/node_modules/traverse/.npmignore
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/mkpath/.npmignore
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/nopt/.npmignore
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/nopt/.travis.yml
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/readable-stream/.npmignore
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/readable-stream/node_modules/string_decoder/.npmignore
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/touch/node_modules/.bin
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/touch/node_modules/.bin
rm -rf opt/dingtalk/node_modules/encoding/.prettierrc.js
rm -rf opt/dingtalk/node_modules/encoding/.travis.yml
rm -rf opt/dingtalk/node_modules/encoding/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/encoding/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/fs-extra/.npmignore
rm -rf opt/dingtalk/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/fs-extra/node_modules/.bin
rm -rf opt/dingtalk/node_modules/fs-extra/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/fs-extra/node_modules/klaw/.npmignore
rm -rf opt/dingtalk/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/fs-extra/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/jsonfile/.npmignore
rm -rf opt/dingtalk/node_modules/klaw/.npmignore
rm -rf opt/dingtalk/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/mkpath/.npmignore
rm -rf opt/dingtalk/node_modules/ms/.npmignore
rm -rf opt/dingtalk/node_modules/nan/.dntrc
rm -rf opt/dingtalk/node_modules/nan/doc/.build.sh
rm -rf opt/dingtalk/node_modules/node-fetch/.npmignore
rm -rf opt/dingtalk/node_modules/node-fetch/.travis.yml
rm -rf opt/dingtalk/node_modules/node-fetch/node_modules/encoding/.prettierrc.js
rm -rf opt/dingtalk/node_modules/node-fetch/node_modules/encoding/.travis.yml
rm -rf opt/dingtalk/node_modules/node-fetch/node_modules/encoding/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/node-fetch/node_modules/encoding/node_modules/iconv-lite/.github
rm -rf opt/dingtalk/node_modules/nopt/.npmignore
rm -rf opt/dingtalk/node_modules/nopt/.travis.yml
rm -rf opt/dingtalk/node_modules/readable-stream/.npmignore
rm -rf opt/dingtalk/node_modules/readable-stream/node_modules/string_decoder/.npmignore
rm -rf opt/dingtalk/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/balanced-match/.npmignore
rm -rf opt/dingtalk/node_modules/rimraf/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/node_modules/concat-map/.travis.yml
rm -rf opt/dingtalk/node_modules/semver/.npmignore
rm -rf opt/dingtalk/node_modules/semver/.travis.yml
rm -rf opt/dingtalk/node_modules/string_decoder/.npmignore
rm -rf opt/dingtalk/node_modules/tmp/.npmignore
rm -rf opt/dingtalk/node_modules/tmp/.travis.yml
rm -rf opt/dingtalk/node_modules/touch/node_modules/.bin
rm -rf opt/dingtalk/node_modules/touch/node_modules/.bin
rm -rf opt/dingtalk/node_modules/traverse/.npmignore
rm -rf opt/dingtalk/node_modules/wolfy87-eventemitter/.npmignore
rm -rf opt/dingtalk/web_content/assets/img/.gitkeep
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_callbacks.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_callbacks_12_inl.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_callbacks_pre_12_inl.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_converters.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_converters_43_inl.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_converters_pre_43_inl.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_implementation_12_inl.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_implementation_pre_12_inl.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_maybe_43_inl.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_maybe_pre_43_inl.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_new.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_object_wrap.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_persistent_12_inl.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_persistent_pre_12_inl.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_string_bytes.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_typedarray_contents.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/nan_weak.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_callbacks.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_callbacks_12_inl.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_callbacks_pre_12_inl.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_converters.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_converters_43_inl.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_converters_pre_43_inl.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_implementation_12_inl.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_implementation_pre_12_inl.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_maybe_43_inl.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_maybe_pre_43_inl.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_new.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_object_wrap.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_persistent_12_inl.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_persistent_pre_12_inl.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_string_bytes.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_typedarray_contents.h
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/nan_weak.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_callbacks.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_callbacks_12_inl.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_callbacks_pre_12_inl.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_converters.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_converters_43_inl.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_converters_pre_43_inl.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_implementation_12_inl.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_implementation_pre_12_inl.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_maybe_43_inl.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_maybe_pre_43_inl.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_new.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_object_wrap.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_persistent_12_inl.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_persistent_pre_12_inl.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_string_bytes.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_typedarray_contents.h
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/nan_weak.h
rm -rf opt/dingtalk/node_modules/nan/nan.h
rm -rf opt/dingtalk/node_modules/nan/nan_callbacks.h
rm -rf opt/dingtalk/node_modules/nan/nan_callbacks_12_inl.h
rm -rf opt/dingtalk/node_modules/nan/nan_callbacks_pre_12_inl.h
rm -rf opt/dingtalk/node_modules/nan/nan_converters.h
rm -rf opt/dingtalk/node_modules/nan/nan_converters_43_inl.h
rm -rf opt/dingtalk/node_modules/nan/nan_converters_pre_43_inl.h
rm -rf opt/dingtalk/node_modules/nan/nan_implementation_12_inl.h
rm -rf opt/dingtalk/node_modules/nan/nan_implementation_pre_12_inl.h
rm -rf opt/dingtalk/node_modules/nan/nan_maybe_43_inl.h
rm -rf opt/dingtalk/node_modules/nan/nan_maybe_pre_43_inl.h
rm -rf opt/dingtalk/node_modules/nan/nan_new.h
rm -rf opt/dingtalk/node_modules/nan/nan_object_wrap.h
rm -rf opt/dingtalk/node_modules/nan/nan_persistent_12_inl.h
rm -rf opt/dingtalk/node_modules/nan/nan_persistent_pre_12_inl.h
rm -rf opt/dingtalk/node_modules/nan/nan_string_bytes.h
rm -rf opt/dingtalk/node_modules/nan/nan_typedarray_contents.h
rm -rf opt/dingtalk/node_modules/nan/nan_weak.h
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/.bin/decompress-zip
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/.bin/semver
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/bin/decompress-zip
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/.bin/nopt
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/touch/node_modules/.bin/nopt
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-silent-updater/node_modules/semver/bin/semver
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/node_modules/nan/doc/.build.sh
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/scripts/build_against_node.sh
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-sqlite3/scripts/build_against_node_webkit.sh
rm -rf opt/dingtalk/node_modules/@ali/dingtalk-video/node_modules/fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/@ali/safechat/node_modules/fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-screen-projection@1.1.0-Beta.3@@ali/dingtalk-screen-projection/node_modules/fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/.bin/decompress-zip
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/.bin/semver
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/bin/decompress-zip
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/.bin/nopt
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/decompress-zip/node_modules/touch/node_modules/.bin/nopt
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-silent-updater@0.4.2@@ali/dingtalk-silent-updater/node_modules/semver/bin/semver
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/node_modules/nan/doc/.build.sh
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/scripts/build_against_node.sh
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-sqlite3@3.4.0@@ali/dingtalk-sqlite3/scripts/build_against_node_webkit.sh
rm -rf opt/dingtalk/node_modules/_@ali_dingtalk-video@2.3.0@@ali/dingtalk-video/node_modules/fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/_@ali_safechat@0.4.12@@ali/safechat/node_modules/fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/bin/decompress-zip
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/.bin/nopt
rm -rf opt/dingtalk/node_modules/_decompress-zip@0.2.2@decompress-zip/node_modules/touch/node_modules/.bin/nopt
rm -rf opt/dingtalk/node_modules/_fs-extra@0.24.0@fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/_fs-extra@0.26.7@fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/_nan@2.2.1@nan/doc/.build.sh
rm -rf opt/dingtalk/node_modules/_semver@5.0.3@semver/bin/semver
rm -rf opt/dingtalk/node_modules/_touch@0.0.3@touch/node_modules/.bin/nopt
rm -rf opt/dingtalk/node_modules/decompress-zip/bin/decompress-zip
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/.bin/nopt
rm -rf opt/dingtalk/node_modules/decompress-zip/node_modules/touch/node_modules/.bin/nopt
rm -rf opt/dingtalk/node_modules/fs-extra/node_modules/.bin/rimraf
rm -rf opt/dingtalk/node_modules/nan/doc/.build.sh
rm -rf opt/dingtalk/node_modules/semver/bin/semver
rm -rf opt/dingtalk/node_modules/touch/node_modules/.bin/nopt

%install
mkdir -p %{buildroot}/opt/
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
cp -rf opt/dingtalk %{buildroot}/opt/dingtalk
rm -rf usr/share/applications/nwjs-dingtalk.desktop
rm -rf usr/share/doc
cp -rf usr/share/* %{buildroot}%{_datadir}
cp -f libpango* %{buildroot}/opt/dingtalk/lib/
ln -s /opt/dingtalk/nw %{buildroot}%{_bindir}/dingtalk
echo "[Desktop Entry]
Name=钉钉 for Linux
GenericName=Official Dingtalk client
Comment=Official Dingtalk desktop application
Exec=dingtalk
Terminal=false
Type=Application
Icon=dingtalk
X-Desktop-File-Install-Version=%{version}
Categories=Network;WebBrowser;" > "%{buildroot}%{_datadir}/applications/dingtalk.desktop"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/opt/dingtalk
%{_bindir}/dingtalk
%{_datadir}/applications/dingtalk.desktop
%{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/128x128
%{_datadir}/icons/hicolor/128x128/apps
%{_datadir}/icons/hicolor/16x16
%{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/24x24
%{_datadir}/icons/hicolor/24x24/apps
%{_datadir}/icons/hicolor/256x256
%{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/32x32
%{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/48x48
%{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/512x512
%{_datadir}/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/64x64
%{_datadir}/icons/hicolor/64x64/apps
%{_datadir}/icons/hicolor/96x96
%{_datadir}/icons/hicolor/96x96/apps
%{_datadir}/icons/hicolor/16x16/apps/dingtalk.png
%{_datadir}/icons/hicolor/24x24/apps/dingtalk.png
%{_datadir}/icons/hicolor/32x32/apps/dingtalk.png
%{_datadir}/icons/hicolor/48x48/apps/dingtalk.png
%{_datadir}/icons/hicolor/64x64/apps/dingtalk.png
%{_datadir}/icons/hicolor/96x96/apps/dingtalk.png
%{_datadir}/icons/hicolor/128x128/apps/dingtalk.png
%{_datadir}/icons/hicolor/256x256/apps/dingtalk.png
%{_datadir}/icons/hicolor/512x512/apps/dingtalk.png

%changelog

