#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx themes for Pylons Project documentation
Summary(pl.UTF-8):	Motywy Sphinksa do dokumentacji z projektu Pylons
Name:		python-pylons-sphinx-themes
Version:	1.0.6
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pylons-sphinx-themes/
Source0:	https://files.pythonhosted.org/packages/source/p/pylons-sphinx-themes/pylons-sphinx-themes-%{version}.tar.gz
# Source0-md5:	4585a8032eee440fa1d89f9cf945b58b
URL:		https://pylonsproject.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Sphinx themes for Pylons related projects.

%description -l pl.UTF-8
Ten pakiet zawiera motywy Sphinksa dla projektów powiązanych z Pylons.

%package -n python3-pylons-sphinx-themes
Summary:	Sphinx themes for Pylons Project documentation
Summary(pl.UTF-8):	Motywy Sphinksa do dokumentacji z projektu Pylons
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pylons-sphinx-themes
This package contains Sphinx themes for Pylons related projects.

%description -n python3-pylons-sphinx-themes -l pl.UTF-8
Ten pakiet zawiera motywy Sphinksa dla projektów powiązanych z Pylons.

%prep
%setup -q -n pylons-sphinx-themes-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt CONTRIBUTORS.txt COPYRIGHT.txt LICENSE.txt README.md
%{py_sitescriptdir}/pylons_sphinx_themes
%{py_sitescriptdir}/pylons_sphinx_themes-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pylons-sphinx-themes
%defattr(644,root,root,755)
%doc CHANGES.txt CONTRIBUTORS.txt COPYRIGHT.txt LICENSE.txt README.md
%{py3_sitescriptdir}/pylons_sphinx_themes
%{py3_sitescriptdir}/pylons_sphinx_themes-%{version}-py*.egg-info
%endif
