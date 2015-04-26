%define major   1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Basic widget set based on EFL for mobile touch-screen devices
Name:		elementary
Version:	1.13.2
Release:	1
License:	LGPLv2.1+
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/libs/%{name}/%{name}-%{version}.tar.xz
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
BuildRequires:	pkgconfig(eldbus) >= 1.8.0
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
BuildRequires:	pkgconfig(libsystemd-journal)
BuildRequires:	pkgconfig(libsystemd-daemon)
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
%{_bindir}/elementary_codegen
%{_bindir}/elementary_config
%{_bindir}/elementary_quicklaunch
%{_bindir}/elm_prefs_cc
%{_libdir}/edje/modules/elm/v*/module.so
%{_libdir}/elementary/modules/access_output/v*
%{_libdir}/elementary/modules/prefs/v*
%{_datadir}/applications/%{name}_config.desktop
%{_datadir}/%{name}/config/*
%{_datadir}/%{name}/edje_externals/*
%{_datadir}/%{name}/images/*
%{_datadir}/%{name}/themes/default.edj
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
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
%{name} development headers and libraries.

%files -n %{devname}
%{_bindir}/elementary_test
%{_libdir}/cmake/Elementary/
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/elementary/modules/test_entry/v*
%{_libdir}/elementary/modules/test_map/v*
%{_libdir}/elementary/modules/datetime_input_ctxpopup/v*
%{_datadir}/applications/%{name}_test.desktop
%{_datadir}/eolian/include/elementary-1/*.eo
%{_includedir}/%{name}*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure \
	--disable-static
make all

%install
%makeinstall_std

%find_lang %{name}

