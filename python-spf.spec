Name:           python-spf
Version:        2.0.3
Release:        %mkrel 1
Epoch:		0
Summary:        Python module and programs for SPF (Sender Policy Framework)
Group:          Development/Python
License:        Python Software Foundation License
URL:            http://sourceforge.net/forum/forum.php?forum_id=596908
Source0:        pyspf-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
%py_requires -d
Requires:       python-pydns
Provides:	python-pyspf = %{epoch}:%{version}-%{release}
Provides:	pyspf = %{epoch}:%{version}-%{release}

%description
SPF does email sender validation.  For more information about SPF,
please see http://openspf.org

This SPF client is intended to be installed on the border MTA, checking
if incoming SMTP clients are permitted to send mail.  The SPF check
should be done during the MAIL FROM:<...> command.

%prep
%setup -q -n pyspf-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install -O2 --skip-build --root %{buildroot}
mv %{buildroot}/usr/bin/type99.py %{buildroot}/usr/bin/type99
mv %{buildroot}/usr/bin/spfquery.py %{buildroot}/usr/bin/pyspfquery
rm -f %{buildroot}/usr/bin/*.py{o,c}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG PKG-INFO README test
%{python_sitelib}/*
/usr/bin/type99
/usr/bin/pyspfquery

