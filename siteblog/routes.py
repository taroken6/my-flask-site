from flask import render_template, url_for
from siteblog import app


@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello world!<h1>'


@app.route('/projects')
def projects():
    return ''


@app.route('/blog')
def blog():
    return ''


@app.route('/register')
def register():
    return ''


@app.route('/login')
def login():
    return ''


@app.route('/logout')
def logout():
    return ''


@app.route('account')
def account():
    return ''
