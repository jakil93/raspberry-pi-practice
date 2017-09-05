#coding: utf-8
import sys, time
import Adafruit_DHT
import httplib, urllib

#API Key
KEY = "W3T1G60VYTY05ZCZ"
headers = {"Content-Type":"application/x-www-form-urlencoded",
            "Accept" : "text/plain"}

#set GPIO.BCM


def sendData():
    if humidity is not None and temperature is not None:
        print('온도 : {0:0.1f}*  습도 : {1:0.1f}% 정보를 보냈습니다..'.format(temperature, humidity))
    else:
        print('정보를 불러오는데 실패했습니다..')

while 1:
    humidity, temperature = Adafruit_DHT.read_retry(11, 3)
    params = urllib.urlencode({'field1' : temperature,
                                'key' : KEY})
    
    con = httplib.HTTPConnection("api.thingspeak.com")

    try:
        con.request("POST", "/update", params, header)
        resp = con.getresponse()
        print resp.status, resp.reason
    except:
        print "Error! Connection Fail!"
    time.sleep(5)

print "프로그램을 종료합니다."