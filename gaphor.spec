Summary:	UML modeling environment written in Python
Summary(pl):	¦rodowisko modelowania UML oparte o Pythona
Name:		gaphor
Version:	0.7.0
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/gaphor/%{name}-%{version}.tar.gz
# Source0-md5:	ed771389b03f4a8ab06b4021263dbe74
Source1:	%{name}.desktop
Patch0:		%{name}-datadir.patch
URL:		http://gaphor.sourceforge.net/
BuildRequires:	X11-Xvfb
BuildRequires:	python-devel
BuildRequires:	python-pygtk-gtk >= 2.0.0
BuildRequires:	python-diacanvas >= 0.13
Requires:	python-pygtk-gtk >= 2.0.0
Requires:	python-diacanvas >= 0.13
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
%patch0 -p1

%build
/usr/X11R6/bin/Xvfb :69 -nolisten tcp -ac -terminate >/dev/null 2>&1 &
xvfb_pid=${!}
DISPLAY=:69 \
	python setup.py build
kill ${xvfb_pid} >/dev/null 2>&1 || :

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

/usr/X11R6/bin/Xvfb :69 -nolisten tcp -ac -terminate >/dev/null 2>&1 &
xvfb_pid=${!}
DISPLAY=:69 \
	python setup.py install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT
		--build-dir=$(pwd)
kill ${xvfb_pid} >/dev/null 2>&1 || :

cat <<EOF > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/usr/bin/python -O
import gaphor
gaphor.main()
EOF

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README PKG-INFO NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{name}
%dir %{py_sitescriptdir}/%{name}/ui
%dir %{py_sitescriptdir}/%{name}/misc
%dir %{py_sitescriptdir}/%{name}/diagram
%dir %{py_sitescriptdir}/%{name}/UML
%{py_sitescriptdir}/%{name}/*.py[oc]
%{py_sitescriptdir}/%{name}/ui/*.py[oc]
%{py_sitescriptdir}/%{name}/misc/*.py[oc]
%{py_sitescriptdir}/%{name}/diagram/*.py[oc]
%{py_sitescriptdir}/%{name}/UML/*.py[oc]
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
