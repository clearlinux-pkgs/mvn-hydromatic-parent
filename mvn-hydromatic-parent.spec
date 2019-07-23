#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-hydromatic-parent
Version  : 0.1
Release  : 1
URL      : https://github.com/julianhyde/hydromatic-parent/archive/parent-0.1.tar.gz
Source0  : https://github.com/julianhyde/hydromatic-parent/archive/parent-0.1.tar.gz
Source1  : https://repo.maven.apache.org/maven2/net/hydromatic/parent/0.1/parent-0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-hydromatic-parent-data = %{version}-%{release}

%description
# hydromatic-parent
Parent POM for net.hydromatic projects

%package data
Summary: data components for the mvn-hydromatic-parent package.
Group: Data

%description data
data components for the mvn-hydromatic-parent package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/hydromatic/parent/0.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/net/hydromatic/parent/0.1/parent-0.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/net/hydromatic/parent/0.1/parent-0.1.pom
