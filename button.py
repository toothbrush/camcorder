#!/usr/bin/env python

# using pin 24

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)

while True:
        if ( GPIO.input(24) == False ):
                print "pressed?"
        sleep(0.1);
