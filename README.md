# Django dnsmasq

**Description:** A Django application to create 
[dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html) configuration

**Copyright:** 2021-2022 Fabio Castelli (Muflone) <muflone@muflone.com>

**License:** GPL-3+

**Source code:** https://github.com/muflone/django-dnsmasq

**Documentation:** http://www.muflone.com/django-dnsmasq/

# Description

Django dnsmasq is a Django application to create configuration files
for dnsmasq.

# System Requirements

* Python >= 3.9
* dbus Python 1.2.x (https://pypi.org/project/dbus-python/)
* Django 4.0.x (https://pypi.org/project/Django/)
* django-macaddress 1.8.0 (https://pypi.org/project/django-macaddress/)
* Font Awesome free 5.15.4 (https://pypi.org/project/fontawesome-free/)

# Usage

To generate a dnsmasq configuration file you can use the integrated
management command:

    python manage.py create_configuration --filename <filename> [--description]

The `filename` arguments refers to the new dnsmasq configuration file
to be created.

The optional `descriptions` argument is meant to add comments in the
configuration file containing the descriptions of each item.
