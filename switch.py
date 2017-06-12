# A simple Python program to check to see if a button attached
# to GPIO 18 and if it is, print that it was pressed.
# Taken from http://razzpisampler.oreilly.com/ch07.html

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
