Summary:	UML modeling environment written in Python
Summary(pl):	¦rodowisko modelowania UML oparte o Pythona
Name:		gaphor
Version:	0.5.0
Release:	4
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/gaphor/%{name}-%{version}.tar.gz
# Source0-md5:	761451126030e3171d0b20fee829d800
Source1:	%{name}.desktop
Patch0:		%{name}-pluginsdir.patch
Patch1:		%{name}-datadir.patch
URL:		http://gaphor.sourceforge.net/
BuildRequires:	python-devel
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
%patch0
%patch1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

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
