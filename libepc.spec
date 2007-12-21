%define name libepc
%define version 0.3.1
%define release %mkrel 2
%define api 1.0
%define major 1
%define libname %mklibname epc %api %major
%define develname %mklibname -d epc

Summary: Easy Publish and Consume library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch: libepc-0.3.1-gio-include.patch
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org/
BuildRequires: libgnutls-devel
BuildRequires: libsoup-devel
BuildRequires: avahi-client-devel avahi-glib-devel
BuildRequires: libext2fs-devel
BuildRequires: avahi-ui-devel
BuildRequires: glib2-devel >= 2.15

%description
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

%package -n %develname
Group: Development/C
Summary: Easy Publish and Consume library
Requires: %libname = %version
Provides: libepc-devel = %version-%release

%description -n %develname
The Easy Publish and Consume library provides an easy method to:

* publish data per HTTPS
* announce that information via DNS-SD
* find that information
* and finally consume it

You can use this library as key/value store published to the network,
using encryption, authentication and service discovery.


%prep
%setup -q
%patch -p1

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/libepc*.a

%check
#gw make check needs a running avahi daemon
#make check

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%doc README
%_libdir/libepc-%api.so.%{major}*
%_libdir/libepc-ui-%api.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc NEWS ChangeLog AUTHORS
%_libdir/libepc-%api.so
%_libdir/libepc-ui-%api.so
%_libdir/libepc-%api.la
%_libdir/libepc-ui-%api.la
%_includedir/libepc-%api
%_includedir/libepc-ui-%api
%_libdir/pkgconfig/libepc-%api.pc
%_libdir/pkgconfig/libepc-ui-%api.pc
%_datadir/gtk-doc/html/libepc-%api




