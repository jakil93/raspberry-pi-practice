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

def controlLED(target):
	turnOnLED(target)
	time.sleep(1.2)
	turnOffLED(target)

#Send Mail function
def sendMail(givenmail, subject, content, email, pw):


	#set SMTP
	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.ehlo()
	smtp.starttls()

	#login
	smtp.login(email, pw)

	#append subject and content
	msg = MIMEText(content)
	msg['Subject'] = subject

	#receiver
	msg['To'] = givenmail
	smtp.sendmail(email, givenmail, msg.as_string())
	smtp.quit()

	#when complete, notify LED!
	controlLED(GPIO_LED)

#thread start function
def sendMailStart(receiver, subject, content, email, pw):
	result = "success"
	for x in xrange(1, 10):
		try:
			sendMail(str(receiver), str(x) + "번째" + str(subject), str(content), email, pw)
			print str(x) + "번째 메일 전송!"
		except Exception:
			result = "fail"

	return result

#make instance
app = Flask(__name__)

#main page
@app.route("/")
def main():
	return render_template("main.html")

#sendmail restful api
@app.route("/sendmail", methods=["POST"])
def sendmail():
	email = request.form['email']
	pw = request.form['pw']
	receiver = request.form['receiver']

	print email + ", " + pw + ", " + receiver

	'''
	th = Thread(target = sendMailStart, args=(receiver, "제목", "내용", email, pw))
	th.start()
	'''
	return sendMailStart(receiver, "제목", "내용", email, pw)

#shutdown restful api
@app.route("/shutdown")
def shutdown():
	shutdownServer()
	return "서버를 종료했습니다."

#start server!
if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0", port = 8888)

