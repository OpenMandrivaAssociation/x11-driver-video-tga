%define _disable_ld_no_undefined 1

Summary:	X.org driver for DEC Tga Cards
Name:		x11-driver-video-tga
Version:	1.2.2
Release:	26
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-tga-%{version}.tar.bz2
Patch0:		remove_mibstore_h.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-tga is the X.org driver for DEC Tga Cards.

%prep
%setup -qn xf86-video-tga-%{version}
%autopatch -p1

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/tga_drv.so

