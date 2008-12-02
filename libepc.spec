%define name libepc
%define version 0.3.8
%define release %mkrel 3
%define api 1.0
%define major 2
%define libname %mklibname epc %api %major
%define develname %mklibname -d epc

Summary: Easy Publish and Consume library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgnutls-devel
BuildRequires: libsoup-devel
BuildRequires: avahi-client-devel avahi-glib-devel
BuildRequires: libext2fs-devel
BuildRequires: avahi-ui-devel
BuildRequires: glib2-devel >= 2.15
BuildRequires: intltool

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
Requires: %{name}-i18n >= %version

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

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/libepc*.a
%find_lang %name

%check
#gw make check needs a running avahi daemon
#make check

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files i18n -f %name.lang
%defattr(-,root,root)

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




