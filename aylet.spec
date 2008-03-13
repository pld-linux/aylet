# TODO: pl description
Summary:	AY player
Summary(pl.UTF-8):	Odtwarzacz AY
Name:		aylet
Version:	0.5
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	ftp://ftp.ibiblio.org/pub/Linux/apps/sound/players/%{name}-%{version}.tar.gz
# Source0-md5:	a4df39033644b3aa7c89899708bad207
URL:		http://rus.members.beeb.net/aylet.htm
BuildRequires:	gtk+-devel
BuildRequires:	ncurses-devel
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aylet plays music files in the `.ay' format. These files are
essentially wrappers around bits of Z80 code which play music on the
Sinclair ZX Spectrum 128's sound hardware - either the beeper, or
(eponymously) the AY-3-8912 sound chip. Files using the Amstrad CPC
ports are also supported.

`aylet' has a curses-based interface, and `xaylet' has an X-based one.

One source of `.ay' files playable with aylet/xaylet is "Project AY"
on the World of Spectrum website:

http://www.worldofspectrum.org/

%package x11
Summary:	AY player for X11
Summary(pl.UTF-8):	Odtwarzacz AY dla X11
Group:		X11/Applications/Sound

%description x11
aylet plays music files in the `.ay' format. These files are
essentially wrappers around bits of Z80 code which play music on the
Sinclair ZX Spectrum 128's sound hardware - either the beeper, or
(eponymously) the AY-3-8912 sound chip. Files using the Amstrad CPC
ports are also supported.

`aylet' has a curses-based interface, and `xaylet' has an X-based one.

One source of `.ay' files playable with aylet/xaylet is "Project AY"
on the World of Spectrum website:

http://www.worldofspectrum.org/

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	CPPFLAGS="-I/usr/include/ncurses -DDRIVER_OSS" \

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install aylet $RPM_BUILD_ROOT%{_bindir}
install xaylet $RPM_BUILD_ROOT%{_bindir}
install aylet.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo ".so aylet.1" > $RPM_BUILD_ROOT%{_mandir}/man1/xaylet.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/aylet
%{_mandir}/man1/aylet*

%files x11
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xaylet
%{_mandir}/man1/xaylet*
