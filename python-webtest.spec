%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-webtest
Version:        1.2
Release:        2%{?dist}
Summary:        Helper to test WSGI applications

Group:          Development/Languages
License:        MIT
URL:            http://pythonpaste.org/webtest/
Source0:        http://pypi.python.org/packages/source/W/WebTest/WebTest-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch
BuildRequires:  python-setuptools-devel
BuildRequires:  python-nose
BuildRequires:  python-webob
Requires:       python-webob

%description
WebTest wraps any WSGI application and makes it easy to send test
requests to that application, without starting up an HTTP server.

This provides convenient full-stack testing of applications written
with any WSGI-compatible framework.

%prep
%setup -q -n WebTest-%{version}


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

 
%clean
%{__rm} -rf %{buildroot}


%check
./test


%files
%defattr(-,root,root,-)
%doc docs/*
%{python_sitelib}/webtest
%{python_sitelib}/*.egg-info


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Luke Macken <lmacken@redhat.com> - 1.2-1
- Update to 1.2

* Tue Apr 14 2009 Ricky Zhou <ricky@fedoraproject.org> - 1.1-3
- Change define to global.
- Remove old >= 8 conditional.
- Remove unnecessary BuildRequires on python-devel.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 06 2008 Ricky Zhou <ricky@fedoraproject.org> - 1.1-1
- Upstream released new version.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0-4
- Rebuild for Python 2.6

* Thu Jul 17 2008 Ricky Zhou <ricky@fedoraproject.org> - 1.0-3
- Update Requires for python-webob rename.
- Add BuildRequires on python-webob for tests.

* Sat Jul 07 2008 Ricky Zhou <ricky@fedoraproject.org> - 1.0-2
- Add %%check section.

* Sat Jun 14 2008 Ricky Zhou <ricky@fedoraproject.org> - 1.0-1
- Initial RPM Package.
