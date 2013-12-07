%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# WARNING
# To build this package, you may have to set LANG to es
# example :	LANG=es; rpm -ba aspell-es.spec

%define src_ver 1.11-2
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languagelocal espanol
%define languageeng spanish
%define languageenglazy Spanish
%define languagecode es

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	1.11.2
Release:	4
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.sourceforge.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= %{aspell_ver}
BuildRequires:	locales-es
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary spell-es
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

%build
export LANG=es
# don't use configure macro
./configure

%make

%install
export LANG=es
%makeinstall_std

chmod 644 README Copyright

%files
%doc README Copyright
%{_libdir}/aspell-%{aspell_ver}/*

