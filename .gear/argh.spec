%define _unpackaged_files_terminate_build 1

Name: argh
Version: 1.3.2
Release: alt2

Summary: Command line arguments parser
License: BSD-3-Clause
URL: https://github.com/adishavit/argh.git
Group: Development/C++
BuildArch: noarch

BuildRequires: cmake gcc-c++ doctest-devel

Source0: %name-%version.tar

%description
Minimalistic header-only parser of command line arguments for C++ programs

%prep
%setup

%build
%cmake -DBUILD_EXAMPLES=OFF -DBUILD_TESTS=ON
%cmake_build

%check
./%_cmake__builddir/argh_tests

%install
%cmakeinstall_std

install -D -m644 %name.h %buildroot%_includedir/%name.h
install -D -m644 LICENSE %buildroot%_datadir/doc/%name/LICENSE
install -D -m644 README.md %buildroot%_datadir/doc/%name/README.md

%files
%_includedir/%name.h
%_datadir/doc/%name/
%_libdir/cmake/%name/

%changelog
* Sun Sep 15 2024 Pavel Khromov <hromovpi@altlinux.org> 1.3.2-alt2
- Fix uninstalling package
- Installing CMake targets

* Wed Sep 04 2024 Pavel Khromov <hromovpi@altlinux.org> 1.3.2-alt1
- Initial build for ALT
