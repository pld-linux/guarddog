Summary:	A graphical tool for configuration of firewall
Summary(pl):	Graficzne narzêdzie do konfiguracji ogniomurka
Name:		guarddog
Version:	2.1.5
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.simonzone.com/software/guarddog/%{name}-%{version}.tar.gz
# Source0-md5:	55faa1fd541414abed84ae9c40f6eaf5
URL:		http://www.simonzone.com/software/guarddog/
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
Guarddog is a firewall configuration utility for Linux systems.
Guarddog is aimed at two groups of users. Novice to intermediate users
who are not experts in TCP/IP networking and security, and those users
who don't want the hastle of dealing with cryptic shell scripts and
ipchains/iptables parameters.

%description -l pl
Guarddog jest narzêdziem do konfiguracji ogniomurka dla systemów
Linux. Guarddog zosta³ stworzony dla dwóch grup u¿ytkowników, dla
pocz±tkuj±cych lub ¶rednio zaawansowanych u¿ytkowników, którzy nie s±
ekspertami w kwestii sieci oraz jej bezpieczeñstwa, oraz dla
u¿ytkowników, którzy nie chc± traciæ czasu na tworzenie
skomplikowanych skryptów pow³oki i regu³ek ipchains/iptables.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/guarddog
%{_pixmapsdir}/*/*/apps/*.png
%{_applnkdir}/System/*.desktop
