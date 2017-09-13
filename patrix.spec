Name: patrix
Version: 0.1.3
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
%doc README.md TODO CHANGELOG.git
%{_bindir}/patrix

%changelog
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
