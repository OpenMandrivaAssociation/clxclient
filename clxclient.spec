# empty debug
%define debug_package %{nil}

%define major 3
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Clxclient C++ libraries
Name:		clxclient
Version:	3.9.0
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.kokkinizita.net/linuxaudio/
Source0:	http://www.kokkinizita.net/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Patch0:		clxclient-3.9.0.patch
BuildRequires:	clthreads-devel
BuildRequires:	x11-proto-devel
BuildRequires:	pkgconfig(xft)

%description
Clthreads C++ libraries

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
The libraries from %{name} package

%files -n %{libname}
%doc COPYING AUTHORS
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development libraries from %{name}.

%files -n %{devname}
%doc COPYING AUTHORS
%{_includedir}/clxclient.h
%{_libdir}/libclxclient.so

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
%make LDFLAGS="%{ldflags}"

%install
mkdir -p %{buildroot}%{_includedir}
make install PREFIX=%{buildroot}%{_prefix}

