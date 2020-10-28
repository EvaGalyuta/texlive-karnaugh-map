Name:		karnaugh-map
Version:	1.1
Release:	1
Summary:	 This package draws [karnaugh maps](https://en.wikipedia.org/wiki/Karnaugh_map) with 2, 3, 4, 5, and 6 variables.
Group:		Publishing
URL:		https://ctan.org/pkg/karnaugh-map
License:	Free license not otherwise listed
Source0:	http://ctan.altspu.ru/systems/texlive/tlnet/archive/karnaugh-map.tar.xz 
Source1:	http://ctan.altspu.ru/systems/texlive/tlnet/archive/karnaugh-map.doc.tar.xz 
Source2:       http://ctan.altspu.ru/systems/texlive/tlnet/archive/karnaugh-map.source.tar.xz 
BuildArch:	noarch
BuildRequires: texlive-tlpkg
Requires(pre): texlive-tlpkg
Requires(post):texlive-kpathsea	

%description
This package draws [karnaugh maps](https://en.wikipedia.org/wiki/Karnaugh_map) with 2, 3, 4, 5, and 6 variables.
It also contains commands for filling the karnaugh map with terms semi-automatically or manually.
Last but not least it contains commands for drawing implicants on top of the map.

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/karnaugh-map
%doc %{_texmfdistdir}/doc/latex/makecmds/README.md
%doc %{_texmfdistdir}/doc/latex/makecmds/karnaugh-map.pdf
#- source
%doc %{_texmfdistdir}/source/latex/makecmds/karnaugh-map.dtx
%doc %{_texmfdistdir}/source/latex/makecmds/karnaugh-map.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
