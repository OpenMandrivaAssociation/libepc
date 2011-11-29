%define %{api} 1.0
%define major 3
%define libname %mklibname epc %{api} %major
%define libnameui %mklibname epc-ui %{api} %major
%define develname %mklibname -d epc
%define develnameui %mklibname -d epc-ui

Summary: Easy Publish and Consume library
Name: libepc
Version: 0.4.3
Release: 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org/

BuildRequires: intltool
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(avahi-ui) >= 0.6
BuildRequires: pkgconfig(avahi-ui-gtk3) >= 0.6
BuildRequires: pkgconfig(gnutls) >= 1.4
BuildRequires: pkgconfig(uuid) >= 1.36
BuildRequires: pkgconfig(gtk+-2.0) >= 2.10

%description
The Easy Publish and Consume library provides an easy method to:

* publish data per HTTPS
* announce that information via DNS-SD
* find that information
* and finally consume it

You can use this library as key/value store published to the network,
using encryption, authentication and service discovery.

%package i18n
Summary: Easy Publish and Consume library
Group: System/Libraries

%description i18n
The Easy Publish and Consume library provides an easy method to:

* publish data per HTTPS
* announce that information via DNS-SD
* find that information
* and finally consume it

You can use this library as key/value store published to the network,
using encryption, authentication and service discovery.


%package -n %{libname}
Group: System/Libraries
Summary: Easy Publish and Consume library

%description -n %{libname}
The Easy Publish and Consume library provides an easy method to:

* publish data per HTTPS
* announce that information via DNS-SD
* find that information
* and finally consume it

You can use this library as key/value store published to the network,
using encryption, authentication and service discovery.

%package -n %{libnameui}
Group: System/Libraries
Summary: Easy Publish and Consume library

%description -n %{libnameui}
Libraries for %{name}-ui

%package -n %{develname}
Group: Development/C
Summary: Easy Publish and Consume library
Requires: %{libname} = %{version}-%{release}
Provides: libepc-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries.

%package -n %{develnameui}
Group: Development/C
Summary: Easy Publish and Consume library
Requires: %{libnameui} = %{version}-%{release}

%description -n %{develnameui}
%{name}-ui development headers and libraries.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_libdir}/libepc*.la
%find_lang %{name}

%check
#gw make check needs a running avahi daemon
#make check

%files i18n -f %{name}.lang

%files -n %{libname}
%{_libdir}/libepc-%{api}.so.%{major}*

%files -n %libuiname
%{_libdir}/libepc-ui-%{api}.so.%{major}*

%files -n %{develname}
%doc NEWS ChangeLog AUTHORS README
%{_includedir}/libepc-%{api}
%{_libdir}/libepc-%{api}.so
%{_libdir}/pkgconfig/libepc-%{api}.pc
%{_datadir}/gtk-doc/html/libepc-%{api}

%files -n %{develnameui}
%{_includedir}/libepc-ui-%{api}
%{_libdir}/libepc-ui-%{api}.so
%{_libdir}/pkgconfig/libepc-ui-%{api}.pc

