import flask
from flask import request

app = flask.Flask(__name__)

generalP = []

@app.route('/')
def home():
  return flask.render_template('index.html')

@app.route('/general', methods = ['GET', 'POST'])
def general():
  if(request.method == 'GET'):
    return flask.render_template('general.html', posts = generalP)
  else:
    post = request.json
    generalP.append(post)
    return flask.render_template('general.html', posts = generalP)

@app.route('/games')
def games():
  return flask.render_template('games.html')

@app.route('/tv')
def tv():
  return flask.render_template('tv.html')

@app.route('/books')
def books():
  return flask.render_template('books.html')

@app.route('/about')
def about():
  return flask.render_template('about.html')

if __name__ == "__main__":
  app.run()