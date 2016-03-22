Name:			puppet-keystone
Version:		XXX
Release:		XXX
Summary:		Puppet module for OpenStack Keystone
License:		Apache-2.0

URL:			https://launchpad.net/puppet-keystone

Source0:		https://github.com/openstack/puppet-keystone/archive/%{version}.tar.gz

BuildArch:		noarch

Requires:		puppet-apache
Requires:		puppet-inifile
Requires:		puppet-stdlib
Requires:		puppet-openstacklib
Requires:		puppet >= 2.7.0

%description
Puppet module for OpenStack Keystone

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/keystone/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/keystone/



%files
%{_datadir}/openstack-puppet/modules/keystone/


%changelog

