import time
import datetime as d
import os

def log(logFileName ,msg):
	os.system("echo " + msg + "\(" + getCurrentTime() +"\) >> "+ logFileName +".txt")
        print msg

def getCurrentTime():
	now = d.datetime.now()
	return now.strftime("%Y-%m-%d:%H:%M:%S")