# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Filter-Zlib

Summary: POE filter wrapped around Compress::Zlib
Name: perl-POE-Filter-Zlib
Version: 1.8
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Filter-Zlib/

Source: http://www.cpan.org/modules/by-module/POE/POE-Filter-Zlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A POE filter wrapped around Compress::Zlib.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/POE/Filter/
%{perl_vendorlib}/POE/Filter/Zlib.pm
%{perl_vendorlib}/POE/Filter/Zlib/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.8-1
- Updated to release 1.8.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.7-1
- Updated to release 1.7.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.
