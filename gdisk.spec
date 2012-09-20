Summary:	An fdisk-like partitioning tool for GPT disks
Name:		gdisk
Version:	0.7.2
Release:	3
License:	GPL v2
Group:		Base
URL:		http://www.rodsbooks.com/gdisk/
Source0:	http://downloads.sourceforge.net/gptfdisk/gptfdisk-%{version}.tar.gz
# Source0-md5:	31deeb7acb5104d56ba2ddeafd907513
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libuuid-devel
BuildRequires:	popt-devel
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
install -p gdisk sgdisk fixparts $RPM_BUILD_ROOT%{_sbindir}
cp -p gdisk.8 sgdisk.8 fixparts.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_sbindir}/fixparts
%attr(755,root,root) %{_sbindir}/gdisk
%attr(755,root,root) %{_sbindir}/sgdisk
%{_mandir}/man8/fixparts.8*
%{_mandir}/man8/gdisk.8*
%{_mandir}/man8/sgdisk.8*
