Summary:	An fdisk-like partitioning tool for GPT disks
Name:		gdisk
Version:	0.7.2
Release:	1
License:	GPL v2
Group:		Base
URL:		http://www.rodsbooks.com/gdisk/
Source0:	http://downloads.sourceforge.net/gptfdisk/gptfdisk-%{version}.tar.gz
BuildRequires:	libicu-devel
BuildRequires:	libuuid-devel
BuildRequires:	popt-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An fdisk-like partitioning tool for GPT disks. GPT fdisk features a
command-line interface, fairly direct manipulation of partition table
structures, recovery tools to help you deal with corrupt partition
tables, and the ability to convert MBR disks to GPT format.

%prep
%setup -q -n gptfdisk-%{version}

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} -D_FILE_OFFSET_BITS=64"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
install -p gdisk sgdisk $RPM_BUILD_ROOT%{_sbindir}
cp -p gdisk.8 sgdisk.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/gdisk
%attr(755,root,root) %{_sbindir}/sgdisk
%{_mandir}/man8/gdisk.8*
%{_mandir}/man8/sgdisk.8*
