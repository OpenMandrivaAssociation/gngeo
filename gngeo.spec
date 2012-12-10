%define name gngeo
%define longname GnGeo
%define version 0.8
%define release %mkrel 1

Summary: %{longname} - Neo Geo Emulator
Summary(fr): %{longname} - Emulateur Neo Geo
Name: %{name}
Version: %{version}
Release: %{release}
BuildRequires: SDL-devel 
BuildRequires: SDL_image-devel 
BuildRequires: nasm 
BuildRequires: zlib-devel
%if %mdkversion >= 200700
BuildRequires: mesaglu-devel
%else
BuildRequires: MesaGLU-devel
%endif

Source0: http://m.peponas.free.fr/gngeo/download/%{name}-%{version}.tar.bz2
Patch0: gngeo-mkstate.patch
Group: Emulators
License: GPLv2
URL: http://m.peponas.free.fr/gngeo/
BuildRoot: %{_tmppath}/%{name}-build

%description
GnGeo is a NeoGeo emulator for Linux (and maybe some other UNIX).
It needs NeoGeo Bios and roms that you must of course own to play with.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%configure2_5x \
%ifarch %{ix86}
	--enable-i386asm
%else
	--disable-i386asm
%endif

make -j1

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README sample_gngeorc
%attr(0755,root,games) %{_bindir}/%{name}
%dir %attr(0755,root,games) %{_datadir}/%{name}
%{_mandir}/man1/gngeo.1.*
%{_datadir}/%{name}/gngeo_data.zip

%clean
rm -rf %{buildroot}



%changelog
* Fri May 04 2012 Zombie Ryushu <ryushu@mandriva.org> 0.8-1mdv2011.0
+ Revision: 796259
- install stage issues
- install stage issues
- dumb makefile mistake
- fix mkstate patch
- apply mkstate patch
- mecurial fixes
- Upgrade to 0.8

* Sun Jul 31 2011 Andrey Bondrov <abondrov@mandriva.org> 0.7-3
+ Revision: 692516
- Try to fix x86_64 build
- imported package gngeo


* Sat Jul 23 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.7-2mdv2011.0
- Import from PLF
- Remove PLF reference

* Fri Sep 01 2006 Guillaume Bedot <littletux@zarb.org> 0.7-1plf2007.0
- 0.7 (with new romrc.d directory)

* Thu Aug 31 2006 Anssi Hannula <anssi@zarb.org> 0.6.12-4plf2007.0
- fix buildrequires

* Thu Jul 20 2006 Guillaume Bedot <littletux@zarb.org> 0.6.12-3plf2007.0
- NEWS was file empty in gngb not gngeo

* Thu Jul 20 2006 Guillaume Bedot <littletux@zarb.org> 0.6.12-2plf2007.0
- dropped empty NEWS file
- fixed glu buildrequire
- clean short-circuit install

* Thu Jun 15 2006 Guillaume Bedot <littletux@zarb.org> 0.6.12-1plf2007.0
- 0.6.12
- standard mkrel
- buildrequires

* Sun Apr 09 2006 Guillaume Bedot <littletux@zarb.org> 0.6.11-1plf
- Release 0.6.11
- Dropped patch from previous version (applied upstream:)

* Thu Mar 16 2006 Guillaume Bedot <littletux@zarb.org> 0.6.10-2plf
- Patch to fix blitter and effect help, this also fixes xgngeo config issue.
 Thanks to Alexandre Bedot to the bug report !

* Mon Mar 13 2006 Guillaume Bedot <littletux@zarb.org> 0.6.10-1plf
- New release 0.6.10

* Wed Feb 22 2006 Guillaume Bedot <littletux@zarb.org> 0.6.9.1plf
- New release

* Thu Jan 19 2006 Guillaume Bedot <littletux@zarb.org> 0.6.7-1plf
- New release, dropped already applied patches 

* Wed Oct 19 2005 Anssi Hannula <anssi@zarb.org> 0.6.5-0.beta2.2plf
- disable i386asm on non-x86 arches
- fix non-i386asm build (patch1)
- quiet %%setup

* Sun Jul 17 2005 Guillaume Bedot <littletux@zarb.org> 0.6.5-0.beta2.1plf
- New release 0.6.5 beta2
- patch to allow gcc4 build
- use mkrel

* Mon Oct 04 2004 Guillaume Bedot <littletux@zarb.org> 0.6.4-1plf
- New release 0.6.4

* Tue Aug 31 2004 Guillaume Bedot <littletux@zarb.org> 0.6.3-1plf
- Release 0.6.3

* Mon Apr 26 2004 Guillaume Bedot <littletux@zarb.org> 0.6.2-2plf
- fixed buildrequires and removed (wrong) requires

* Mon Apr 19 2004 Guillaume Bedot <littletux@zarb.org> 0.6.2-1plf
- Update to 0.6.2
- reason for a plf package 

* Sun Jul 20 2003 Guillaume Bedot <guillaume.bedot@wanadoo.fr> 0.5.9a-1plf
- 0.5.9a and Build / License fixes thanks to Michael Sherer aka misc.

* Wed May 21 2003 Guillaume Bedot <guillaume.bedot@wanadoo.fr> 0.5.9-1plf
- First package
