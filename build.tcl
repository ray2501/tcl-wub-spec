#!/usr/bin/tclsh

set arch "noarch"
set base "wub-5.0"

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force wub.service build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tcl-wub.spec]
exec >@stdout 2>@stderr {*}$buildit

