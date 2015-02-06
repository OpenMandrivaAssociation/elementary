%define major   1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Basic widget set based on EFL for mobile touch-screen devices
Name:		elementary
Version:	1.10.2
Release:	2
License:	LGPLv2.1+
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.fr/releases/%{name}-%{version}.tar.bz2
BuildRequires:	doxygen
BuildRequires:	gettext-devel
BuildRequires:	edje
BuildRequires:	eet
BuildRequires:	embryo
BuildRequires:	eolian
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(ecore-con)
BuildRequires:	pkgconfig(ecore-evas)
BuildRequires:	pkgconfig(ecore-file)
BuildRequires:	pkgconfig(ecore-imf)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(efreet)
BuildRequires:	pkgconfig(efreet-mime)
BuildRequires:	pkgconfig(efreet-trash)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(eio)
BuildRequires:	pkgconfig(eldbus)
BuildRequires:	pkgconfig(eo)
BuildRequires:	pkgconfig(eolian)
BuildRequires:	pkgconfig(evas)
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
%{_bindir}/elementary_run
%{_bindir}/elementary_codegen
%{_bindir}/elementary_config
%{_bindir}/elementary_quicklaunch
%{_bindir}/elm_prefs_cc
%{_libdir}/edje/modules/elm/v-*/module.so
%{_libdir}/elementary/modules/access_output/v-*
%{_libdir}/elementary/modules/datetime_input_ctxpopup/v-*
%{_libdir}/elementary/modules/prefs/v-*
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
%{_libdir}/libelementary.so.%{major}*

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
%dir %{_libdir}/cmake/Elementary
%{_libdir}/cmake/Elementary/*.cmake
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libelementary.so
%{_libdir}/elementary/modules/test_entry/v-*
%{_libdir}/elementary/modules/test_map/v-*
%{_datadir}/applications/%{name}_test.desktop
%dir %{_datadir}/eolian/include/elementary-1
%{_datadir}/eolian/include/elementary-1/*
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

