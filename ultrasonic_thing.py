#coding: utf-8
#Libraries
import RPi.GPIO as GPIO
import time
import httplib, urllib
from flask import Flask, jsonify, render_template

#API Key
KEY = "4HVWDTTFGPG3EX3D"
headers = {"Content-Type":"application/x-www-form-urlencoded",
            "Accept" : "text/plain"}


#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

#GPIO disable warnning!
GPIO.setwarnings(False)

#set GPIO Pins
GPIO_TRIGGER = 7
GPIO_ECHO = 5
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
while 1:
    dist = distance()
    params = urllib.urlencode({'field1' : dist,
                                'key' : KEY})
    con = httplib.HTTPConnection("api.thingspeak.com")

    try:
        con.request("POST", "/update", params, headers)
        resp = con.getresponse()
        print resp.status, resp.reason
    except:
        print "Error! Connection Fail!"
    print "측정된 거리 : " + str(dist)
    time.sleep(5)