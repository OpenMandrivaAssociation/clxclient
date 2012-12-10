%define	major	3
%define	libname	%mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Name:          clxclient
Summary:       Clxclient C++ libraries
Version:       3.6.1
Release:       %mkrel 2
License:       LGPLv2+
Group:	       System/Libraries 
Source0:       http://www.kokkinizita.net/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Patch0:        clxclient-3.6.1-linkage.patch
URL: 	       http://www.kokkinizita.net/linuxaudio/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: clthreads-devel
BuildRequires: x11-proto-devel
BuildRequires: libxft-devel

%description
Clthreads C++ libraries

#--------------------------------------------------------------------

%package -n	%{libname}
Group: 		System/Libraries
Summary: 	Libraries for %{name}
Provides: 	lib%{name} = %{version}-%{release}

%description 
Clxclient C++ libraries

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%_libdir/libclxclient.so.%{major}*

#--------------------------------------------------------------------

%description -n	%{libname}
The libraries from %name package

%package -n	%{develname}
Group: 		Development/Other
Summary: 	Libraries for %name
Requires:	%{libname} = %{version}-%{release}
Provides: 	%{name}-devel = %{version}-%{release}
Obsoletes: 	%{libname}-devel

%description -n	%{develname}
Development libraries from %name

%files -n %{develname}
%defattr (-,root,root)
%_includedir/clxclient.h
%_libdir/libclxclient.so

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p0

%build
%make LDFLAGS="%{ldflags}"

%install
rm -fr %buildroot
mkdir -p %buildroot%_includedir
make install PREFIX=%{buildroot}%{_prefix}

%clean
rm -fr %buildroot


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 3.6.1-2mdv2011.0
+ Revision: 617071
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Funda Wang <fwang@mandriva.org> 3.6.1-1mdv2010.0
+ Revision: 433028
- New version 3.6.1

* Fri Jun 12 2009 Jérôme Brenier <incubusss@mandriva.org> 3.3.1-5mdv2010.0
+ Revision: 385600
- rebuild

* Tue Aug 26 2008 Emmanuel Andry <eandry@mandriva.org> 3.3.1-4mdv2009.0
+ Revision: 276157
- apply devel policy
- fix license

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 3.3.1-3mdv2009.0
+ Revision: 243551
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Dec 09 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.3.1-1mdv2008.1
+ Revision: 116579
- Fix BuildRequires
- import clxclient


