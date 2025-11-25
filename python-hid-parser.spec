%define oname hid_parser

%bcond_without tests

Name:		python-hid-parser
Version:	0.1.0
Release:	1
Summary:	Typed pure Python library to parse HID report descriptors
URL:		https://github.com/usb-tools/python-hid-parser
License:	MIT
Group:		Development/Python
Source0:	https://github.com/usb-tools/python-hid-parser/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(typing-extensions)

%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(hypothesis)
%endif

%description
Typed pure Python library to parse HID report descriptors

%prep
%autosetup -p1

# we dont do coverage tests, remove the module dependency
sed -i -e "s/'pytest-cov',//g" pyproject.toml

%build
%py_build

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
%{__python} -m pytest -v -rs tests/
%endif

%files
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.*-info
%license LICENSE
%doc README.md
