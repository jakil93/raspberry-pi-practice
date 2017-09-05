#coding: utf-8
import sys, time
import Adafruit_DHT
import httplib, urllib

#API Key
KEY = "W3T1G60VYTY05ZCZ"


#set GPIO.BCM
humidity, temperature = Adafruit_DHT.read_retry(11, 3)

def sendData():
    if humidity is not None and temperature is not None:
        print('온도 : {0:0.1f}*  습도 : {1:0.1f}% 정보를 보냈습니다..'.format(temperature, humidity))
        # params = urllib.urlencode({'field1' : temperature,
        #                             'field2' : humidity,
        #                             'key' : KEY})
        params = urllib.urlencode("field1=" + str(temperature) + "&fiel2=" + str(humidity) + "&key=" + KEY)
        con = httplib.HTTPSConnection("api.thingspeak.com")

        try:
            con.request("POST", "/update")
            con.send(params)
            resp = con.getresponse()
            print resp.status, resp.reason
        except:
            print "Error! Connection Fail!"
    else:
        print('정보를 불러오는데 실패했습니다..')

while 1:
    sendData()
    time.sleep(5)

print "프로그램을 종료합니다."