#coding: utf-8

from flask import Flask
from flask import request

#make instance
app = Flask(__name__)

#main page
@app.route("/")
def main():
	args = request.args.get('name')
	return "여기는 "+ str(args) +" 홈페이지다"

#start server!
if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0", port = 8888)

