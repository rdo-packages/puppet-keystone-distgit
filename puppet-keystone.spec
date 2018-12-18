%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-keystone
Version:        XXX
Release:        XXX
Summary:        Puppet module for OpenStack Keystone
License:        ASL 2.0

URL:            https://launchpad.net/puppet-keystone

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-apache
Requires:       puppet-inifile
Requires:       puppet-openstacklib
Requires:       puppet-oslo
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Keystone

%prep
%setup -q -n openstack-keystone-%{upstream_version}

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
#(trown) empty commit to use:
# https://github.com/redhat-openstack/rdoinfo/commit/28ee76369bf9bd357a5e2409b588856513cbe83d
# This should be removed on the next commit to puppet-keystone-distgit


# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/puppet-keystone/commit/?id=63142bf6ef8874e4e4af00990b42f236fabc5e4c
