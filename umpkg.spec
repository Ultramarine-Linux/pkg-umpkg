%undefine       _disable_source_fetch
Name:           umpkg
Version:        0.2.1
Release:        %autorelease
Summary:        Ultramarine Linux Packaging tools

License:        MIT
URL:            https://gitlab.ultramarine-linux.org/release-engineering/umpkg/
Source0:        %{url}-/archive/%{version}/umpkg-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-virtualenv
Requires:       mock
Requires:       mock-core-configs
Requires:       rpmdevtools
Requires:       koji
Requires:       python3-typer
Requires:       python3-typer-cli
Requires:       python3-setuptools
Requires:       python3-wheel
Requires:       python3-gitlab
Provides:       ultramarine-packager
Provides:       python3-umpkg
Provides:       python3dist(umpkg)

# configparser is not available as a package for some reason
%{?python_disable_dependency_generator}

%description
The command-line tool for packaging Ultramarine Linux packages.

%prep
%autosetup -n umpkg-%{version}

%generate_buildrequires
%pyproject_buildrequires -R

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files umpkg

%files -f %{pyproject_files}

%{_bindir}/umpkg
%{_bindir}/umpkg-repo


%changelog
* Wed Feb 23 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
