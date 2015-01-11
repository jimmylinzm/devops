# sudo yum -y install rpmdevtools && rpmdev-setuptree
# sudo yum -y install libtool automake autoconf

Name:          omp2_vishnu
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
%setup -n omp2_vishnu
sh package.sh

%install
make ROOT="$RPM_BUILD_ROOT" install

%post
(cp -rf /omp2/route_data/data_vishnu/* /usr/omp2/vishnu/data/ && cd /usr/omp2/vishnu && sh start_vishnu.sh)

%preun
(cd /usr/omp2/vishnu && sh stop_vishnu.sh) || echo "uninstalled"

%postun
rm -rf /usr/omp2/vishnu

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr
