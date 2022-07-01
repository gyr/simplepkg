#
# spec file for package simplepkg
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           simplepkg
Version:        1
Release:        0
Summary:        Simple package
License:        MIT
Group:          Development/Tools/Other
#Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Simple test package for OBS

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 simplescript.sh %{buildroot}/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/simplescript.sh
