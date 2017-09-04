#coding: utf-8
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/posttest", methods=["POST"])
def posttest():
	name = request.form['name']
	print "받은 요청 : " + name
	return render_template("flask_6.html", name = name)

@app.route("/")
def main():
	return render_template("main2.html")

if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0", port = 8888)
	print "서버를 종료합니다."