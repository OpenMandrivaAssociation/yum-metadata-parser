Name:       yum-metadata-parser
Version:    1.1.4
Release:    %mkrel 3
Summary:    A fast metadata parser for yum
License:    GPL
Group:      System/Configuration/Packaging
URL:        http://devel.linux.duke.edu/cgi-bin/viewcvs.cgi/yum-metadata-parser/
Source0:    http://linux.duke.edu/projects/yum/download/yum-metadata-parser/%{name}-%{version}.tar.gz
Requires:       yum >= 2.6.2
BuildRequires:  python-devel
BuildRequires:  glib2-devel
BuildRequires:  libxml2-devel
BuildRequires:  sqlite3-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Fast metadata parser for yum implemented in C.

%prep
%setup -q

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
%{python_sitearch}/yum_metadata_parser-*.egg-info


%changelog
* Tue Dec 07 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.1.4-3mdv2011.0
+ Revision: 614426
- rebuild for python 2.7

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Wed Jan 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.4-1mdv2010.1
+ Revision: 490763
- update to new version 1.1.4

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 1.1.2-6mdv2010.0
+ Revision: 446314
- rebuild

* Thu Dec 25 2008 Michael Scherer <misc@mandriva.org> 1.1.2-5mdv2009.1
+ Revision: 318499
- rebuild for new python

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 1.1.2-4mdv2009.0
+ Revision: 262976
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 1.1.2-3mdv2009.0
+ Revision: 262813
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.2-1mdv2008.1
+ Revision: 115434
- import yum-metadata-parser


* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.2-1mdv2008.1
- first mdv release
