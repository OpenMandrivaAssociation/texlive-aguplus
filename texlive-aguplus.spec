# revision 17156
# category Package
# catalog-ctan /macros/latex/contrib/aguplus
# catalog-date 2010-02-24 21:28:09 +0100
# catalog-license lppl
# catalog-version 1.6b
Name:		texlive-aguplus
Version:	1.6b
Release:	1
Summary:	Styles for American Geophysical Union
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aguplus
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aguplus.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aguplus.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This bundle started as an extension to the AGU's own published
styles, providing extra facilities and improved usability. The
AGU now publishes satisfactory LaTeX materials of its own; the
author of aguplus recommends that users switch to using the
official distribution.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/aguplus/agu.bst
%{_texmfdistdir}/bibtex/bst/aguplus/agu04.bst
%{_texmfdistdir}/bibtex/bst/aguplus/agufull.bst
%{_texmfdistdir}/bibtex/bst/aguplus/agufull04.bst
%{_texmfdistdir}/tex/latex/aguplus/aguplus.cls
%{_texmfdistdir}/tex/latex/aguplus/aguplus.sty
%{_texmfdistdir}/tex/latex/aguplus/agupp.sty
%doc %{_texmfdistdir}/doc/latex/aguplus/README
%doc %{_texmfdistdir}/doc/latex/aguplus/README.aguplus
%doc %{_texmfdistdir}/doc/latex/aguplus/aguplus.pdf
%doc %{_texmfdistdir}/doc/latex/aguplus/aguplus.tex
%doc %{_texmfdistdir}/doc/latex/aguplus/changes.v16b
%doc %{_texmfdistdir}/doc/latex/aguplus/geophys.tex
%doc %{_texmfdistdir}/doc/latex/aguplus/sample.bib
%doc %{_texmfdistdir}/doc/latex/aguplus/samplus.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
