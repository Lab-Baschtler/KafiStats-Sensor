#!/usr/bin/python

from time import sleep

from hc_scr04 import hc_sr04_helper


def C_to_F(C):
    return C * (180.0 / 100.0) + 32.0

# ===========================================================================
# Example Code
# ===========================================================================


# Wait a short bit for sample averaging
while True:
    print "Pausing 2.0 s..."
    sleep(2.0)
    hc_sr04_helper.measureDistance()





