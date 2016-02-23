%{?scl:%scl_package nodejs-ansistyles}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-ansistyles_0.1.3

%global npmname ansistyles
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-ansistyles
Version:        0.1.3
Release:        4%{?dist}
Summary:        Functions that surround a string with ansistyle codes so it prints in style.
Url:            https://github.com/thlorenz/ansistyles
Source0:        http://registry.npmjs.org/ansistyles/-/ansistyles-%{version}.tgz
License:        MIT

BuildArch:      noarch

%if 0%{?fedora} >= 19
ExclusiveArch:  %{nodejs_arches} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Functions that surround a string with ansistyle codes so it prints in style.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/ansistyles
cp -pr package.json ansistyles.js %{buildroot}%{nodejs_sitelib}/ansistyles
%nodejs_symlink_deps

%check
%{?scl:scl enable %{scl} "}
node test/ansistyles.js
%{?scl:"}

%files
%{nodejs_sitelib}/ansistyles
%doc LICENSE README.md

%changelog
* Thu Feb 18 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.3-4
- Add missing ExclusiveArch and BuildArch
- Use macro in -runtime dependency
- Rebuilt with updated metapackage

* Thu Jan 30 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.3-1
- Initial build 
