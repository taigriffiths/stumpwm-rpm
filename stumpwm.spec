Name: stumpwm
BuildArch: noarch
Version: 19.13
Release: 1%{?dist}
License: GPLv2
Summary: A tiling window manager written in Common Lisp
Source0: https://github.com/stumpwm/stumpwm/archive/19.11.tar.gz
Source1: ./19.11.tar.gz
BuildRequires: sbcl
Requires: sbcl

%description
A tiling window manager written in Common Lisp

%prep
%autosetup -n %{name}-%{version} -p 1
%build
make

%install
make install

%files
/usr/bin/stumpwm
