#!/usr/bin/python

from time import sleep
from time import time

from adafruit_libs.Adafruit_TMP006.Adafruit_TMP006 import TMP006
import reportCoffee

distanceChangeOffset = 2
autoDistance = 0;
oldDistance = -99
fillingMode = False
measureTimeOffset = 5
measureStartTime = 0
measureStopTime = 0


class TempSensor(object):
	def __init__(self, address):
		self.device = TMP006(address)

	def measure_temp(self):
		return self.device.readObjTempC()
		

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

temp_sensor = TempSensor(0x40)


while True:

    sleep(2.0)

    distance = temp_sensor.measure_temp() 

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














