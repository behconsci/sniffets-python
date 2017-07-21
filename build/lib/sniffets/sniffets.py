import grequests
import requests


class Sniffet(object):
    def __init__(self, token):
        self.url = 'http://sniffets.com/sniff/event/%s/' % token

        # keep alive and connection pooling
        self.session = requests.session()

    def event(self, event_name, extra=None):
        url = '%s?name=%s' % (self.url, event_name)
        payload = {'name': event_name, 'extra': extra}
        req_ = [grequests.post(url, session=self.session, data=payload)]
        grequests.imap(req_)
