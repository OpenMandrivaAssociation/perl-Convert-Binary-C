%define upstream_name	 Convert-Binary-C
%define upstream_version 0.76

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Convert::Binary::C is a preprocessor and parser for C type definitions. 
It is highly configurable and supports arbitrarily complex data structures. 
Its object-oriented interface has pack and unpack methods that act as 
replacements for Perl's pack and unpack and allow to use C types instead 
of a string representation of the data structure for conversion of binary 
data from and to Perl's complex data structures.

Actually, what Convert::Binary::C does is not very different from what a 
C compiler does, just that it doesn't compile the source code into an object 
file or executable, but only parses the code and allows Perl to use the 
enumerations, structs, unions and typedefs that have been defined within 
your C source for binary data conversion, similar to Perl's pack and unpack.

Beyond that, the module offers a lot of convenience methods to retrieve 
information about the C types that have been parsed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/*
%doc Changes README
%{perl_vendorlib}/
%{_mandir}/*/*


%changelog
* Tue Jan 24 2012 Stéphane Téletchéa <steletch@mandriva.org> 0.760.0-2
+ Revision: 768076
- Convert to new rpm numbering scheme
- Rebuild for new perl

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.760.0-1
+ Revision: 654001
- update to new version 0.76

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.740.0-2mdv2011.0
+ Revision: 555701
- rebuild

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.740.0-1mdv2010.0
+ Revision: 409024
- rebuild using %%perl_convert_version

* Tue May 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.74-1mdv2010.0
+ Revision: 372090
- update to new version 0.74

* Fri Mar 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.73-1mdv2009.1
+ Revision: 359033
- update to new version 0.73

* Mon Mar 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.72-1mdv2009.1
+ Revision: 355675
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.71-2mdv2009.0
+ Revision: 268402
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 22 2008 Stéphane Téletchéa <steletch@mandriva.org> 0.71-1mdv2009.0
+ Revision: 196673
-Added missing BuildRequires
- import perl-Convert-Binary-C


* Tue Apr 22 2008 0.71-1mdv2008.1 Stephane Teletchea <steletch@mandriva.org>
- Initial package
