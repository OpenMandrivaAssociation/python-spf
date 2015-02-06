Name:           python-spf
Version:        2.0.3
Release:        5
Epoch:		0
Summary:        Python module and programs for SPF (Sender Policy Framework)
Group:          Development/Python
License:        Python Software Foundation License
URL:            http://sourceforge.net/forum/forum.php?forum_id=596908
Source0:        pyspf-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:	python
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
%{_bindir}/*



%changelog
* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 0:2.0.3-4mdv2011.0
+ Revision: 593154
- python-devel is not requried
- rebuild for py 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0:2.0.3-3mdv2010.0
+ Revision: 442487
- rebuild

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 0:2.0.3-2mdv2009.1
+ Revision: 324130
- rebuild

* Tue Sep 16 2008 Luca Berra <bluca@mandriva.org> 0:2.0.3-1mdv2009.0
+ Revision: 285251
- import python-spf


* Mon Sep 08 2008 Luca Berra <bluca@mandriva.org> 2.0.3-1mdv2008.1
- mandriva port

* Mon Jan 15 2007 Stuart Gathman <stuart@bmsi.com> 2.0.3-1
- pyspf requires pydns, python-pyspf requires python-pydns
- Record matching mechanism and add to Received-SPF header.
- Test for RFC4408 6.2/4, and fix spf.py to comply.
- Test for type SPF (type 99) by default in harsh mode only.
- Permerror for more than one exp or redirect modifier.
- Parse op= modifier
* Sat Dec 30 2006 Stuart Gathman <stuart@bmsi.com> 2.0.2-1
- Update openspf URLs
- Update Readme to better describe available pyspf interfaces
- Add basic description of type99.py and spfquery.py scripts
- Add usage instructions for type99.py DNS RR type conversion script
- Add spfquery.py usage instructions
- Incorporate downstream feedback from Debian packager
- Fix key-value quoting in get_header
* Fri Dec 08 2006 Stuart Gathman <stuart@bmsi.com> 2.0.1-1
- Prevent cache poisoning attack
- Prevent malformed RR attack
- Update license on a few files we missed last time
* Mon Nov 20 2006 Stuart Gathman <stuart@bmsi.com> 2.0-1
- Completed RFC 4408 compliance
- Added spf.check2 for RFC 4408 compatible result codes
- Full IP6 support
- Fedora Core compatible RPM spec file
- Update README, licenses
* Wed Sep 26 2006 Stuart Gathman <stuart@bmsi.com> 1.8-1
- YAML test suite syntax
- trailing dot support (RFC4408 8.1)
* Tue Aug 29 2006 Sean Reifschneider <jafo@tummy.com> 1.7-1
- Initial RPM spec file.
