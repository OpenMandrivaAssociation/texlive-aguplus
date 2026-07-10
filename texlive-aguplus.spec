%global tl_name aguplus
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6b
Release:	%{tl_revision}.1
Summary:	Styles for American Geophysical Union
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aguplus
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aguplus.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aguplus.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle started as an extension to the AGU's own published styles,
providing extra facilities and improved usability. The AGU now publishes
satisfactory LaTeX materials of its own; the author of aguplus
recommends that users switch to using the official distribution.

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
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/aguplus
%dir %{_datadir}/texmf-dist/doc/latex/aguplus
%dir %{_datadir}/texmf-dist/tex/latex/aguplus
%{_datadir}/texmf-dist/bibtex/bst/aguplus/agu.bst
%{_datadir}/texmf-dist/bibtex/bst/aguplus/agu04.bst
%{_datadir}/texmf-dist/bibtex/bst/aguplus/agufull.bst
%{_datadir}/texmf-dist/bibtex/bst/aguplus/agufull04.bst
%doc %{_datadir}/texmf-dist/doc/latex/aguplus/README
%doc %{_datadir}/texmf-dist/doc/latex/aguplus/README.aguplus
%doc %{_datadir}/texmf-dist/doc/latex/aguplus/aguplus.pdf
%doc %{_datadir}/texmf-dist/doc/latex/aguplus/aguplus.tex
%doc %{_datadir}/texmf-dist/doc/latex/aguplus/changes.v16b
%doc %{_datadir}/texmf-dist/doc/latex/aguplus/geophys.tex
%doc %{_datadir}/texmf-dist/doc/latex/aguplus/sample.bib
%doc %{_datadir}/texmf-dist/doc/latex/aguplus/samplus.tex
%{_datadir}/texmf-dist/tex/latex/aguplus/aguplus.cls
%{_datadir}/texmf-dist/tex/latex/aguplus/aguplus.sty
%{_datadir}/texmf-dist/tex/latex/aguplus/agupp.sty
