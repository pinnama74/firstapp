from flask import render_template, flash, redirect, url_for
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Siddhu'}
    return render_template('main.html', title='Home', user=user)
