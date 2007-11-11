# $Id$
# Authority: dries
# Upstream: Michel Rodriguez <mirod$xmltwig,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-XPathEngine

Summary: Reusable XPath engine for DOM-like trees
Name: perl-XML-XPathEngine
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-XPathEngine/

Source: http://www.cpan.org/modules/by-module/XML/XML-XPathEngine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module is used to add XPath support to XML modules.

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
%{perl_vendorlib}/XML/XPathEngine.pm
%{perl_vendorlib}/XML/XPathEngine/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Updated to release 0.05.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
