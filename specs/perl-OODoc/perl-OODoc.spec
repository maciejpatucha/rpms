# $Id$
# Authority: dries
# Upstream: Mark Overmeer <mark$overmeer,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name OODoc

Summary: Creates code related documentation
Name: perl-OODoc
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/OODoc/

Source: http://www.cpan.org/modules/by-module/OODoc/OODoc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Creates code related documentation in an object oriented way.

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
%doc ChangeLog LICENSE MANIFEST META.yml README
%doc %{_mandir}/man1/oodist.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/oodist
%{perl_vendorlib}/OODoc.pm
%{perl_vendorlib}/OODoc.pod
%{perl_vendorlib}/OODoc/

%changelog
* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 1.01-1
- Updated to latest upstream version { old source not available }

* Wed Jan 10 2007 Dries Verachtert <dries@ulyssis.org> - 0.98-1
- Updated to release 0.98.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Initial package.
