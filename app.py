import flask
from flask import request

app = flask.Flask(__name__)

generalP = []

@app.route('/')
def home():
  return flask.render_template('index.html')

@app.route('/general')
def general():
  return flask.render_template('general.html')

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