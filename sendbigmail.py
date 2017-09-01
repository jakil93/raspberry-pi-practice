#coding: utf-8

import flask import Flask

#make instance
app = Flask(__name__)

#main page
@app.route("/")
def main():
	return "여기는 태영이 홈페이지다"

#start server!
if __name__ = "__main__":
	app.run(debug = True, host = "0.0.0.0", port = 8888)

