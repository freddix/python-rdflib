%define		module	rdflib

Summary:	Python library for working with RDF
Name:		python-%{module}
Version:	4.1.2
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	https://github.com/RDFLib/rdflib/archive/%{version}.tar.gz
# Source0-md5:	5c284061f1f2a086b0782644afbaac59
URL:		http://www.rdflib.net/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python-isodate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information. The library contains an RDF/XML
parser/serializer, a TripleStore, an InformationStore and various
store backends. It is being developed by Daniel Krech along with the
help of a number of contributors.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%attr(755,root,root) %{_bindir}/csv2rdf
%attr(755,root,root) %{_bindir}/rdf2dot
%attr(755,root,root) %{_bindir}/rdfgraphisomorphism
%attr(755,root,root) %{_bindir}/rdfpipe
%attr(755,root,root) %{_bindir}/rdfs2dot
%{py_sitescriptdir}/rdflib
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info

