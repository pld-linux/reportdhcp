%include	/usr/lib/rpm/macros.perl
Summary:	A Web-based monitor for ISC DHCP lease statistics
Summary(pl):	Statystyki dla ISC DHCP na stronie WWW
Name:		reportdhcp
Version:	2.0b
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.omar.org/opensource/reportdhcp/%{name}.pl-%{version}.tar.gz
# Source0-md5:	313f8757f1d7a60215c8baa8e338a70c
Patch0:		%{name}-config.patch
URL:		http://www.omar.org/opensource/reportdhcp/
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reportdhcp.pl is a CGI script written in perl. It displays statistics
and lease entries for ISC DHCPD by parsing the dhcpd.conf and
dhcpd.leases files.

%description -l pl
Reportdhcp.pl jest skryptem CGI napisanym w perlu. Wy¶wietla
statystyki oraz wpisy dzier¿aw dla ISC DHCPD poprzez pasowanie pliku
dhcpd.conf oraz dhcpd.leases.

%prep
%setup -q -c -n %{name}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/services/httpd/cgi-bin/reportdhcp/

install reportdhcp.pl $RPM_BUILD_ROOT/home/services/httpd/cgi-bin/reportdhcp/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%dir /home/services/httpd/cgi-bin/reportdhcp
%attr(755,root,root) /home/services/httpd/cgi-bin/reportdhcp/reportdhcp.pl
