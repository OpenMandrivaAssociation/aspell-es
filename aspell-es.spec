%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# WARNING
# To build this package, you may have to set LANG to es
# example : LANG=es; rpm -ba aspell-es.spec

%define src_ver 1.11-2
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languagelocal espanol
%define languageeng spanish
%define languageenglazy Spanish
%define languagecode es

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       1.11.2
Release:       %mkrel 1
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:           http://aspell.sourceforge.net/
License:       GPLv2
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
BuildRequires: aspell >= %{aspell_ver}
Requires:      aspell >= %{aspell_ver}

BuildRequires: locales-es

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary spell-es

# RedHat Stuff. is this right:
#Obsoletes: ispell-es, ispell-spanish

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
export LANG=es
# don't use configure macro
./configure

%make

%install
rm -fr %{buildroot}
export LANG=es

%makeinstall_std

chmod 644 README Copyright

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc README Copyright
%{_libdir}/aspell-%{aspell_ver}/*



%changelog
* Thu Sep 29 2011 Andrey Bondrov <abondrov@mandriva.org> 1.11.2-1mdv2012.0
+ Revision: 701865
- New version: 1.11.2

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9a.1-5
+ Revision: 662809
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9a.1-4mdv2011.0
+ Revision: 603204
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9a.1-3mdv2010.1
+ Revision: 518918
- rebuild

* Wed Jun 24 2009 Isabel Vallejo <isabel@mandriva.org> 1.9a.1-2mdv2010.0
+ Revision: 388882
- update to 1.9a.1
- update to 1.9a-1
- update to 1.9a-1
- update to 1.9a-1

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.50.2-12mdv2009.1
+ Revision: 350019
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.50.2-11mdv2009.0
+ Revision: 220373
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.50.2-10mdv2008.1
+ Revision: 182418
- provide enchant-dictionary

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-8mdv2007.0
+ Revision: 123245
- Import aspell-es

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-8mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.50.2-6mdk
- rebuild for new aspell

* Wed Jul 28 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.2-5mdk
- allow build on ia64

