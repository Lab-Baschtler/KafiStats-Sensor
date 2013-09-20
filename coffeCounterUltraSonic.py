#!/usr/bin/python

from time import sleep
from time import time

from hc_scr04 import hc_sr04_helper

distanceChangeOffset = 1
oldDistance = -99
fillingMode = False
measureTimeOffset = 5
measureStartTime = 0
measureStopTime = 0


def hasDistanceIncreased(new, old):
    if (new >= old + distanceChangeOffset):
        return True

    return False


def hasDistanceDecreased(new, old):
    if (new <= old - distanceChangeOffset):
        return True

    return False


def isValidDuration(startTime, endTime):
    duration = endTime - startTime
    if (duration >= measureTimeOffset):
        return True

    return False


def isInitRun(distance):
    if (distance == -99):
        return True

    return False


# ===========================================================================
# Example Code
# ===========================================================================


# Wait a short bit for sample averaging
while True:

    print "Initialising Sensors ..."
    sleep(2.0)

    distance = hc_sr04_helper.measureDistance()

    if (isInitRun(oldDistance)):
        oldDistance = distance
        break

    if (hasDistanceDecreased(distance, oldDistance) and fillingMode == False):
        print "distance has decreased from " + oldDistance + " to " + distance + "assuming coffee is beeing filled"
        measureStartTime = time()
        fillingMode = True

    if (hasDistanceIncreased(distance, oldDistance)):
        print "distance has increased from " + oldDistance + " to " + distance + "assuming coffee has been removed"
        measureStopTime = time()
        fillingMode = False
        if (isValidDuration(measureStartTime, measureStopTime)):
            print "Coffee detected, send to database"

        else:
            print "No Coffee filling time too short"


















