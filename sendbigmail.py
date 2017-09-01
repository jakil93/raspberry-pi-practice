#coding: utf-8

import RPi.GPIO as GPIO
import time
import smtplib

from email.mime.text import MIMEText
from threading import Thread
from flask import Flask, request, render_template


#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO disable warnning!
GPIO.setwarnings(False)

#set GPIO Pins
#GPIO_TRIGGER = 18
#GPIO_ECHO = 24
GPIO_LED = 14
GPIO_LED2 = 15


#set GPIO direction (IN / OUT)
#GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GPIO_LED2, GPIO.OUT, initial=GPIO.LOW)


def shutdownServer():
	func = request.environ.get("werkzeug.server.shutdown")
	if func is None:
		raise RuntimeError("Not running with the Werkzeug Server")
	func()

def turnOnLED(target):
    GPIO.output(target, GPIO.HIGH)

def turnOffLED(target):
    GPIO.output(target, GPIO.LOW)

#Send Mail function
def sendMail(givenmail, subject, content):

	#when start turn on led
	turnOnLED(GPIO_LED)
	#set SMTP
	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.ehlo()
	smtp.starttls()

	#login
	smtp.login('ares9046@gmail.com','netgear12')

	#append subject and content
	msg = MIMEText(content)
	msg['Subject'] = subject

	#receiver
	msg['To'] = givenmail
	smtp.sendmail('ares9046@gmail.com', givenmail, msg.as_string())
	smtp.quit()

	#when complete turn off led
	turnOffLED(GPIO_LED)

#thread start function
def sendMailStart():
	for x in xrange(1,100):
		sendMail("jakil93@naver.com", "테스트제목", "내용")

#make instance
app = Flask(__name__)

#main page
@app.route("/")
def main():

	email = request.args.get('email')
	pw = request.args.get('pw')
	receiver = request.args.get('receiver')

	data = {
		'email' : email,
		'pw' : pw,
		'receiver' : receiver
	}

	th = Thread(target = sendMailStart)
	th.start()

	return render_template("main.html", **data)

#shutdown restful api
@app.route("/shutdown")
def shutdown():
	shutdownServer()
	return "서버를 종료했습니다."

#start server!
if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0", port = 8888)

