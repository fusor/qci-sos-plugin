Summary: QCI SOS Plugin 
Name:    qci-sos-plugin
Version: 1.0.1
Release: 1%{?dist}
Group:   Applications/Internet 
License: Distributable
URL: https://github.com/fusor/qci-sos-plugin
Source0: %{name}-%{version}.tar.gz

BuildRequires: python-devel
Requires: python >= 2.3
Requires: sos

BuildArch: noarch

%description
QCI SOS Plugin

%prep
%setup -q

%install
install -d -m 755 %{buildroot}%{python_sitelib}/sos/plugins/
cp -a qci.py %{buildroot}%{python_sitelib}/sos/plugins/

%clean
%{__rm} -rf %{buildroot}

%files
%{python_sitelib}/sos/plugins/qci.py*

%changelog

