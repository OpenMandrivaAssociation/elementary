%define major   1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Basic widget set based on EFL for mobile touch-screen devices
Name:		elementary
Version:	1.8.2
Release:	1
License:	LGPLv2.1+
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/libs/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	doxygen
BuildRequires:	gettext-devel
BuildRequires:	edje
BuildRequires:	eet
BuildRequires:	embryo
BuildRequires:	pkgconfig(ecore) >= 1.8.0
BuildRequires:	pkgconfig(ecore-con) >= 1.8.0
BuildRequires:	pkgconfig(ecore-evas) >= 1.8.0
BuildRequires:	pkgconfig(ecore-file) >= 1.8.0
BuildRequires:	pkgconfig(ecore-imf) >= 1.8.0
BuildRequires:	pkgconfig(ecore-input) >= 1.8.0
BuildRequires:	pkgconfig(edbus) >= 1.8.0
BuildRequires:	pkgconfig(edje) >= 1.8.0
BuildRequires:	pkgconfig(eet) >= 1.8.0
BuildRequires:	pkgconfig(efreet) >= 1.8.0
BuildRequires:	pkgconfig(efreet-mime) >= 1.8.0
BuildRequires:	pkgconfig(efreet-trash) >= 1.8.0
BuildRequires:	pkgconfig(eina) >= 1.8.0
BuildRequires:	pkgconfig(eio) >= 1.8.0
BuildRequires:	pkgconfig(eldbus) >= 1.8.0
BuildRequires:	pkgconfig(eo) >= 1.8.0
BuildRequires:	pkgconfig(evas) >= 1.8.0
BuildRequires:	evas_generic_loaders

# Extra stuff
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(ethumb_client)
#BuildRequires:	pkgconfig(eweather)

%description
A basic widget set that is easy to use based on EFL for mobile
touch-screen devices.

This package is part of the Enlightenment DR17 desktop shell.

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

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for the %{name} package
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}.

%files -n %{libname}
%{_libdir}/*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Requires:	pkgconfig(eweather)
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
%{name} development headers and libraries.

%files -n %{devname}
%{_bindir}/elementary_testql
%{_bindir}/elementary_test
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/elementary/modules/test_entry/linux*
%{_libdir}/elementary/modules/test_map/linux*
%{_libdir}/elementary/modules/datetime_input_ctxpopup/linux*
%{_datadir}/applications/%{name}_test.desktop
%{_includedir}/%{name}*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%find_lang %{name}

