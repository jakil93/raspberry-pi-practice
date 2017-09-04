#coding: utf-8
import RPi.GPIO as GPIO
import time
from dht11.dht11 import DHT11

GPIO.setwarning(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

#get instance DHT11
instance = DHT11(pin = 8)
result = instance.read()

if result.is_vaild():
	print("온도 : %dC" %result.temperature)
	print("습도 : %d" %result.humidity)
else:
	print("Error : %d" %result.error_code)