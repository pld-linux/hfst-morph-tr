Summary:	HFST morphological analysis transducer for Turkish language
Summary(pl.UTF-8):	Automat HFST do analizy morfologicznej dla języka tureckiego
Name:		hfst-morph-tr
# or 20110316?
Version:	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
# source is hfst-turkish.tar.gz, but it doesn't contain scripts
Source0:	http://downloads.sourceforge.net/hfst/hfst-turkish-installable.tar.gz
# Source0-md5:	0862b7cc418f892d8caa7d33f5837118
Patch0:		%{name}-DESTDIR.patch
URL:		http://hfst.sourceforge.net/
Requires:	hfst
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Turkish morphological transducer for HFST. It's based on
TRmorph morphological analyzer
<http://www.let.rug.nl/coltekin/trmorph/>.

%description -l pl.UTF-8
Ten pakiet zawiera automat dla HFST do analizy morfologicznej języka
tureckiego. Jest oparty na analizatorze morfologicznym TRmorph
<http://www.let.rug.nl/coltekin/trmorph/>.

%prep
%setup -q -n hfst-turkish-installable
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/turkish-analyze.sh
%attr(755,root,root) %{_bindir}/turkish-generate.sh
%{_datadir}/hfst/tr
