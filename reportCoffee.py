__author__ = 'd22'

import requests

_url = "http://127.0.0.1"


def makeRequest(time):
    payload = {'timestamp': time}
    r = requests.post(_url, data=payload)


makeRequest('1234567890')
