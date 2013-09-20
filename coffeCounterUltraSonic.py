#!/usr/bin/python

from time import sleep
from time import time

from hc_scr04 import hc_sr04_helper
import reportCoffee
import sys

distanceChangeOffset = 2
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


def getFillDuration():
    return measureStopTime - measureStartTime;



# ===========================================================================
# Example Code
# ===========================================================================


# Wait a short bit for sample averaging


while True:

    sleep(2.0)

    distance = hc_sr04_helper.measureDistance()

    if (isInitRun(oldDistance)):
        print "Initialising ultrasonic coffee measure system, please stand by ..."
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
            print "Coffee detected, fill duration %f, send data to database" % (getFillDuration())
            reportCoffee.makeRequest(getFillDuration())
        else:
            print "No Coffee filling time too short"

    oldDistance = distance














