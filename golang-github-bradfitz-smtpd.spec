# Run tests in check section
%bcond_without check

%global goipath         github.com/bradfitz/go-smtpd
%global commit          deb6d623762522f8ad4a55b952001e4215a76cf4

%global common_description %{expand:
SMTP server library for Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        SMTP server library for Go 
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitdeb6d62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1-20180417gitdeb6d62
- First package for Fedora

