Name: stumpwm
Version: 19.12
Release: 1%{?dist}
License: GPLv2
Summary: A tiling window manager written in Common Lisp
Source0: https://github.com/stumpwm/stumpwm/archive/19.11.tar.gz
BuildRequires: sbcl
Requires: sbcl

%description
A tiling window manager written in Common Lisp

%build
make

%install
make install

%files
/usr/bin/stumpwm
