#coding: utf-8
import RPi.GPIO as GPIO
import time
import datetime as d
import os

#Set the GPIO Pin
LED = 8

#initialize GPIO Module
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)

def turnOn():
        GPIO.output(LED, GPIO.HIGH)
        addLog("LED가 커졌습니다.")

def turnOff():
        GPIO.output(LED, GPIO.LOW)
        addLog("LED가 꺼졌습니다.")

def addLog(msg):
	os.system("echo " + msg + "\(" + getCurrentTime() +"\) >> ledlog.txt")
        print msg

def getCurrentTime():
	now = d.datetime.now()
	return now.strftime("%Y-%m-%d:%H:%M:%S")


addLog("프로그램을 실행합니다.")

while True:
        try:
                turnOn()
                time.sleep(3)

                turnOff()
                time.sleep(3)

        except KeyboardInterrupt:
		GPIO.cleanup()
		addLog("프로그램을 종료합니다.")
		break

