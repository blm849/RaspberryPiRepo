# A simple Python program to turn an LED light on port 18 on and
# off. 
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
