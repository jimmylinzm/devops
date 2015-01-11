# sudo yum -y install rpmdevtools && rpmdev-setuptree
# sudo yum -y install libtool automake autoconf

Name:          omp2_shiva
Version:       2.0.0
Release:       %{?dist}
Summary:       UI
Group:         Applications/Internet
License:       COMMERCIAL
URL:           http://www.sf-express.com/
Source:        %{name}-%{version}.tar.gz
Prefix:        %{prefix} 
BuildRoot:     /
AutoReqProv:   no

%description
The infrastructure for storm

%prep
%setup -n omp2_shiva
sh package.sh

%install
make ROOT="$RPM_BUILD_ROOT" install

%post
(cp -rf /omp2/config/shiva/* /usr/omp2/shiva && cd /usr/omp2/shiva && sh start_shiva.sh)

%preun
(cd /usr/omp2/shiva && sh stop_shiva.sh) || echo "uninstalled"

%postun
rm -rf /usr/omp2/shiva

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr
