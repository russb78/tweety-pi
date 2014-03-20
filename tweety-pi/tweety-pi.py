#!/usr/bin/env python

import RPi.GPIO as GPIO
import random
import time
import tweepy
import picamera
import os

### GPIO SETTINGS ###
# Set the pin for our PIR
# Don't forget to configure the PIR GPIO pin as an input
pir = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir, GPIO.IN)

### TWITTER SETTINGS ###
# Set your access keys as configured via https://apps.twitter.com
# Keep these details a secret (the speech marks are required) 
api_key = 'api_key'
api_secret = 'api_secret'
access_token = 'access_token'
token_secret = 'token_secret'
# Initiate the OAuth process
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, token_secret)
api = tweepy.API(auth)
my_twitter = api.me()
# Confirm your account is working
print my_twitter.name, "is connected! Press CTRL + C to quit."
# Three twitter statuses. We'll pick one at random to accompany our pic
tweet_text = ['Another shot taken with tweety-pi!',
				'Just spotted with my Raspberry Pi', 
				'Snapped automagically with my Rasperry Pi camera!']

### CAMERA SETTINGS ###
# Configure the camera, its resolution and give it a second to settle
camera = picamera.PiCamera()
cam_res = (1024, 768)
camera.led = False # We don't want to scare the birdies, so turn the LED off!
pics_taken = 0
time.sleep(1)

### MAIN FUNCTIONS ###

def motion_sense(pir):
	"""An event detect 'callback' function to trigger the camera 
	using the PIR's GPIO pin connected to our PIR motion detector"""
	print "Motion detected... Taking picture!"
	take_picture(cam_res)

def take_picture(resolution):
	"""A function to take a number of camera frames using picamera"""
	global pics_taken
	camera.resolution = resolution
	# Capture a sequence of frames
	camera.capture(os.path.join('pics', 'image_' + str(pics_taken) + '.jpg'))
	pics_taken += 1
	print "Picture taken! Tweeting it..."""
	update_twitter()

def update_twitter():
	"""A function that loads a picture and updates your twitter status"""
	api.update_with_media(os.path.join(
	'pics', 'image_' + str(pics_taken -1) + '.jpg'),
	status = random.choice(tweet_text))
	print "Status updated!"
	#We don't want to tweet more than once per minute!
	time.sleep(60)

### MAIN PROGRAM LOOP ###

try:
	# When the pir GPIO pin detects activity, it calls our function
	GPIO.add_event_detect(pir, GPIO.RISING, callback=motion_sense)
	# We want the above event to stay alive forever
	# so let's create an infinite loop
	while True:
		time.sleep(60)

# The loop is broken if we press CRTL+C
except KeyboardInterrupt:
	print "\nQuitting"
	
# Regardless of what causes the script to end, the 'finally' condition
# will always be met, meaning we can close gracefully
finally:
	camera.close()
	GPIO.cleanup()
