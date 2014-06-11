%define uname vowpal_wabbit
%define name vowpal-wabbit
%define version 7.6
%define release 4
%define major 0
%define libname lib%{name}%{major}
%define develname lib%{name}-devel

Summary: A fast and efficient machine learning system
Name:    %{name}
Version: %{version}
Release: %{release}
Source0: http://github.com/JohnLangford/%{uname}/archive/%{version}.tar.gz
License: BSD
Group:   Sciences/Mathematics
Url:     http://hunch.net/~vw/
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: zlib-devel
#Requires: %{libname} = %{version}

%description
The Vowpal Wabbit (VW) project is a fast out-of-core learning system sponsored
by Microsoft Research and (previously) Yahoo! Research.

%package -n     %{libname}
Summary:        Main library for Vowpal Wabbit
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}
 
%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with vowpal-wabbit.

%package -n     %{develname}
Summary:        Headers for developing programs that will use Vowpal Wabbit
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}
 
%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use Vowpal Wabbit.

%prep
%setup -q -n %{uname}-%{version}

%build
./configure
make clean
make

%install
make \
    DESTDIR=$RPM_BUILD_ROOT \
install

# install the utl scripts
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_includedir}/vowpalwabbit/
cp utl/vw-convergence %{buildroot}%{_bindir}/
cp utl/vw2csv %{buildroot}%{_bindir}/
cp utl/vw-regr %{buildroot}%{_bindir}/
cp utl/vw-varinfo %{buildroot}%{_bindir}/
cp $RPM_BUILD_ROOT/usr/local/bin/* %{buildroot}%{_bindir}/
cp $RPM_BUILD_ROOT/usr/local/lib/*  %{buildroot}%{_libdir}/
cp $RPM_BUILD_ROOT/usr/local/include/vowpalwabbit/*  %{buildroot}%{_includedir}/vowpalwabbit/
mkdir -p %{buildroot}%{_datadir}/vowpalwabbit
cp utl/vw-validate.html %{buildroot}%{_datadir}/vowpalwabbit/
mv README.md README

# remove libtool files
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

rm -fr $RPM_BUILD_ROOT/usr/local/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README LICENSE AUTHORS
%{_bindir}/active_interactor
%{_bindir}/library_example
%{_bindir}/spanning_tree
%{_bindir}/vw
%{_bindir}/vw-convergence
%{_bindir}/vw-regr
%{_bindir}/vw-varinfo
%{_bindir}/vw2csv
%{_datadir}/vowpalwabbit/vw-validate.html

 
%files -n %{libname}
%{_libdir}/liballreduce.so.%{major}*
%{_libdir}/libvw.so.%{major}*
 
%files -n %{develname}
%{_includedir}/vowpalwabbit/*.h
%{_libdir}/*.so
%{_datadir}/vowpalwabbit/vw-validate.html


%changelog
* Wed Jun 11 2014 Vladimir Vladimirov <smartkiwi@gmail.com> 7.6
+ Revision: 586839
- spec file updated for Cent OS
- building from 7.6 sources
- README was renamed to README.md
- changed github url - tag name not doesn't include "v" prefix (7.6 instead of v7.3)

* Sat Feb 08 2014 barjac <barjac> 7.3-3.mga5
+ Revision: 586839
- rebuild against boost-1.55

* Sat Oct 19 2013 umeabot <umeabot> 7.3-2.mga4
+ Revision: 533683
- Mageia 4 Mass Rebuild

* Tue Sep 03 2013 malo <malo> 7.3-1.mga4
+ Revision: 474822
- update to 7.3 and libification

* Wed Apr 10 2013 malo <malo> 7.2-2.mga4
+ Revision: 409436
- rebuild for boost 1.53

* Fri Apr 05 2013 malo <malo> 7.2-1.mga3
+ Revision: 408413
- update to 7.2, removed upstreamed patches

* Sat Jan 26 2013 malo <malo> 7.1-1.mga3
+ Revision: 392464
- fix build with upstream and linking patches
- patch for automake 1.13
- imported package vowpal-wabbit

