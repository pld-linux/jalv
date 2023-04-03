Summary:	Simple but fully featured LV2 host for JACK
Summary(pl.UTF-8):	Prosty, ale w pełni funkcjonalny host LV2 dla JACK-a
Name:		jalv
Version:	1.6.8
Release:	1
License:	ISC
Group:		Applications/Sound
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.xz
# Source0-md5:	7ae987243660ed44e882057aa24e5ede
URL:		http://drobilla.net/software/jalv/
BuildRequires:	Qt5Widgets-devel >= 5.1.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.120.0
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	lilv-devel >= 0.24.0
BuildRequires:	lv2-devel >= 1.18.0
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel >= 19
BuildRequires:	python3 >= 1:3.2
BuildRequires:	qt4-build >= 4.0.0
BuildRequires:	qt5-build >= 5.1.0
BuildRequires:	serd-devel >= 0.30.0
BuildRequires:	sord-devel >= 0.14.0
BuildRequires:	sratom-devel >= 0.6.4
BuildRequires:	suil-devel >= 0.10.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Gui >= 5.1.0
Requires:	gtk+2 >= 2:2.18.0
Requires:	gtk+3 >= 3.0.0
Requires:	jack-audio-connection-kit-libs >= 0.120.0
Requires:	lilv >= 0.24.0
Requires:	lv2 >= 1.18.0
Requires:	serd >= 0.30.0
Requires:	sord >= 0.14.0
Requires:	sratom >= 0.6.4
Requires:	suil >= 0.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jalv is a simple but fully featured LV2 host for JACK. It runs LV2
plugins and exposes their ports as JACK ports, essentially making any
LV2 plugin function as a JACK application.

%description -l pl.UTF-8
Jalv to prosty, ale w pełni funkcjonalny host LV2 dla JACK-a.
Uruchamia wtyczki LV2 i udostępnia ich porty jako porty JACK-a, w
szczególności pozwalając dowolnej wtyczce LV2 działać jako aplikacja
JACK-a.

%prep
%setup -q

%build
# Qt5 requires -fPIC from users
CXXFLAGS="%{rpmcxxflags} -fPIC"
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.md
%attr(755,root,root) %{_bindir}/jalv
%attr(755,root,root) %{_bindir}/jalv.gtk
%attr(755,root,root) %{_bindir}/jalv.gtk3
%attr(755,root,root) %{_bindir}/jalv.qt5
%attr(755,root,root) %{_libdir}/jack/jalv.so
%{_desktopdir}/jalv.desktop
%{_mandir}/man1/jalv.1*
%{_mandir}/man1/jalv.gtk.1*
%{_mandir}/man1/jalv.gtk3.1*
%{_mandir}/man1/jalv.qt5.1*
