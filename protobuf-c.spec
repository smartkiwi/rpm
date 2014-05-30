Name:           protobuf-c
Version:        1.0.0
Release:        rc1.magnetic
Summary:        C bindings for Google's Protocol Buffers
Group:          System Environment/Libraries
License:        ASL 2.0
URL:            https://github.com/protobuf-c/protobuf-c/
Source0:        https://github.com/protobuf-c/protobuf-c/releases/download/v1.0.0-rc1/protobuf-c-1.0.0-rc1.tar.gz

#BuildRequires:  protobuf-devel

%description
Protocol Buffers are a way of encoding structured data in an efficient yet 
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c. 

%package devel
Summary:        Protocol Buffers C headers and libraries
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains protobuf-c headers and libraries.

%prep
%setup -q -n protobuf-c-1.0.0-rc1
#cp %{SOURCE1} .

%build
%configure --disable-static
# Causes build to fail
#make %{?_smp_mflags}
make

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/libprotobuf-c.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/protoc-c
%{_libdir}/libprotobuf-c.so.*
%doc TODO LICENSE ChangeLog

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/google
/usr/include/protobuf-c/protobuf-c.h
%{_includedir}/google/protobuf-c
%{_libdir}/libprotobuf-c.so
%{_libdir}/pkgconfig/libprotobuf-c.pc

%changelog
* Thu May 29 2014 Vladimir Vladimirov <smartkiwi@gmail.com> - 1.0.0-rc1
- updated to use latest protobuf-c version from github

* Sun Apr 24 2011 David Robinson <zxvdr.au@gmail.com> - 0.15-2
- Spec file cleanup

* Wed Apr 20 2011 David Robinson <zxvdr.au@gmail.com> - 0.15-1
- New upstream release
- Spec file cleanup

* Mon Jan 17 2011 Bobby Powers <bobby@laptop.org> - 0.14-1
- New upstream release
- Removed -devel dependency on protobuf-devel
- Small specfile cleanups

* Wed May 19 2010 David Robinson <zxvdr.au@gmail.com> - 0.13-2
- Spec file cleanup

* Wed May 19 2010 David Robinson <zxvdr.au@gmail.com> - 0.13-1
- Initial packaging
