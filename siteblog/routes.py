from flask import render_template, url_for, redirect
from siteblog import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')


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


@app.route('/account')
def account():
    return ''
