#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : statsmodels
Version  : 0.13.1
Release  : 24
URL      : https://files.pythonhosted.org/packages/e7/86/8c95a2f43d8d66837f52fc0a2d9b4ea491e564789ee94d28f642d9d47ebc/statsmodels-0.13.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e7/86/8c95a2f43d8d66837f52fc0a2d9b4ea491e564789ee94d28f642d9d47ebc/statsmodels-0.13.1.tar.gz
Summary  : Statistical computations and models for Python
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: statsmodels-license = %{version}-%{release}
Requires: statsmodels-python = %{version}-%{release}
Requires: statsmodels-python3 = %{version}-%{release}
Requires: pandas
Requires: scipy
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : numpy
BuildRequires : pandas
BuildRequires : patsy
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(cython)
BuildRequires : pypi(numpy)
BuildRequires : pypi(pandas)
BuildRequires : pypi(patsy)
BuildRequires : pypi(scipy)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : python-dateutil
BuildRequires : scipy
BuildRequires : tox
BuildRequires : virtualenv

%description
The format for landing.json should be self-explanatory. The images should be placed in docs/source/_static/images/. They will be displayed at 360 x 225 (W x H). It's best to save them as a png with a resolution of a multiple of at least 720 x 450. If you want, you can use png crush to make the images smaller.

%package license
Summary: license components for the statsmodels package.
Group: Default

%description license
license components for the statsmodels package.


%package python
Summary: python components for the statsmodels package.
Group: Default
Requires: statsmodels-python3 = %{version}-%{release}

%description python
python components for the statsmodels package.


%package python3
Summary: python3 components for the statsmodels package.
Group: Default
Requires: python3-core
Provides: pypi(statsmodels)
Requires: pypi(numpy)
Requires: pypi(pandas)
Requires: pypi(patsy)
Requires: pypi(scipy)

%description python3
python3 components for the statsmodels package.


%prep
%setup -q -n statsmodels-0.13.1
cd %{_builddir}/statsmodels-0.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641321107
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

## build_append content
rm -f %{_builddir}/statsmodels-0.13.1/statsmodels/LICENSE.txt
touch  %{_builddir}/statsmodels-0.13.1/statsmodels/LICENSE.txt
## build_append end
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/statsmodels
cp %{_builddir}/statsmodels-0.13.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/statsmodels/2d60e5640eefa748369bb8731e2376c1993cca43
cp %{_builddir}/statsmodels-0.13.1/statsmodels/LICENSE.txt %{buildroot}/usr/share/package-licenses/statsmodels/2d60e5640eefa748369bb8731e2376c1993cca43
cp %{_builddir}/statsmodels-0.13.1/statsmodels/multivariate/factor_rotation/LICENSE.txt %{buildroot}/usr/share/package-licenses/statsmodels/0fc2c72f519bbfc29403c0fea97ec8f2dc28b35a
cp %{_builddir}/statsmodels-0.13.1/statsmodels/stats/libqsturng/LICENSE.txt %{buildroot}/usr/share/package-licenses/statsmodels/c207c94132c3d588103b506d0eeec17c665c0ae6
cp %{_builddir}/statsmodels-0.13.1/statsmodels/tsa/statespace/tests/results/frbny_nowcast/Nowcasting/LICENSE %{buildroot}/usr/share/package-licenses/statsmodels/375dbeee823f610ce7d2a3b79a0ae094de427c63
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/statsmodels/0fc2c72f519bbfc29403c0fea97ec8f2dc28b35a
/usr/share/package-licenses/statsmodels/2d60e5640eefa748369bb8731e2376c1993cca43
/usr/share/package-licenses/statsmodels/375dbeee823f610ce7d2a3b79a0ae094de427c63
/usr/share/package-licenses/statsmodels/c207c94132c3d588103b506d0eeec17c665c0ae6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
