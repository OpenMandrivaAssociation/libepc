%define api 1.0
%define major 3
%define libname %mklibname epc %{api} %{major}
%define libnameui %mklibname epc-ui %{api} %{major}
%define devname %mklibname -d epc
%define devnameui %mklibname -d epc-ui

%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	Easy Publish and Consume library
Name:		libepc
Version:	0.4.6
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(avahi-ui) >= 0.6
BuildRequires:	pkgconfig(avahi-ui-gtk3) >= 0.6
BuildRequires:	pkgconfig(gnutls) >= 1.4
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.10
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(uuid) >= 1.36

%description
The Easy Publish and Consume library provides an easy method to:

* publish data per HTTPS
* announce that information via DNS-SD
* find that information
* and finally consume it

You can use this library as key/value store published to the network,
using encryption, authentication and service discovery.

%package i18n
Summary:	Easy Publish and Consume library
Group:		System/Libraries
BuildArch:	noarch

%description i18n
This package contains the translations for %{name}.

%package -n %{libname}
Group:		System/Libraries
Summary:	Easy Publish and Consume library

%description -n %{libname}
The Easy Publish and Consume library provides an easy method to:

* publish data per HTTPS
* announce that information via DNS-SD
* find that information
* and finally consume it

You can use this library as key/value store published to the network,
using encryption, authentication and service discovery.

%package -n %{libnameui}
Group:		System/Libraries
Summary:	Easy Publish and Consume library

%description -n %{libnameui}
Libraries for %{name}-ui

%package -n %{devname}
Group:		Development/C
Summary:	Easy Publish and Consume library
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name} development headers and libraries.

%package -n %{devnameui}
Group:		Development/C
Summary:	Easy Publish and Consume library
Requires:	%{libnameui} = %{version}-%{release}

%description -n %{devnameui}
%{name}-ui development headers and libraries.

%prep
%setup -q

%build
%configure \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%check
#gw make check needs a running avahi daemon
#make check

%files i18n -f %{name}.lang

%files -n %{libname}
%{_libdir}/libepc-%{api}.so.%{major}*

%files -n %libnameui
%{_libdir}/libepc-ui-%{api}.so.%{major}*

%files -n %{devname}
%doc NEWS ChangeLog AUTHORS README
%{_includedir}/libepc-%{api}
%{_libdir}/libepc-%{api}.so
%{_libdir}/pkgconfig/libepc-%{api}.pc
%{_datadir}/gtk-doc/html/libepc-%{api}

%files -n %{devnameui}
%{_includedir}/libepc-ui-%{api}
%{_libdir}/libepc-ui-%{api}.so
%{_libdir}/pkgconfig/libepc-ui-%{api}.pc

