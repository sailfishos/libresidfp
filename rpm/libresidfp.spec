Name:       libresidfp
Summary:    SID playback library
Version:    1.2.3
Release:    1
License:    GPLv2+
URL:        https://github.com/sailfishos/libresidfp
Source:     %{name}-%{version}.tar.gz

%description
reSIDfp is a fork of Dag Lem's reSID 0.16, a reverse engineered software
emulation of the MOS6581/8580 SID (Sound Interface Device).

%package devel
Summary:    libresidfp development headers and libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Files required for using libresidfp library.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libresidfp.so.*

%files devel
%{_libdir}/libresidfp.a
%{_libdir}/libresidfp.so
%{_libdir}/pkgconfig/libresidfp.pc
%dir %{_includedir}/residfp
%{_includedir}/residfp/residfp_defs.h
%{_includedir}/residfp/residfp.h
%{_includedir}/residfp/sidversion.h
