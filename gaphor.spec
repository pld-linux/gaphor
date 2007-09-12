Summary:	UML modeling environment written in Python
Summary(pl.UTF-8):	Środowisko modelowania UML oparte o Pythona
Name:		gaphor
Version:	0.12.2
Release:	0.1
License:	GPL
Group:		Applications/Engineering
Source0:	http://pypi.python.org/packages/source/g/gaphor/%{name}-%{version}.tar.gz
# Source0-md5:	00a6ab4469931d7ed908960f4bb2360e
Source1:	%{name}.desktop
URL:		http://gaphor.devjavu.com/
BuildRequires:	python-devel
BuildRequires:	python-pygtk-gtk >= 2.8.4
%pyrequires_eq	python-libs
Requires:	python-gaphas >= 0.3.3
Requires:	python-pygtk-gtk >= 2.8.4
Requires:	Zope-Component
Requires:	Zope-Interface
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
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

%{__python} setup.py install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%py_postclean

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc README PKG-INFO NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}*egg*
%{_desktopdir}/%{name}.desktop
