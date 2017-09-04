from flask import Flask, render_template
import dic

app = Flask(__name__)

articles = dic.articles()

@app.route('/')
def index():
	return 'hi dictionary'

@app.route('/articles')
def articles():
	return render_template('articles.html', t_articles = articles)

@app.route('/article/<int:id>')
def article(id):
	return render_template('article.html', id = id, articles= articles)
if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=8888)