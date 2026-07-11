%global tl_name jlreq-deluxe
%global tl_revision 78373

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6.0
Release:	%{tl_revision}.1
Summary:	Multi-weight Japanese font support for the jlreq class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/jlreq-deluxe
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jlreq-deluxe.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jlreq-deluxe.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides multi-weight Japanese font support for the jlreq
class.

