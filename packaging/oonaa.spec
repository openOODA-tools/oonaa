Name:           oonaa
Version:        0.1.0
Release:        1%{?dist}
Summary:        Enforces zero ambient authentication, requiring explicit credential passing.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oonaa
Source0:        oonaa-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oonaa is a sovereign, capability-bounded NO AMBIENT AUTH written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oonaa
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oonaa-uninstall

%files
/usr/bin/oonaa
/usr/bin/oonaa-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
