import sys

__author__ = 'd22'

import requests

def makeRequest(dbUrl, city, street, floor, duration):
    print sys.argv[1]
    payload = {'city': city, 'street': street, 'floor': floor, 'duration': duration}
    requests.post(dbUrl, data=payload)