Name: hdajackretask-realtek-alc887-vd
Version: 0.0.2
Release: 1%{?dist}
License: GPL-3.0 license
Summary: RPM package to install 5.1 firware for realtek-alc887-vd to enable 5.1 surround on immutable filesystems.
Url: https://github.com/PVermeer/copr_realtek-alc887-vd

BuildRequires: git

%define workdir %{_builddir}/work

%description
RPM package to install 5.1 firware for realtek-alc887-vd to enable 5.1 surround on immutable filesystems.

Pink mic, rear side -> Center/LFE
Blue line in, rear side -> Line out to back

%prep
git clone https://github.com/PVermeer/copr_realtek-alc887-vd.git %{workdir}

%install
mkdir -p %{buildroot}/etc/modprobe.d
mkdir -p %{buildroot}/lib/firmware

install %{workdir}/hda-jack-retask.fw %{buildroot}/lib/firmware
install %{workdir}/hda-jack-retask.conf %{buildroot}/etc/modprobe.d

%files
/lib/firmware/hda-jack-retask.fw
/etc/modprobe.d/hda-jack-retask.conf
