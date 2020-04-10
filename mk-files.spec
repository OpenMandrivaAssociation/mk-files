Summary:	Support files for bmake, the NetBSD make(1) tool
Name:		mk-files
Version:	20191111
Release:	1
License:	BSD
Group:		Development/Other
Url:		ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/
Source0:	ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/mk-%{version}.tar.gz
BuildArch:	noarch

%description
The mk-files package provides some bmake macros derived from the NetBSD
bsd.*.mk macros.  These macros allow the creation of simple Makefiles to
build all kinds of targets, including, for example, C/C++ programs and/or
shared libraries.

%prep
%setup -qn mk
sed -i.timestamp -e 's|cp_f=-f|cp_f=-pf|' install-mk

%build
echo "empty"

%install
install -m 755 -d %{buildroot}%{_datadir}/mk
env FORCE_BSD_MK=%{buildroot}/nonexistent \
	SYS_MK_DIR=%{buildroot}/nonexistent \
	sh install-mk -v -m 644 %{buildroot}%{_datadir}/mk

%files
%doc ChangeLog README
%dir %{_datadir}/mk
%{_datadir}/mk/*

