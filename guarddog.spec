Summary:	A graphical tool for configuration of firewall
Summary(pl):	Graficzne narz�dzie do konfiguracji ogniomurka
Name:		guarddog
Version:	2.5.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.simonzone.com/software/guarddog/%{name}-%{version}.tar.gz
# Source0-md5:	baa25ee6e20bb49a96259077e67ba097
Patch0:		%{name}-desktop.patch
URL:		http://www.simonzone.com/software/guarddog/
BuildRequires:	kdebase-devel >= 3.1
BuildRequires:	qt-devel >= 3.1
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

%description -l pl
Guarddog jest narz�dziem do konfiguracji ogniomurka dla system�w
Linux. Guarddog zosta� stworzony dla dw�ch grup u�ytkownik�w, dla
pocz�tkuj�cych lub �rednio zaawansowanych u�ytkownik�w, kt�rzy nie s�
ekspertami w kwestii sieci oraz jej bezpiecze�stwa, oraz dla
u�ytkownik�w, kt�rzy nie chc� traci� czasu na tworzenie
skomplikowanych skrypt�w pow�oki i regu�ek ipchains/iptables.

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
