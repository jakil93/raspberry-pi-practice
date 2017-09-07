#coding: utf-8
import RPi.GPIO as GPIO
import time
import logger

from dht11.dht11 import DHT11
from flask import Flask, request, render_template, jsonify

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

#GPIO disable warnning!
GPIO.setwarnings(False)

#set GPIO Pins
LED_RED = 8
LED_YELLOW = 10
TRIGGER = 11
ECHO = 7

#set logger file name
LOGGER_FILE_NAME = "SensorHandler"

#set GPIO direction (IN / OUT)
GPIO.setup(LED_RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_YELLOW, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def distance():
	# set Trigger to HIGH
	GPIO.output(TRIGGER, True)

	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(TRIGGER, False)

	StartTime = time.time()
	StopTime = time.time()

	# save StartTime
	while GPIO.input(ECHO) == 0:
		StartTime = time.time()

	# save time of arrival
	while GPIO.input(ECHO) == 1:
		StopTime = time.time()

	# time difference between start and arrival
	TimeElapsed = StopTime - StartTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	distance = (TimeElapsed * 34300) / 2

	return distance
def getTemperatureAndHumidit():
	instance = DHT11(pin=5)
	result = instance.read()
	return result.temperature, result.humidity


#get flask instance
app = Flask(__name__)

@app.route("/dht11", methods=["GET"])
def dht11():
	temp, humidity = getTemperatureAndHumidit()

	if temp == 0 and humidity == 0:
		result = "fail"
	else:
		result = "success"

	data = jsonify(temp = temp, humidity = humidity, result = result)
	return data

@app.route('/ultrasonic', methods=["GET"])
def ultrasonic():
	dist = distance()
	data = jsonify(dist=dist, name="kty")
	return data

@app.route("/ledon", methods=["GET"])
def ledon():

	target = str( request.args.get("target") )
	logger.log(LOGGER_FILE_NAME, "led on.. target : " + target)

	if target == "red":
		GPIO.output(LED_RED, GPIO.HIGH)
		result = "ledred turn on"
	elif target == "yellow":
		GPIO.output(LED_YELLOW, GPIO.HIGH)
		result = "ledyellow turn on"
	else:
		result = "fail"

	return result

@app.route("/ledoff", methods=["GET"])
def ledoff():

	target = str( request.args.get("target") )
	logger.log(LOGGER_FILE_NAME, "led off.. target : " + target)
	if target == "red":
		GPIO.output(LED_RED, GPIO.LOW)
		result = "ledred turn off"
	elif target == "yellow":
		GPIO.output(LED_YELLOW, GPIO.LOW)
		result = "ledyellow turn off"
	else:
		result = "fail"

	return result

@app.route("/ledalloff", methods=["GET"])
def ledalloff():
	logger.log(LOGGER_FILE_NAME, "led all off")
	GPIO.output(LED_RED, GPIO.LOW)
	GPIO.output(LED_YELLOW, GPIO.LOW)
	return "all led turn off"

@app.route("/ledallon", methods=["GET"])
def ledallon():
	logger.log(LOGGER_FILE_NAME, "led all on")
	GPIO.output(LED_RED, GPIO.HIGH)
	GPIO.output(LED_YELLOW, GPIO.HIGH)
	return "all led turn on"

if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0", port = 8888)
	GPIO.cleanup()
	print "서버를 종료합니다."