%define	name	elementary
%define version 0.1.0.0
%define release %mkrel 2

%define major	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Basic widget set that is easy to use based on EFL for mobile touch-screen devices
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	http://download.enlightenment.org/snapshots/TMP/st/%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	edje-devel >= 0.9.9.050, edje >= 0.9.9.050
BuildRequires:	e_dbus-devel
buildrequires:	embryo >= 0.9.9.050

%description
a basic widget set that is easy to use based on EFL for mobile
touch-screen devices

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/%{name}_run
%{_bindir}/elementary_quicklaunch
%{_bindir}/elementary_testql
%{_bindir}/elementary_test
%{_datadir}/applications/%{name}_test.desktop
%{_datadir}/%name/images/*
%{_datadir}/%name/themes/default.edj
%{_datadir}/%name/objects/test.edj
%{_iconsdir}/%name.png

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/%name/*.h
%{_includedir}/Elementary.h



