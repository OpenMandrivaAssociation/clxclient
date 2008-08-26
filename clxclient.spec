%define	major	3
%define	libname	%mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Name:          clxclient
Summary:       Clxclient C++ libraries
Version:       3.3.1
Release:       %mkrel 4
License:       LGPLv2+
Group:	       System/Libraries 
Source0:       %{name}-%{version}.tar.bz2
Patch0:        clxclient-3.3.1-fix-install.patch
URL: 	       http://users.skynet.be/solaris/linuxaudio/getit.html
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

%make

%install
make DESTDIR=%buildroot  install

%clean

