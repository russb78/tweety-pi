#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

pir = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir, GPIO.IN)

time.sleep(5)

def motion_sense(pir):
	"""An event detect 'callback' function to trigger the camera 
	using the pir GPIO pin connected to our PIR motion detector"""

	print "Motion detected!"
	time.sleep(1)
try:
	GPIO.add_event_detect(pir, GPIO.RISING, callback=motion_sense)
	print "PIR connected"
	while True:
		time.sleep(60)

except KeyboardInterrupt:
	print "\nQuitting"

finally:
	GPIO.cleanup()
