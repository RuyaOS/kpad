Name: kpad
Version: 1
Release: 1%{?dist}
Summary: Auto enable touchpad tapping in Wayland KDE
License: GPLv3
URL: https://parmg.sa
Source0: LICENSE
Source1: kpad
Source2: 30-touchpad.conf
Source3: kpad.desktop
Source4: lspad
Source5: sa.parmg.ruya.pkexec.kpad.policy
Source6: sa.parmg.ruya.pkexec.kpad.rules
BuildArch: noarch

%description
Auto enable touchpad tapping in Wayland KDE

%prep
cp %{SOURCE0} .

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/skel/.config/autostart
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
mkdir -p %{buildroot}%{_datadir}/polkit-1/rules.d
mkdir -p %{buildroot}%{_sysconfdir}/X11/xorg.conf.d

install -Dp -m 0755 %{SOURCE1} %{buildroot}%{_bindir}
install -Dp -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/X11/xorg.conf.d
install -Dp -m 0755 %{SOURCE3} %{buildroot}%{_sysconfdir}/skel/.config/autostart
install -Dp -m 0755 %{SOURCE4} %{buildroot}%{_bindir}
install -Dp -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/polkit-1/actions
install -Dp -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/polkit-1/rules.d

%files
%license LICENSE
%{_bindir}/kpad
%{_bindir}/lspad
%{_sysconfdir}/X11/xorg.conf.d/30-touchpad.conf
%{_sysconfdir}/skel/.config/autostart/kpad.desktop
%{_datadir}/polkit-1/actions/sa.parmg.ruya.pkexec.kpad.policy
%{_datadir}/polkit-1/rules.d/sa.parmg.ruya.pkexec.kpad.rules

%changelog
* Sat Oct 22 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 1-1
- Initial
