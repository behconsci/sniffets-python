===============================
Python Library for sniffets.com
===============================

Install
-------

``pip install sniffets``


Usage
-----

::

    from sniffets import Sniffet

    sniff = Sniffet(token='ave32sde98ruj23if3riugrg')

    sniff.event('important event')


In Django Project, it is better to setup in settings.py and call the event tracker in views or wherever you want