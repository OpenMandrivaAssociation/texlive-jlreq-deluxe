Name:		texlive-jlreq-deluxe
Version:	64072
Release:	2
Summary:	Multi-weight Japanese font support for the jlreq class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jlreq-deluxe
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jlreq-deluxe.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jlreq-deluxe.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides multi-weight Japanese font support for
the jlreq class.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/platex/jlreq-deluxe
%{_texmfdistdir}/fonts/vf/public/jlreq-deluxe
%{_texmfdistdir}/fonts/tfm/public/jlreq-deluxe
%doc %{_texmfdistdir}/doc/platex/jlreq-deluxe

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
