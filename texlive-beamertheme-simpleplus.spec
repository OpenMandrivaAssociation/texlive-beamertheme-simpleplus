Name:		texlive-beamertheme-simpleplus
Version:	64770
Release:	1
Summary:	A simple and clean theme for LaTeX beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-simpleplus
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-simpleplus.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-simpleplus.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a simple and clean theme for LaTeX
Beamer. It can be used for academic and scientific
presentations.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamertheme-simpleplus
%doc %{_texmfdistdir}/doc/latex/beamertheme-simpleplus

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
