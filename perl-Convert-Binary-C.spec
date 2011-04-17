%define upstream_name	 Convert-Binary-C
%define upstream_version 0.76

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

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
