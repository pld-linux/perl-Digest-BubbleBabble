%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	BubbleBabble
Summary:	Digest::BubbleBabble Perl module - create bubble-babble fingerprints
Summary(pl):	Modu� perla Digest::BubbleBabble - tworz�cy odciski palca "bubble-babble"
Name:		perl-Digest-BubbleBabble
Version:	0.01
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digest::BubbleBabble takes a message digest (generated by either of
the MD5 or SHA-1 message digest algorithms) and creates a fingerprint
of that digest in "bubble babble" format. Bubble babble is a method of
representing a message digest as a string of "real" words, to make the
fingerprint easier to remember. The "words" are not necessarily real
words, but they look more like words than a string of hex characters.

%description -l pl
Modu� Digest::BubbleBabble przyjmuje skr�t wiadomo�ci (wygenerowany
algorytmem skr�tu MD5 lub SHA-1) i tworzy odcisk palca tego skr�tu w
formacie "bubble babble". Format ten to spos�b reprezentowania skr�tu
wiadomo�ci jako ci�gu "prawdziwych" s��w, aby uczyni� odcisk
�atwiejszym do zapami�tania. "S�owa" niekoniecznie s� prawdziwymi
s�owami, ale wygl�daj� jak s�owa bardziej ni� ci�g cyfr
szesnastkowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Digest/BubbleBabble.pm
%{_mandir}/man3/*
