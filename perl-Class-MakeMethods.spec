%define module  Class-MakeMethods
%define version 1.009
%define release %mkrel 1
%define	pdir	Class

Summary: 	%{module} module for perl
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source0: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/search?dist=%{module}
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	perl >= 5.005 , perl-base >= 5.005
BuildRequires:	perl-devel >= 5.005

%define _requires_exceptions perl(Class::MakeMethods::Template::Array)

%description
%{module} module for perl.  By passing arguments to "use
Class::MakeMethods ..." statements, you can select from a library of
hundreds of common types of methods, which are dynamically generated
and installed as subroutines in your module, simplifying the code for
your class.

%prep
%setup -q -n %{module}-%{version}

%build
# use all defaults

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{perl_vendorlib}/Class/MakeMethods*
%{_mandir}/man*/*

