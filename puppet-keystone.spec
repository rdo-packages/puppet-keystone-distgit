%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-keystone
Version:        11.6.0
Release:        1%{?dist}
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
* Thu May 16 2019 RDO <dev@lists.rdoproject.org> 11.6.0-1
- Update to 11.6.0

* Fri Jan 19 2018 RDO <dev@lists.rdoproject.org> 11.4.0-1
- Update to 11.4.0

* Fri Dec 01 2017 RDO <dev@lists.rdoproject.org> 11.3.1-1
- Update to 11.3.1

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 11.3.0-1
- Update to 11.3.0

#(trown) empty commit to use:
# https://github.com/redhat-openstack/rdoinfo/commit/28ee76369bf9bd357a5e2409b588856513cbe83d
# This should be removed on the next commit to puppet-keystone-distgit


