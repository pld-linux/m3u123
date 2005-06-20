Summary:	Command line music player using XMMS I/O plugins to play music
Summary(pl):	Odtwarzacz muzyki z linii poleceñ u¿ywaj±cy wtyczek XMMS-a
Name:		m3u123
Version:	0.5.1
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://mail.rochester.edu/~asveikau/src/%{name}.tar.gz
# Source0-md5:	b61cd3464822077bfe795c0373dfc485
URL:		http://mail.rochester.edu/~asveikau/src/
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple program which uses XMMS I/O plugins to play files,
independently of XMMS itself. Not all XMMS plugins will work, but I've
found that most will.

%description -l pl
Jest to prosty program, który u¿ywa wtyczek wej¶cia/wyj¶cia XMMS-a do
odtwarzania plików niezale¿nie od samego XMMS-a. Nie wszystkie wtyczki
dzia³aj±, ale wiêkszo¶æ obs³ugiwana jest poprawnie.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}" \
	OUTPUT=OSS \
	STRIP=/bin/true

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install m3u123 $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
