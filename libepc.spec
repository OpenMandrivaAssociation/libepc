%define api 1.0
%define major 3
%define libname %mklibname epc %{api} %{major}
%define libnameui %mklibname epc-ui %{api} %{major}
%define develname %mklibname -d epc
%define develnameui %mklibname -d epc-ui

Summary:	Easy Publish and Consume library
Name:		libepc
Version:	0.4.4
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz


BuildRequires:	intltool
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(avahi-ui) >= 0.6
BuildRequires:	pkgconfig(gnutls) >= 1.4
BuildRequires:	pkgconfig(avahi-ui-gtk3) >= 0.6
BuildRequires:	pkgconfig(uuid) >= 1.36
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.10

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

%description i18n
The Easy Publish and Consume library provides an easy method to:

* publish data per HTTPS
* announce that information via DNS-SD
* find that information
* and finally consume it

You can use this library as key/value store published to the network,
using encryption, authentication and service discovery.

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

%package -n %{develname}
Group:		Development/C
Summary:	Easy Publish and Consume library
Requires:	%{libname} = %{version}-%{release}
Provides:	libepc-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries.

%package -n %{develnameui}
Group:		Development/C
Summary:	Easy Publish and Consume library
Requires:	%{libnameui} = %{version}-%{release}

%description -n %{develnameui}
%{name}-ui development headers and libraries.

%prep
%setup -q

%build
%configure2_5x \
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


%changelog
* Sun Feb 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.4-1
+ Revision: 771304
- version update 0.4.4

* Tue Nov 29 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.4.3-1
+ Revision: 735269
- fixed typoes for api and libnameui
- new version 0.4.3
- split out ui lib and devel pkgs
- cleaned up spec
- removed clean section
- removed old ldconfig scriptlets
- removed .la files
- disabled static build
- removed mkrel & BuildRoot
- converted BRs to pkgconfig provides
- removed defattr

* Thu Sep 22 2011 Götz Waschk <waschk@mandriva.org> 0.3.11-4
+ Revision: 700861
- rebuild

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.11-3
+ Revision: 660244
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.11-2mdv2011.0
+ Revision: 602540
- rebuild

* Tue Mar 23 2010 Götz Waschk <waschk@mandriva.org> 0.3.11-1mdv2010.1
+ Revision: 526803
- update to new version 0.3.11

* Sat Jan 02 2010 Götz Waschk <waschk@mandriva.org> 0.3.10-2mdv2010.1
+ Revision: 485007
- fix build deps

* Sat May 23 2009 Götz Waschk <waschk@mandriva.org> 0.3.10-1mdv2010.0
+ Revision: 378924
- update to new version 0.3.10

* Sun Feb 08 2009 Götz Waschk <waschk@mandriva.org> 0.3.9-1mdv2009.1
+ Revision: 338533
- update to new version 0.3.9

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 0.3.8-3mdv2009.1
+ Revision: 309152
- rebuild to get rid of libtasn1 dep

* Sat Nov 08 2008 Götz Waschk <waschk@mandriva.org> 0.3.8-2mdv2009.1
+ Revision: 301104
- rebuild for new libxcb

* Tue Oct 21 2008 Götz Waschk <waschk@mandriva.org> 0.3.8-1mdv2009.1
+ Revision: 295993
- new version
- new major

* Sun Oct 19 2008 Götz Waschk <waschk@mandriva.org> 0.3.7-1mdv2009.1
+ Revision: 295243
- new version
- remove build workaround

* Fri Oct 17 2008 Götz Waschk <waschk@mandriva.org> 0.3.6-1mdv2009.1
+ Revision: 294596
- fix build deps
- new version
- enable parallel build
- fix linking

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 0.3.5-1mdv2009.0
+ Revision: 192482
- new version

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 0.3.4-2mdv2008.1
+ Revision: 166151
- libsoup rebuild

* Tue Jan 29 2008 Götz Waschk <waschk@mandriva.org> 0.3.4-1mdv2008.1
+ Revision: 159662
- fix buildrequires
- new version
- add translations

* Tue Jan 15 2008 Götz Waschk <waschk@mandriva.org> 0.3.3-1mdv2008.1
+ Revision: 152140
- new version
- new major

* Mon Jan 14 2008 Götz Waschk <waschk@mandriva.org> 0.3.2-1mdv2008.1
+ Revision: 151887
- new version
- drop patch
- new major

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 21 2007 Götz Waschk <waschk@mandriva.org> 0.3.1-2mdv2008.1
+ Revision: 136203
- fix build with glib 2.15

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 17 2007 Götz Waschk <waschk@mandriva.org> 0.3.1-1mdv2008.1
+ Revision: 121673
- new version

* Thu Dec 06 2007 Götz Waschk <waschk@mandriva.org> 0.3.0-3mdv2008.1
+ Revision: 115879
- bump release
- bump release
- import libepc

