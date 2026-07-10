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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle started as an extension to the AGU's own published styles,
providing extra facilities and improved usability. The AGU now publishes
satisfactory LaTeX materials of its own; the author of aguplus
recommends that users switch to using the official distribution.

