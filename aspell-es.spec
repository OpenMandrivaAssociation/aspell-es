%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# WARNING
# To build this package, you may have to set LANG to es
# example : LANG=es; rpm -ba aspell-es.spec

%define src_ver 1.9a-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languagelocal espanol
%define languageeng spanish
%define languageenglazy Spanish
%define languagecode es

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       1.9a.1
Release:       %mkrel 1
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:           http://aspell.sourceforge.net/
License:       GPL
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
rm -fr $RPM_BUILD_ROOT
export LANG=es

%makeinstall_std

chmod 644 README Copyright

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Copyright
%{_libdir}/aspell-%{aspell_ver}/*


