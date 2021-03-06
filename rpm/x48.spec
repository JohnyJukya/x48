Summary:   	x48 is an HP 48 GX emulator
Name:      	x48
Version:   	0.6.4
Release:  	1
License:	GPL
Group:     	Applications/Math
URL:            http://developer.berlios.de/projects/x48/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
Requires:  	libX11  libXext  readline
BuildRequires:  autoconf libX11-devel libXext-devel readline-devel
BuildRequires:  libXt-devel

Source:         http://download.berlios.de/x48/%{name}-%{version}.tar.gz

%description
 This is an emulator of the HP 48 SX and GX calculator.
 Romdumps are available from http://x48.berlios.de/

%define x11_app_defaults_dir %(pkg-config --variable appdefaultdir xt)

%prep
%setup -q

%build
%configure \
	--prefix=/usr
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root,-)
%doc	README
%{_bindir}/x48
%{_bindir}/dump2rom
%{_bindir}/checkrom
%{_bindir}/mkcard
%{_mandir}/man1/*
%{x11_app_defaults_dir}/X48


