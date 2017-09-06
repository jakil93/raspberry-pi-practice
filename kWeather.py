# coding: utf-8
import httplib, urllib, json

#set params
params = {"version" : "1",
          "city" : "부산",
          "county" : "수영구",
          "village" : "광안동",
          }

# set program info

names = {'name':'강태영'}

KEY = "90c4f0c8-d7b4-38a2-a221-701ad624f172"
URL = "/weather/current/minutely?"
header = {"appKey" : KEY, "Accept" : "application/json; charset=UTF-8"}

con = httplib.HTTPConnection("apis.skplanetx.com")

params = urllib.urlencode(params)
con.request("GET", URL + params, None, header)
resp = con.getresponse()

result = resp.read()

datas = json.loads(result)
datas = json.dumps(datas, ensure_ascii=False)
print datas