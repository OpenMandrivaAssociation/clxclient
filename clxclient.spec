%define	major	3
%define	libname	%mklibname %name %major

Name:          clxclient
Summary:       Clxclient C++ libraries
Version:       3.3.1
Release:       %mkrel 1
License:       GPL
Group:	       System/Libraries 
Source0:       %{name}-%{version}.tar.bz2
Patch0:        clxclient-3.3.1-fix-install.patch
URL: 	       http://users.skynet.be/solaris/linuxaudio/getit.html
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: clthreads-devel

%description
Clthreads C++ libraries

#--------------------------------------------------------------------

%package -n	%libname
Group: 		System/Libraries
Summary: 	Libraries for %name
Provides: 	lib%name = %version-%release

%description 
Clxclient C++ libraries

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%_libdir/libclxclient.so.3
%_libdir/libclxclient.so.3.3.1

#--------------------------------------------------------------------

%description -n	%libname
The libraries from %name package

%package -n	%libname-devel
Group: 		Development/Other
Summary: 	Libraries for %name
Requires:	%libname = %version-%release
Provides:	lib%name-devel = %version-%release
Provides: 	%{name}-devel = %{version}-%{release}

%description -n	%libname-devel
Development libraries from %name

%files -n %libname-devel
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
