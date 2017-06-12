# A simple Python program to check to see if a button attached
# to GPIO 18 and if it is, print that it was pressed.
# Taken from http://razzpisampler.oreilly.com/ch03.html#SEC7.1

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while (True):
    GPIO.output(18, True)
    time.sleep(0.5)
        GPIO.output(18, False)
        time.sleep(0.5)
