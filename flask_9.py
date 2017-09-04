#coding: utf-8
from flask import Flask, render_template
import dic
import json

app = Flask(__name__)

arti = json.dumps(dic.articles(), ensure_ascii=False).encode('utf8')

@app.route('/')
def index():
	return 'hi dictionary'

@app.route('/articles')
def articles():
	return render_template('articles.html', articles = arti)

@app.route('/article/<int:id>')
def article(id):
	return render_template('article.html', id = id, articles= arti)
if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=8888)