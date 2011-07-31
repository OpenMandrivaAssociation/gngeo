%define name gngeo
%define longname GnGeo
%define version 0.7
%define release %mkrel 2

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
Group: Emulators
License: GPLv2
URL: http://m.peponas.free.fr/gngeo/
BuildRoot: %{_tmppath}/%{name}-build

%description
GnGeo is a NeoGeo emulator for Linux (and maybe some other UNIX).
It needs NeoGeo Bios and roms that you must of course own to play with.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x \
%ifarch %{ix86}
	--enable-i386asm
%else
	--disable-i386asm
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README sample_gngeorc
%attr(0755,root,games) %{_bindir}/%{name}
%dir %attr(0755,root,games) %{_datadir}/%{name}
%{_datadir}/%{name}/romrc
%{_datadir}/%{name}/romrc.d
%{_datadir}/%{name}/cursor.bmp
%{_datadir}/%{name}/gui_font.bmp
%{_datadir}/%{name}/gui_font2.bmp
%{_datadir}/%{name}/little_font.bmp
%{_datadir}/%{name}/sb_arrows.bmp
%{_mandir}/man1/gngeo.1.*

%clean
rm -rf %{buildroot}
