%{?scl:%scl_package nodejs-ansistyles}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-ansistyles_0.1.3

%global npmname ansistyles
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-ansistyles
Version:        0.1.3
Release:        1%{?dist}
Summary:        Functions that surround a string with ansistyle codes so it prints in style.
Url:            https://github.com/thlorenz/ansistyles
Source0:        http://registry.npmjs.org/ansistyles/-/ansistyles-0.1.3.tgz
License:        MIT

BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Functions that surround a string with ansistyle codes so it prints in style.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/ansistyles
cp -pr package.json ansistyles.js %{buildroot}%{nodejs_sitelib}/ansistyles
%nodejs_symlink_deps
%check
%{?scl:scl enable %{scl} "}
node test/ansistyles.js
%{?scl:"}
%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/ansistyles

%doc LICENSE README.md

%changelog
* Thu Jan 30 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.3-1
- Initial build 
