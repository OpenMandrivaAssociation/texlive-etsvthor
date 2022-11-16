Name:		texlive-etsvthor
Version:	48186
Release:	1
Summary:	Some useful abbreviations for members of e.t.s.v. Thor
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/etsvthor
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etsvthor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etsvthor.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
"e.t.s.v. Thor" stands for "Elektrotechnische Studievereniging
Thor", a study association of Electrical Engeering at the
Eindhoven University of Technology. The author of the package
tells us: "Most of our committees use LaTeX to create meeting
notes or other formal documents within the association. When
you create a lot of these documents (which I do a lot, since I
am currently the candidate Secretary of the new board), some
abbreviations are extremely useful. I discovered that more
people from our association are interested in using these, so I
decided to put them in a package, so they can use it very
easily too."

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/etsvthor
%doc %{_texmfdistdir}/doc/latex/etsvthor

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
