Summary:	Write BASH-scripts by inserting comments, statements, tests, variables, builtins, etc
Name:		vim-plugin-bash
Version:	3.1.1
Release:	0.1
License:	vim
Group:		Applications/Editors/Vim
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-%{version}.zip
# Source0-md5:	cb189a5ef7b6c3b2c72a06c29c2c8445
Source1:	http://lug.fh-swf.de/vim/vim-bash/bash-hot-keys.pdf
# Source1-md5:	d6923526204a2920a155ec52eafbc947
Source2:	http://lug.fh-swf.de/vim/vim-doc/bashsupport.html
# Source2-md5:	1b410b4adbf7ec603b01e0e2f8a5406c
URL:		http://www.vim.org/scripts/script.php?script_id=213
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/vim
Requires:	vim-rt >= 4:7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Write BASH-scripts by inserting comments, statements, tests,
variables, builtins, etc

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}

install -d $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin
cp -a ftplugin/sh.vim $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin

install -d $RPM_BUILD_ROOT%{_vimdatadir}/plugin
cp -a plugin/bash-support.vim $RPM_BUILD_ROOT%{_vimdatadir}/plugin

install -d $RPM_BUILD_ROOT%{_vimdatadir}/doc
cp -a doc/bashsupport.txt $RPM_BUILD_ROOT%{_vimdatadir}/doc

install -d $RPM_BUILD_ROOT%{_vimdatadir}/bash-support
cp -a bash-support/{codesnippets,rc,scripts,templates,wordlists} \
	$RPM_BUILD_ROOT%{_vimdatadir}/bash-support

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -a %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
vim -c "helptags %{_vimdatadir}/doc" -c "q"

%postun
vim -c "helptags %{_vimdatadir}/doc" -c "q"

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%{_vimdatadir}/ftplugin/*
%{_vimdatadir}/plugin/*
%{_vimdatadir}/doc/*
%{_vimdatadir}/bash-support
