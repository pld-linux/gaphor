Summary:	UML modeling environment written in Python
Summary(pl.UTF-8):   Środowisko modelowania UML oparte o Pythona
Name:		gaphor
Version:	0.8.1
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/gaphor/%{name}-%{version}.tar.gz
# Source0-md5:	60768b5ff8163b90cba6e936144644cc
Source1:	%{name}.desktop
URL:		http://gaphor.sourceforge.net/
BuildRequires:	xorg-xserver-Xvfb
BuildRequires:	python-devel
BuildRequires:	python-diacanvas >= 0.14.4
BuildRequires:	python-pygtk-gtk >= 2.8.4
%pyrequires_eq	python-libs
Requires:	python-diacanvas >= 0.14.4
Requires:	python-pygtk-gtk >= 2.8.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gaphor is an easy to use modeling environment. This means that you are
able to create nice UML diagrams for documentation and to assist you
with design decisions. Gaphor will help you create your applications.

%description -l pl.UTF-8
Gaphor jest łatwym w użyciu środowiskiem do projektowania UML. To
znaczy ułatwia tworzenie diagramów UML dla dokumentacji oraz pomaga w
podejmowaniu decyzji. Gaphor ułatwia pracę przy tworzeniu aplikacji.

%prep
%setup -q

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
