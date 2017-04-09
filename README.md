Python Library for https://apptrackly.com
=========

Install
--------------

``pip install apptrackly``


Usage
--------------

```
from apptrackly import AppTrack

apptrack = AppTrack(token='ave32sde98ruj23if3riugrg')

apptrack.event('important event')

```

In Django Project, it is better to setup in settings.py and call the event tracker in views or wherever you want