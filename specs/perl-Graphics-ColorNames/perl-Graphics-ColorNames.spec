# $Id$
# Authority: dries
# Upstream: Robert Rothenberg <rrwo$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Graphics-ColorNames

Summary: Defines RGB values for common color names
Name: perl-Graphics-ColorNames
Version: 1.06
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graphics-ColorNames/

Source: http://www.cpan.org/modules/by-module/Graphics/Graphics-ColorNames-%{version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/Graphics/Graphics-ColorNames-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module defines RGB values for common color names. The intention is
to (1) provide a common module that authors can use with other modules
to specify colors; and (2) free module authors from having to "re-invent
the wheel" whenever they decide to give the users the option of
specifying a color by name rather than RGB value.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Graphics/ColorNames.pm
%{perl_vendorlib}/Graphics/ColorNames/*
%{perl_vendorlib}/Graphics/ColourNames.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1.2
- Rebuild for Fedora Core 5.

* Sat Jun 18 2005 Dries Verachtert <dries@ulyssis.org> - 1.06
- Update

* Sat Oct 30 2004 Dries Verachtert <dries@ulyssis.org> - 1.05
- Update to release 1.05

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.3901-1
- Initial package.
