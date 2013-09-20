import sys
import requests

__author__ = 'd22'


def getDBUrl():
    try:
        return sys.argv[1]
    except IndexError:
        return ''


def getCity():
    try:
        return sys.argv[2]
    except IndexError:
        return 'Unknown City'


def getStreet():
    try:
        return sys.argv[3]
    except IndexError:
        return 'Unknown Street'


def getFloor():
    try:
        return sys.argv[4]
    except IndexError:
        return 'Unknown Floor'


def makeRequest(duration):
    payload = {'city': getCity(), 'street': getStreet(), 'floor': getFloor(), 'duration': duration}
    requests.post(getDBUrl(), data=payload)