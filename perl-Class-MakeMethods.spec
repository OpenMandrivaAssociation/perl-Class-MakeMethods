%define upstream_name    Class-MakeMethods
%define upstream_version 1.01

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Class::MakeMethods::Template::Array\\)'
%else
%define _requires_exceptions perl(Class::MakeMethods::Template::Array)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Generate common types of methods 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
By passing arguments to "use Class::MakeMethods ..." statements, you can
select from a library of hundreds of common types of methods, which are
dynamically generated and installed as subroutines in your module,
simplifying the code for your class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
# use all defaults

CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{perl_vendorlib}/Class/MakeMethods*
%{perl_vendorlib}/Class/benchmark.pl
%{_mandir}/man*/*



%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.10.0-2mdv2011.0
+ Revision: 680823
- mass rebuild

* Wed Jul 08 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 393666
- update to 1.01
- using %%perl_convert_version
- fixed summary, license & description fields

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.009-3mdv2009.0
+ Revision: 256026
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.009-1mdv2008.1
+ Revision: 136684
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.009-1mdv2008.0
+ Revision: 67610
- use %%mkrel


* Wed Jun 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.009-1mdk
- 1.009
- update docs
- fix perms

- use %%makeinstall_std macro

* Wed Jan 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.006-3mdk
- remove perl(Class::MakeMethods::Template::Array) dependency

* Tue May 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.006-2mdk
- fix install

* Thu May 15 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.006-1mdk
- from Peter Chen <petechen@netilla.com> :
	- Initial packaging.

