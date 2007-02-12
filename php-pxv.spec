# TODO
# - doesn't compile
# - .ini fragment
Summary:	PHP XML Validator
Summary(pl.UTF-8):   Narzędzie do kontroli poprawności XML-a w PHP
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
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows to validate XML documents in PHP.

%description -l pl.UTF-8
Ten pakiet umożliwia sprawdzanie poprawności dokumentów XML w PHP.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--libdir=%{php_extensiondir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{php_extensiondir}/*
