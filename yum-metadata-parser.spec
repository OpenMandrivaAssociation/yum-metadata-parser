Summary: A fast metadata parser for yum
Name: yum-metadata-parser
Version: 1.1.2
Release: %mkrel 1
License: GPL
Group: Development/Libraries
URL: http://devel.linux.duke.edu/cgi-bin/viewcvs.cgi/yum-metadata-parser/
Source0: http://linux.duke.edu/projects/yum/download/yum-metadata-parser/%{name}-%{version}.tar.gz
Requires: yum >= 2.6.2
BuildRequires: python-devel
BuildRequires: glib2-devel
BuildRequires: libxml2-devel
BuildRequires: sqlite-devel
BuildRequires: pkgconfig
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Fast metadata parser for yum implemented in C.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --root=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%{python_sitearch}/_sqlitecache.so
%{python_sitearch}/sqlitecachec.py
%{python_sitearch}/sqlitecachec.pyc
%{python_sitearch}/sqlitecachec.pyo
%{python_sitearch}/yum_metadata_parser-*.egg-info

