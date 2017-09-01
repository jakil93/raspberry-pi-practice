#coding: utf-8
import RPi.GPIO as GPIO
import time

from flask import Flask, request, render_template

GPIO.setmode(GPIO.BCM)

#GPIO disable warnning!
GPIO.setwarnings(False)

#set GPIO Pins
LED_RED = 14
LED_YELLOW = 15


#set GPIO direction (IN / OUT)
GPIO.setup(LED_RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_YELLOW, GPIO.OUT, initial=GPIO.LOW)

#get flask instance
app = Flask(__name__)

@app.route("/ledon", methods=["GET"])
def ledon():

	target = str( request.args.get("target") )
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
	if target == "red":
		GPIO.output(LED_RED, GPIO.LOW)
		result = "ledred turn off"
	elif target == "yellow":
		GPIO.output(LED_YELLOW, GPIO.LOW)
		result = "ledyellow turn off"
	else:
		result = "fail"

	return result


if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0", port = 8888)
	print "이건언제 뜸?"