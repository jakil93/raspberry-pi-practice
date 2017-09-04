#Libraries
import RPi.GPIO as GPIO
import time
from flask import Flask, jsonify, render_template
 
#GPIO Mode (BOARD / BCM)
GPIO.setwarnings(False)
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

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('ultrasonic.html')

@app.route('/ajax')
def ajax():
	dist = distance()
	data = jsonify(dist=dist, name="kty")
	return data

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8888)