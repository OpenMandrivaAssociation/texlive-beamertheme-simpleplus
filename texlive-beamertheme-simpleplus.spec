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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a simple and clean theme for LaTeX Beamer. It can
be used for academic and scientific presentations.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-simpleplus
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-simpleplus
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-simpleplus/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-simpleplus/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-simpleplus/beamertheme-simpleplus-sample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-simpleplus/beamertheme-simpleplus-sample.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-simpleplus/reference.bib
%{_datadir}/texmf-dist/tex/latex/beamertheme-simpleplus/beamercolorthemeSimplePlus.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-simpleplus/beamerfontthemeSimplePlus.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-simpleplus/beamerinnerthemeSimplePlus.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-simpleplus/beamerthemeSimplePlus.sty
