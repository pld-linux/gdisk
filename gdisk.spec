Summary:	An fdisk-like partitioning tool for GPT disks
Summary(pl.UTF-8):	Podobne do fdiska narzędzie do partycjonowania dysków GPT
Name:		gdisk
Version:	1.0.3
Release:	1
License:	GPL v2
Group:		Base
Source0:	http://downloads.sourceforge.net/gptfdisk/gptfdisk-%{version}.tar.gz
# Source0-md5:	07b625a583b66c8c5840be5923f3e3fe
Patch0:		%{name}-link.patch
URL:		http://www.rodsbooks.com/gdisk/
#BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libuuid-devel
BuildRequires:	ncurses-devel
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPT fdisk (gdisk) is an fdisk-like partitioning tool for GPT disks.
It features a command-line interface, fairly direct manipulation of
partition table structures, recovery tools to help you deal with
corrupt partition tables, and the ability to convert MBR disks to GPT
format.

%description -l pl.UTF-8
GPT fdisk (gdisk) to podobne do fdiska narzędzie do partycjonowania
dysków GPT. Ma interfejs linii poleceń, w miarę bezpośrednie operacje
na strukturach tablicy partycji, narzędzia pomagające przy naprawie
uszkodzonych tablic partycji oraz możliwość konwersji dysków MBR do
formatu GPT.

%prep
%setup -q -n gptfdisk-%{version}
# since 0.8.9 libicu for UTF-16 support is optional
#%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} %{rpmcppflags} -D_FILE_OFFSET_BITS=64"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install fixparts *gdisk $RPM_BUILD_ROOT%{_sbindir}
install -p *.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README *.html
%attr(755,root,root) %{_sbindir}/fixparts
%attr(755,root,root) %{_sbindir}/*gdisk
%{_mandir}/man8/fixparts.8*
%{_mandir}/man8/*gdisk.8*
