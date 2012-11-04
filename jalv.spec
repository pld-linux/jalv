Summary:	Simple but fully featured LV2 host for JACK
Summary(pl.UTF-8):	Prosty, ale w pełni funkcjonalny host LV2 dla JACK-a
Name:		jalv
Version:	1.2.0
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	babb0ffb0f5083d87b93def98880579d
URL:		http://drobilla.net/software/jalv/
BuildRequires:	QtGui-devel >= 4.0.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtkmm-devel >= 2.20.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.120.0
BuildRequires:	libstdc++-devel
BuildRequires:	lilv-devel >= 0.14.0
BuildRequires:	lv2-devel >= 1.0.15
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	serd-devel >= 0.5.0
BuildRequires:	sratom-devel >= 0.2.0
BuildRequires:	suil-devel >= 0.6.0
Requires:	QtGui >= 4.0.0
Requires:	gtk+2 >= 2:2.18.0
Requires:	gtk+3 >= 3.0.0
Requires:	gtkmm >= 2.20.0
Requires:	jack-audio-connection-kit-libs >= 0.120.0
Requires:	lilv >= 0.14.0
Requires:	lv2 >= 1.0.15
Requires:	serd >= 0.5.0
Requires:	sratom >= 0.2.0
Requires:	suil >= 0.6.0
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
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--strict

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/jalv
%attr(755,root,root) %{_bindir}/jalv.gtk
%attr(755,root,root) %{_bindir}/jalv.gtk3
%attr(755,root,root) %{_bindir}/jalv.gtkmm
%attr(755,root,root) %{_bindir}/jalv.qt
%{_mandir}/man1/jalv.1*
%{_mandir}/man1/jalv.gtk.1*
%{_mandir}/man1/jalv.gtkmm.1*
%{_mandir}/man1/jalv.qt.1*
