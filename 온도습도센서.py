#coding: utf-8
import RPi.GPIO as GPIO
from dht11.dht11 import DHT11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

instance = DHT11(pin = 5)
result = instance.read()

while True:
	try:
		msg = ""
		time.sleep(2)
		if result.is_valid():
			msg += "온도 : " + str( result.temperature) + "C\n"
			msg += "습도 : " + str( result.humidity) + "\n"
		else:
			msg += "Error : " + str( result.error_code)
		print msg, "현재시각 : ", time.time()
	except KeyboardInterrupt:
		GPIO.cleanup()
		break
