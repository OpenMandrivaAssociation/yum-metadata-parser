Name:       yum-metadata-parser
Version:    1.1.4
Release:    6
Summary:    A fast metadata parser for yum
License:    GPL
Group:      System/Configuration/Packaging
URL:        https://devel.linux.duke.edu/cgi-bin/viewcvs.cgi/yum-metadata-parser/
Source0:    http://linux.duke.edu/projects/yum/download/yum-metadata-parser/%{name}-%{version}.tar.gz
Requires:       yum >= 2.6.2
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  libxml2-devel
BuildRequires:  sqlite3-devel

%description
Fast metadata parser for yum implemented in C.

%prep
%setup -q

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --root=%{buildroot}


%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%{python2_sitearch}/_sqlitecache.so
%{python2_sitearch}/sqlitecachec.py
%{python2_sitearch}/yum_metadata_parser-*.egg-info

