#coding: utf-8
import time, httplib, urllib, json

#set program info
KEY = "90c4f0c8-d7b4-38a2-a221-701ad624f172"
URL = "/weather/summary?version=1&lat=37.5714000000&lon=126.9658000000&stnid=108&appKey=" + KEY
header = {"Content-Type":"application/x-www-form-urlencoded",
            "Accept" : "application/json"}

con = httplib.HTTPConnection("apis.skplanetx.com")

try:
    con.request("GET", URL, "", header)
    resp = con.getresponse()
    result = json.load(resp.read())
    print result
    
except:
    print "Error! Connection Fail!"