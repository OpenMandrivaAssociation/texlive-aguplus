# revision 17156
# category Package
# catalog-ctan /macros/latex/contrib/aguplus
# catalog-date 2010-02-24 21:28:09 +0100
# catalog-license lppl
# catalog-version 1.6b
Name:		texlive-aguplus
Version:	1.6b
Release:	8
Summary:	Styles for American Geophysical Union
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aguplus
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aguplus.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aguplus.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle started as an extension to the AGU's own published
styles, providing extra facilities and improved usability. The
AGU now publishes satisfactory LaTeX materials of its own; the
author of aguplus recommends that users switch to using the
official distribution.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6b-2
+ Revision: 749151
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6b-1
+ Revision: 717804
- texlive-aguplus
- texlive-aguplus
- texlive-aguplus
- texlive-aguplus
- texlive-aguplus

