Summary:	PHP XML Validator
Summary(pl):	Narzêdzie do kontroli poprawno¶ci XML-a w PHP
Name:		php-pxv
Version:	0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	ac1b87ed1f8cbd74230922365728b5e2
#URL:
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2-devel
BuildRequires:	php-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows to validate XML documents in PHP.

%description -l pl
Ten pakiet umo¿liwia sprawdzanie poprawno¶ci dokumentów XML w PHP.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--libdir=%{_libdir}/php
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove pxv %{_sysconfdir}/php.ini
fi

%post
%{_sbindir}/php-module-install install pxv %{_sysconfdir}/php.ini

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%{_libdir}/php/*
