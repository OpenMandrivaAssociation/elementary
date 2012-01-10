#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/elementary elementary; \
#cd elementary; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf elementary-$PKG_VERSION.tar.xz elementary/ --exclude .svn --exclude .*ignore


%define svndate	20120103
%define svnrev	66796

%define	major	0
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Name:		elementary
Version:	0.8.0.%{svnrev}
Release:	0.%{svndate}.1
Summary:	Basic widget set based on EFL for mobile touch-screen devices
Group:		Graphical desktop/Enlightenment
License:	BSD
URL:		http://www.enlightenment.org/
Source0: 	%{name}-%{version}.tar.xz

BuildRequires:	edje
BuildRequires:	eet
BuildRequires:	embryo
BuildRequires:	evas
Buildrequires:  gettext-devel
BuildRequires:	pkgconfig(edbus)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(efreet)

%description
a basic widget set that is easy to use based on EFL for mobile
touch-screen devices

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary:	Libraries for the %{name} package
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}

%package -n %{develname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries.

%prep
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/%{name}_run
%{_bindir}/elementary_config
%{_bindir}/elementary_quicklaunch
%{_libdir}/edje/modules/elm/linux-*/module.so
%{_libdir}/elementary/modules/access_output/linux*
%{_datadir}/applications/%{name}_config.desktop
%{_datadir}/%{name}/config/*
%{_datadir}/%{name}/edje_externals/*
%{_datadir}/%{name}/images/*
%{_datadir}/%{name}/themes/default.edj
%{_datadir}/%{name}/themes/default-desktop.edj
%{_datadir}/%{name}/objects/*
%{_iconsdir}/%{name}.png

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_bindir}/elementary_testql
%{_bindir}/elementary_test
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/elementary/modules/test_entry/linux*
%{_libdir}/elementary/modules/test_map/linux*
%{_datadir}/applications/%{name}_test.desktop
%{_includedir}/%{name}*

