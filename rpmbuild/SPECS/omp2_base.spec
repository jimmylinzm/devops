# sudo yum -y install rpmdevtools && rpmdev-setuptree
# sudo yum -y install libtool automake autoconf zeromq-devel
# wget https://raw.github.com/nmilford/rpm-jzmq/master/jzmq.spec -O ~/rpmbuild/SPECS/jzmq.spec
# wget https://codeload.github.com/nathanmarz/jzmq/zip/master -O ~/rpmbuild/SOURCES/jzmq-2.1.0.zip
# rpmbuild -bb ~/rpmbuild/SPECS/jzmq.spec

Name:          omp2_base
Version:       0.01
Release:       storm%{?dist}
Summary:       The infrastructure for storm
Group:         Applications/Internet
License:       COMMERCIAL
URL:           http://www.sf-express.com/
Source:        %{name}-%{version}.tar.gz
Prefix:        %{prefix} 
BuildRoot:     /
Requires:      libstdc++,unzip,libuuid
AutoReqProv: no

%description
The infrastructure for storm

%prep
%setup -q -n omp2_base
sh package.sh

%install
make ROOT="$RPM_BUILD_ROOT" install

%post
sh /config/config.sh
/sbin/ldconfig

%preun
sh /config/uninstall_config.sh

%postun
rm -rf /usr/share/neo4j-community-1.9.5
rm -rf /package
/sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
/etc
/service
/usr
%attr(1777,root,root) /config
%attr(1755,root,root) /package
