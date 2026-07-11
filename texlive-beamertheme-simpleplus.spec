%global tl_name beamertheme-simpleplus
%global tl_revision 73362

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A simple and clean theme for LaTeX beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-simpleplus
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-simpleplus.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-simpleplus.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a simple and clean theme for LaTeX Beamer. It can
be used for academic and scientific presentations.

