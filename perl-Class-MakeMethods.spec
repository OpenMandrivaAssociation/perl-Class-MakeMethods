%define upstream_name    Class-MakeMethods
%define upstream_version 1.01

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 2

Summary: 	Generate common types of methods 
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%define _requires_exceptions perl(Class::MakeMethods::Template::Array)

%description
By passing arguments to "use Class::MakeMethods ..." statements, you can
select from a library of hundreds of common types of methods, which are
dynamically generated and installed as subroutines in your module,
simplifying the code for your class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/Class/benchmark.pl
%{_mandir}/man*/*

