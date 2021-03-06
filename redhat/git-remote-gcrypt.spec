%global debug_package %{nil}

Name:		git-remote-gcrypt
Version:	1.0.2
Release:	1%{?dist}
Summary:	GNU Privacy Guard-encrypted git remote

Group:		Development Tools
License:	GPLv3
URL:		https://git.spwhitton.name/%{name}
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	python2-docutils
Requires:	gnupg2 git-core

%description
This lets git store git repositories in encrypted form.
It supports storing repositories on rsync or sftp servers.
It can also store the encrypted git repository inside a remote git
repository. All the regular git commands like git push and git pull
can be used to operate on such an encrypted repository.

The aim is to provide confidential, authenticated git storage and
collaboration using typical untrusted file hosts or services.

%prep
%setup -q -n %{name}

%build
:

%install
export DESTDIR="%{buildroot}"
export prefix="%{_prefix}"
./install.sh

%files
/usr/bin/%{name}
%doc /usr/share/man/man1/%{name}.1.gz

%changelog

