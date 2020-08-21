from flask import render_template, url_for
from siteblog import app


@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello world!<h1>'
