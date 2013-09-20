#!/usr/bin/python

from time import sleep
from time import time

from hc_scr04 import hc_sr04_helper

distanceChangeOffset = 1
autoDistance = 0;
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

    sleep(2.0)

    distance = hc_sr04_helper.measureDistance()

    if (isInitRun(oldDistance)):
        print "Initialising coffee measure system ..."
        oldDistance = distance
        autoDistance = distance
        continue

    if (hasDistanceDecreased(distance, autoDistance) and fillingMode == False):
        print "distance has decreased from %f to %f assuming coffee is beeing filled" % (oldDistance, distance)
        measureStartTime = time()
        fillingMode = True

    if (hasDistanceIncreased(distance, oldDistance)):
        print "distance has increased from %f to %f assuming coffee has been removed" % (oldDistance, distance)
        measureStopTime = time()
        fillingMode = False
        if (isValidDuration(measureStartTime, measureStopTime)):
            print "Coffee detected, send to database"

        else:
            print "No Coffee filling time too short"

    oldDistance = distance














