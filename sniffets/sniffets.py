import grequests
import requests


class Sniffet(object):
    def __init__(self, token):
        self.url = 'http://207.154.212.31/inlight/track/%s/' % token

        # keep alive and connection pooling
        self.session = requests.session()

    def event(self, event_name):
        url = '%s?name=%s' % (self.url, event_name)
        req_ = [grequests.get(url, session=self.session)]
        r = grequests.map(req_)
        return r[0]