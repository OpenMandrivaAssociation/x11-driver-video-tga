Name: x11-driver-video-tga
Version: 1.2.2
Release: 9
Summary: X.org driver for DEC Tga Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-tga-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-tga is the X.org driver for DEC Tga Cards.

%prep
%setup -qn xf86-video-tga-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/tga_drv.so



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.2-8
+ Revision: 810695
- version update 1.2.2

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.2.1-8
+ Revision: 787285
- Rebuild for x11-server 1.12

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.1-7
+ Revision: 748474
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.1-6
+ Revision: 703757
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.2.1-5
+ Revision: 683589
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-4
+ Revision: 671181
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.1-3mdv2011.0
+ Revision: 595730
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.1-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.1-1mdv2011.0
+ Revision: 584623
- new release

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for 2010.1

* Tue Aug 11 2009 Funda Wang <fwang@mandriva.org> 1.2.0-3mdv2010.0
+ Revision: 414550
- use configure2_5555555555555555555555555555555555555555555555555555555  SPECS/x11-driver-video-tga.spec

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.0-3mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.0-2mdv2009.1
+ Revision: 308263
- rebuild for new X server

* Thu Sep 04 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-1mdv2009.0
+ Revision: 280663
- new release
- rebuild
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-6mdv2008.1
+ Revision: 166143
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-5mdv2008.1
+ Revision: 156623
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-4mdv2008.1
+ Revision: 154791
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-video-tga-1.1.0@mandriva suggested on upstream
  Tag at git checkout e15d5160c3b9466f2ec3b5fc66695f70885fa133
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-3mdv2008.1
+ Revision: 99056
- minor spec cleanup
- build against new xserver (1.4)

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2008.0
+ Revision: 75811
- rebuild

