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


#% define svndate	20120103
#% define svnrev	66796

%define	major	1
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Name:		elementary
Version:	1.7.3
Release:	1
Summary:	Basic widget set based on EFL for mobile touch-screen devices
Group:		Graphical desktop/Enlightenment
License:	BSD
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz

BuildRequires:	doxygen
BuildRequires:	gettext-devel
BuildRequires:	edje
BuildRequires:	eet
BuildRequires:	embryo
BuildRequires:	pkgconfig(ecore) >= 1.7.1
BuildRequires:	pkgconfig(ecore-con) >= 1.7.1
BuildRequires:	pkgconfig(ecore-evas) >= 1.7.1
BuildRequires:	pkgconfig(ecore-file) >= 1.7.1
BuildRequires:	pkgconfig(ecore-imf) >= 1.7.1
BuildRequires:	pkgconfig(edbus) >= 1.7.1
BuildRequires:	pkgconfig(edje) >= 1.7.1
BuildRequires:	pkgconfig(eet) >= 1.7.1
BuildRequires:	pkgconfig(eina) >= 1.7.1
BuildRequires:	pkgconfig(eio) >= 1.7.1
BuildRequires:	pkgconfig(efreet) >= 1.7.1
BuildRequires:	pkgconfig(efreet-mime) >= 1.7.1
BuildRequires:	pkgconfig(efreet-trash) >= 1.7.1
BuildRequires:	pkgconfig(evas) >= 1.7.1
BuildRequires:	pkgconfig(edje) >= 1.7.1
BuildRequires:	evas_generic_loaders

# Extra stuff
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(ethumb_client)
#BuildRequires:	pkgconfig(eweather)

%description
A basic widget set that is easy to use based on EFL for mobile
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
Requires:	pkgconfig(eweather)
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries.

%prep
%setup -q

%build
#NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static
make

%install
%makeinstall_std

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
%{_libdir}/elementary/modules/datetime_input_ctxpopup/linux*
%{_datadir}/applications/%{name}_test.desktop
%{_includedir}/%{name}*

