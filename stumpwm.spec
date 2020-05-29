Name: stumpwm
Version: 19.11
Release: 2%{?dist}
License: GPLv2
Summary: A tiling window manager written in Common Lisp
Source: https://github.com/%{name}/%{name}/archive/%{version}.tar.gz
BuildRequires: sbcl
BuildRequires: texinfo
Requires: sbcl

%description
A tiling window manager written in Common Lisp

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version} -p 1
./autogen.sh
./configure --prefix=%{buildroot}/usr/

%build
make

%install
mkdir -p %{buildroot}%{_bindir}/%{name}
install -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/stumpwm
