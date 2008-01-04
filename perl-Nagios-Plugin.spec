#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Nagios
%define	pnam	Plugin
Summary:	Nagios::Plugin - A family of perl modules to streamline writing Nagios plugins
Name:		perl-Nagios-Plugin
Version:	0.23
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/T/TO/TONVOON/Nagios-Plugin-%{version}.tar.gz
# Source0-md5:	7eb466f122ea83788506d78d7bf2c402
URL:		http://search.cpan.org/dist/Nagios-Plugin/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Config::Tiny)
BuildRequires:	perl(Math::Calc::Units)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::More) >= 0.62
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nagios::Plugin and its associated Nagios::Plugin::* modules are a
family of Perl modules to streamline writing Nagios plugins. The main
end user modules are Nagios::Plugin, providing an object-oriented
interface to the entire Nagios::Plugin::* collection, and
Nagios::Plugin::Functions, providing a simpler functional interface to
a useful subset of the available functionality.

The purpose of the collection is to make it as simple as possible for
developers to create plugins that conform the Nagios Plugin guidelines
<http://nagiosplug.sourceforge.net/developer-guidelines.html>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Nagios/*.pm
%{perl_vendorlib}/Nagios/Plugin
%{_mandir}/man3/*
