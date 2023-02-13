Name: patrix
Version: 0.1.16
Release: 1%{?dist}
Summary: Command line client for Matrix

Group: Applications/Internet
License: MIT
URL: https://github.com/dani/patrix
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: perl(LWP::UserAgent)
Requires: perl(LWP::Protocol::https)
Requires: perl(Config::Simple)
Requires: perl(HTTP::Request)
Requires: perl(File::HomeDir)
Requires: perl(Getopt::Long)
Requires: perl(JSON)
Requires: perl(File::Basename)
Requires: perl(File::MimeInfo)
Requires: perl(File::Spec)
Requires: perl(URI::Escape)
Requires: perl(Term::ReadKey)
Requires: perl(Hash::Merge::Simple)
Requires: perl(Scalar::Util)
Requires: perl(HTML::Strip)

%description
Patrix is a simple (and quite limited) client for the Matrix communication network
(see https://matrix.org). It's written in perl, and lets you send text message to
room via the command line.

%prep
%setup -q

%build


%install

%{__rm} -rf $RPM_BUILD_ROOT

# Install 
%{__install} -d -m 750 $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 0755 scripts/* $RPM_BUILD_ROOT%{_bindir}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md TODO
%{_bindir}/patrix

%changelog
* Mon Feb 13 2023 Daniel Berteaud <dbd@ehtrace.com> 0.1.16-1
- Add HTML::Strip to Required (dbd@ehtrace.com)
- Add HTML::Strip and always support HTML messages (imagotrigger@gmail.com)

* Tue Jul 26 2022 Daniel Berteaud <dbd@ehtrace.com> 0.1.15-1
- Resign with new key

* Tue Jan 11 2022 Daniel Berteaud <dbd@ehtrace.com> 0.1.14-1
- Release bump for rebuild

* Mon Jan 03 2022 Daniel Berteaud <dbd@ehtrace.com> 0.1.13-1
- Check config readability and global /etc/patrixrc (dbd@ehtrace.com)

* Thu Dec 09 2021 Daniel Berteaud <dani@lapiole.org> 0.1.12-1
- Revert requiring LWP::Protocol::connect (dani@lapiole.org)

* Wed Dec 08 2021 Daniel Berteaud <dani@lapiole.org> 0.1.11-1
- Rebuild with new key

* Wed Nov 28 2018 Daniel Berteaud <daniel@firewall-services.com> 0.1.10-1
- Require LWP::Protocol::connect for EL distro (daniel@firewall-services.com)
- USe LWP::Protocol::connect to handle https proxy if available
  (daniel@firewall-services.com)

* Thu Feb 22 2018 Daniel Berteaud <daniel@firewall-services.com> 0.1.9-1
- Support using an HTTP proxy (daniel@firewall-services.com)

* Fri Nov 24 2017 Daniel Berteaud <daniel@firewall-services.com> 0.1.8-1
- Typo in README (daniel@firewall-services.com)
- Add support for --send-code (daniel@firewall-services.com)

* Thu Nov 23 2017 Daniel Berteaud <daniel@firewall-services.com> 0.1.7-1
- Fix get-room-id, Room ID is already resolved at this point (daniel@firewall-
  services.com)
- Resolve room alias to ID after setting defaults (daniel@firewall-
  services.com)

* Sun Nov 19 2017 Daniel Berteaud <daniel@firewall-services.com> 0.1.6-1
- Define actions array before the loop (daniel@firewall-services.com)

* Tue Nov 14 2017 Daniel Berteaud <daniel@firewall-services.com> 0.1.5-1
- Remove now non existing CHANGELOG.git (daniel@firewall-services.com)
- Fix tito releasers.conf path (daniel@firewall-services.com)

* Tue Nov 14 2017 Daniel Berteaud <daniel@firewall-services.com> 0.1.4-1
- new package built with tito

* Wed Sep 13 2017 Daniel Berteaud <daniel@firewall-services.com> - 0.1.3-1
- New release

* Wed Sep 13 2017 Daniel Berteaud <daniel@firewall-services.com> - 0.1.2-2
- Fix perl dependency in spec file

* Tue Sep 12 2017 Daniel Berteaud <daniel@firewall-services.com> - 0.1.2-1
- New release

* Fri Sep 8 2017 Daniel Berteaud <daniel@firewall-services.com> - 0.1.1-1
- New release

* Wed Sep 6 2017 Daniel B. <daniel@firewall-services.com> - 0.1.0-1
- Initial release
