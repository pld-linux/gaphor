Summary:	UML modeling environment written in Python
Summary(pl):	¦rodowisko modelowania UML oparte o Pythona
Name:		gaphor
Version:	0.8.0
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/gaphor/%{name}-%{version}.tar.gz
# Source0-md5:	3c320b5166523a3d0f21d52c15b1a509
Source1:	%{name}.desktop
Patch0:		%{name}-datadir.patch
URL:		http://gaphor.sourceforge.net/
BuildRequires:	X11-Xvfb
BuildRequires:	python-devel
BuildRequires:	python-diacanvas >= 0.14.3
BuildRequires:	python-pygtk-gtk >= 2.0.0
%pyrequires_eq	python-libs
Requires:	python-diacanvas >= 0.14.3
Requires:	python-pygtk-gtk >= 2.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gaphor is an easy to use modeling environment. This means that you are
able to create nice UML diagrams for documentation and to assist you
with design decisions. Gaphor will help you create your applications.

%description -l pl
Gaphor jest ³atwym w u¿yciu ¶rodowiskiem do projektowania UML. To
znaczy u³atwia tworzenie diagramów UML dla dokumentacji oraz pomaga w
podejmowaniu decyzji. Gaphor u³atwia pracê przy tworzeniu aplikacji.

%prep
%setup -q
#%patch0 -p0

%build
Xvfb :69 -nolisten tcp -ac -terminate >/dev/null 2>&1 &
xvfb_pid=${!}
DISPLAY=:69 \
	python setup.py build
kill ${xvfb_pid} >/dev/null 2>&1 || :

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

Xvfb :69 -nolisten tcp -ac -terminate >/dev/null 2>&1 &
xvfb_pid=${!}
DISPLAY=:69 \
	python setup.py install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT
kill ${xvfb_pid} >/dev/null 2>&1 || :

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README PKG-INFO NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/zope
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
