#!/usr/bin/python

from time import sleep
from time import time

from adafruit_libs.Adafruit_TMP006.Adafruit_TMP006 import TMP006
import reportCoffee


tempChangeOffset = 5
autoTemp = 0
oldTemp = -99
fillingMode = False
measureTimeOffset = 5
measureStartTime = 0
measureStopTime = 0


class TempSensor(object):
    def __init__(self, address):
        self.device = TMP006(address)

    def measure_temp(self):
        return self.device.readObjTempC()


def has_temperature_increased(new, old):
    if new >= old + tempChangeOffset:
        return True

    return False


def has_temperature_decreased(new, old):
    if new <= old - tempChangeOffset:
        return True

    return False


def is_valid_duration(startTime, endTime):
    duration = endTime - startTime
    if duration >= measureTimeOffset:
        return True

    return False


def is_initial_run(distance):
    if distance == -99:
        return True

    return False


def get_fill_duration():
    return measureStopTime - measureStartTime;



temp_sensor = TempSensor(0x40)

while True:

    sleep(1.5)

    temp = temp_sensor.measure_temp()

    if is_initial_run(oldTemp):
        print "Initialising infrared temerature coffee counting system, please stand by ..."
        oldTemp = temp
        autoTemp = temp
        continue

    print "Probing for coffee..."

    if has_temperature_increased(temp, autoTemp) and fillingMode is False:
        print "Temperature has increased from %f to %f assuming coffee is beeing filled" % (oldTemp, temp)
        measureStartTime = time()
        fillingMode = True

    if has_temperature_decreased(temp, oldTemp):
        print "Temperature has decreased from %f to %f assuming coffee has been removed" % (oldTemp, temp)
        measureStopTime = time()
        fillingMode = False
        if is_valid_duration(measureStartTime, measureStopTime):
            print "Coffee detected! Filling duration: %f. Sending data to database" % (get_fill_duration())
            reportCoffee.makeRequest(get_fill_duration())
        else:
            print "Time between changes to short, assuming no coffe has been taken."

    oldTemp = temp














