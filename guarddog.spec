Summary:	A graphical tool for configuration of firewall
Summary(pl):	Graficzne narz�dzie do konfiguracji ogniomurka
Name:		guarddog
Version:	2.1.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.simonzone.com/software/guarddog/%{name}-%{version}.tar.gz
URL:		http://www.simonzone.com/software/guarddog/
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Guarddog is a firewall configuration utility for Linux systems.
Guarddog is aimed at two groups of users. Novice to intermediate users
who are not experts in TCP/IP networking and security, and those users
who don't want the hastle of dealing with cryptic shell scripts and
ipchains/iptables parameters.

%description -l pl
Guarddog jest narz�dziem do konfiguracji ogniomurka dla system�w
Linux. Guarddog zosta� stworzony dla dw�ch grup u�ytkownik�w, dla
pocz�tkuj�cych lub �rednio zaawansowani u�ytkownicy, kt�rzy nie s�
ekspertami w kwestii sieci oraz jej bezpiecze�stwa, oraz dla
u�ytkownik�w, kt�rzy nie chc� traci� czasu na tworzenie
skomplikowanych skrypt�w shellowych i regu�ek ipchains/iptables.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README TODO
%doc doc/en/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
%{_libdir}/menu/guarddog
