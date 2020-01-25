Summary:	A Web-based monitor for ISC DHCP lease statistics
Summary(pl.UTF-8):	Statystyki dla ISC DHCP na stronie WWW
Name:		reportdhcp
Version:	2.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.omar.org/opensource/reportdhcp/%{name}.pl-%{version}.tar.gz
# Source0-md5:	72c3ad073c846981701b4db787112a95
Patch0:		%{name}-config.patch
URL:		http://www.omar.org/opensource/reportdhcp/
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reportdhcp.pl is a CGI script written in perl. It displays statistics
and lease entries for ISC DHCPD by parsing the dhcpd.conf and
dhcpd.leases files.

%description -l pl.UTF-8
Reportdhcp.pl jest skryptem CGI napisanym w perlu. Wyświetla
statystyki oraz wpisy dzierżaw dla ISC DHCPD poprzez analizę pliku
dhcpd.conf oraz dhcpd.leases.

%prep
%setup -q -c
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/services/httpd/cgi-bin/reportdhcp

install reportdhcp.pl $RPM_BUILD_ROOT/home/services/httpd/cgi-bin/reportdhcp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%dir /home/services/httpd/cgi-bin/reportdhcp
%attr(755,root,root) /home/services/httpd/cgi-bin/reportdhcp/reportdhcp.pl
