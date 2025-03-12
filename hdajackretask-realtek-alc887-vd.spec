# Create an option to build locally without fetchting own repo
# for sourcing and patching
%bcond local 0

# Own copr repo
%global coprrepo https://github.com/PVermeer/copr_realtek-alc887-vd.git
%global coprsource copr_realtek-alc887-vd

Name: hdajackretask-realtek-alc887-vd
Version: 0.0.2
Release: 1%{?dist}
License: GPL-3.0 license
Summary: RPM package to install 5.1 firware for realtek-alc887-vd to enable 5.1 surround on immutable filesystems.
Url: %{coprrepo}

BuildRequires: git

%define workdir %{_builddir}/%{name}
%define coprdir %{workdir}/%{coprsource}

%description
RPM package to install 5.1 firware for realtek-alc887-vd to enable 5.1 surround on immutable filesystems.

Pink mic, rear side -> Center/LFE
Blue line in, rear side -> Line out to back

%prep
# To apply working changes handle sources / patches locally
# COPR should clone the commited changes
%if %{with local}
  # Get sources / patches - local build
  mkdir -p %{coprdir}
  cp -r %{_topdir}/SOURCES/* %{coprdir}
%else
  # Get sources / patches - COPR build
  git clone %{coprrepo} %{coprdir}
  cd %{coprdir}
  rm -rf .git
  cd %{workdir}
%endif

%build

%install
mkdir -p %{buildroot}/etc/modprobe.d
mkdir -p %{buildroot}/lib/firmware

install %{coprdir}/sources/hda-jack-retask.fw %{buildroot}/lib/firmware
install %{coprdir}/sources/hda-jack-retask.conf %{buildroot}/etc/modprobe.d

%check

%post

%files
/lib/firmware/hda-jack-retask.fw
/etc/modprobe.d/hda-jack-retask.conf
