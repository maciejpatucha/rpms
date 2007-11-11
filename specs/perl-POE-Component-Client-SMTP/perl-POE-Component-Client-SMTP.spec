# $Id$
# Authority: dries
# Upstream: George Nistoric&#259; <george$upg-ploiesti,ro>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-SMTP

Summary: Asynchronous mail sending with POE
Name: perl-POE-Component-Client-SMTP
Version: 0.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-SMTP/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Client-SMTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl-Module-Build

%description
Asynchronous mail sending with POE.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL installdirs="vendor"
%{__perl} Build

%install
%{__rm} -rf %{buildroot}
%{__perl} Build install destdir=%{buildroot}

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/POE/Component/Client/SMTP.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
