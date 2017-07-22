import grequests
import requests


class Sniffet(object):
    def __init__(self, token):
        self.url = 'http://sniffets.com/sniff/event/%s/' % token

        # keep alive and connection pooling
        self.session = requests.session()

    def event(self, event_name, extra=None):
        payload = {'name': event_name, 'extra': extra}
        req_ = [grequests.post(self.url, session=self.session, json=payload)]
        grequests.imap(req_)
