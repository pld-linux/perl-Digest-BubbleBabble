%define		pdir	Digest
%define		pnam	BubbleBabble
Summary:	Digest::BubbleBabble - create bubble-babble fingerprints
Summary(pl.UTF-8):	Digest::BubbleBabble - tworzenie odcisków palców "bubble-babble"
Name:		perl-Digest-BubbleBabble
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Digest/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4d7edd5b0a904db8194aa660d502fbe0
URL:		http://search.cpan.org/dist/Digest-BubbleBabble/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digest::BubbleBabble pPerl module takes a message digest (generated by
either of the MD5 or SHA-1 message digest algorithms) and creates a
fingerprint of that digest in "bubble babble" format.  Bubble babble
is a method of representing a message digest as a string of "real"
words, to make the fingerprint easier to remember.  The "words" are
not necessarily real words, but they look more like words than a
string of hex characters.

%description -l pl.UTF-8
Moduł Perla Digest::BubbleBabble przyjmuje skrót wiadomości
(wygenerowany algorytmem skrótu MD5 lub SHA-1) i tworzy odcisk palca
tego skrótu w formacie "bubble babble". Format ten to sposób
reprezentowania skrótu wiadomości jako ciągu "prawdziwych" słów, aby
uczynić odcisk łatwiejszym do zapamiętania. "Słowa" niekoniecznie są
prawdziwymi słowami, ale wyglądają jak słowa bardziej niż ciąg cyfr
szesnastkowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/Digest/BubbleBabble.pm
%{_mandir}/man3/Digest::BubbleBabble.3pm*
