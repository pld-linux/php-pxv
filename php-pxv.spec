Summary:	PHP XML Validator
Name:		php-pxv
Version:	0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	%{name}-%{version}.tar.gz
#URL:		
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	libxml2-devel
BuildRequires:	php-devel

%description
This package allows to validate XML documents in PHP.

%description -l pl
Ten pakiet umo¿liwia sprawdzanie poprawnosci dokumentow XML w PHP.

%prep
%setup -q

%build
aclocal
%{__autoconf}
autoheader
%{__automake}
%configure --libdir=/usr/lib/php
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove pxv %{_sysconfdir}/php.ini
fi

%post
%{_sbindir}/php-module-install install pxv %{_sysconfdir}/php.ini

%postun



%files
%defattr(644,root,root,755)
%doc README ChangeLog
/usr/lib/php
