# $Id$
# Authority: dries
# Upstream: David Wheeler <david$justatheory,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Diff-HTML

Summary: XHMTL format for Text::Diff::Unified
Name: perl-Text-Diff-HTML
Version: 0.04
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Diff-HTML/

Source: http://www.cpan.org/modules/by-module/Text/Text-Diff-HTML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl-HTML-Parser
BuildRequires: perl-Text-Diff
BuildRequires: perl-Module-Build

%description
An XHTML format for Text::Diff::Unified.

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
%{perl_vendorlib}/Text/Diff/HTML.pm

%changelog
* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
