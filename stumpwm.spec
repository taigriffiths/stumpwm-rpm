Name: stumpwm
Version: 19.11
Release: 2%{?dist}
License: GPLv2
Summary: A tiling window manager written in Common Lisp
Source0: https://github.com/%{name}/%{name}/archive/%{version}.tar.gz
BuildRequires: sbcl
BuildRequires: texinfo
BuildRequires: autoconf
BuildRequires: wget
Requires: sbcl

%description
A tiling window manager written in Common Lisp

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version} -p 1
./autogen.sh
./configure --prefix=%{buildroot}/usr/
wget https://beta.quicklisp.org/quicklisp.lisp
sbcl --load quicklisp.lisp --eval '(progn (quicklisp-quickstart:install) (ql:add-to-init-file))'

sbcl --eval '(ql:quickload "alexandria")'
sbcl --eval '(ql:quickload "cl-ppcre")'
sbcl --eval '(ql:quickload "clx")'

%build
make

%install
make install

find %{buildroot} > /tmp/stumpwm.find

rm %{buildroot}%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :

%prerun
if [ $1 = 0 ]; then
	/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
fi

%files
%{_bindir}/stumpwm
%{_infodir}/stumpwm.info.gz
