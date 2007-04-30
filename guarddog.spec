Summary:	A graphical tool for configuration of firewall
Summary(pl.UTF-8):	Graficzne narzędzie do konfiguracji ogniomurka
Name:		guarddog
Version:	2.6.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.simonzone.com/software/guarddog/%{name}-%{version}.tar.gz
# Source0-md5:	a1535c4e3f668ea1de5a12f671e7af13
Patch0:		%{name}-desktop.patch
URL:		http://www.simonzone.com/software/guarddog/
BuildRequires:	kdebase-devel >= 3.1
BuildRequires:	qt-devel >= 6:3.1
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	gawk
Requires:	iptables
Requires:	kdebase-core >= 3.1
Requires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guarddog is a firewall configuration utility for Linux systems.
Guarddog is aimed at two groups of users. Novice to intermediate users
who are not experts in TCP/IP networking and security, and those users
who don't want the hastle of dealing with cryptic shell scripts and
ipchains/iptables parameters.

%description -l pl.UTF-8
Guarddog jest narzędziem do konfiguracji ogniomurka dla systemów
Linux. Guarddog został stworzony dla dwóch grup użytkowników, dla
początkujących lub średnio zaawansowanych użytkowników, którzy nie są
ekspertami w kwestii sieci oraz jej bezpieczeństwa, oraz dla
użytkowników, którzy nie chcą tracić czasu na tworzenie
skomplikowanych skryptów powłoki i regułek ipchains/iptables.

%prep
%setup -q
%patch0 -p0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/System/%{name}.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/%{name}.desktop

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/guarddog
%{_iconsdir}/hicolor/*/apps/*.png
%{_desktopdir}/kde/*.desktop
%{_datadir}/sgml/protocoldb/1.0
%{_datadir}/sgml/protocoldb/xmlcatalog
