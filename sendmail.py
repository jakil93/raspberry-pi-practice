#coding: utf-8
import time
import os
from flask import Flask

class human(object):
    def __init__(self, name, age):
        self.name = str(name)
        self.age = str(age)

    def info(self):
        print "이름 : " + self.name + " / 나이 : " + self.age

app = Flask(__name__)

@app.route('/')
def main():
    return "main_page"

if(__name__ == "__main__"):
    app.run(debug=True, host="0.0.0.0", port=8888)
    kty = human("강태영", "25")
    temp = u"강태영"
    print temp[0]
    kty.info()

