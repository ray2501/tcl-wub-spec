#
# spec file for package tcl-wub
#

%define tarname wub

Name:           tcl-wub
BuildRequires:  tcl
BuildRequires:  systemd-rpm-macros
Version:        5.0
Release:        0
Summary:        BSD-3-Clause
Url:            https://github.com/tcler/wub
License:        New BSD License
Group:          Productivity/Networking/Web/Servers
BuildArch:      noarch
Requires:       tcl >= 8.6
BuildRoot:      %{_tmppath}/%{tarname}-%{version}-build
Source0:        %{tarname}-%{version}.tar.gz
Source1:        wub.service

%description
Wub is a web-server written in pure-Tcl.

%prep
%setup -q -n %{tarname}

%build

%install
dir=%buildroot/var/opt/%tarname
mkdir -m755 -p $dir
cp -a -R * $dir

install -D -m 644 %{S:1} %{buildroot}%{_unitdir}/wub.service

%pre
%service_add_pre wub.service

%post
%service_add_post wub.service

%preun
%service_del_preun wub.service

%postun
%service_del_postun wub.service

%files
%defattr(-,wwwrun,www)
%attr(-,wwwrun,www) /var/opt/wub
%{_unitdir}/wub.service

%changelog

