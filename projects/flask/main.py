from flask import Flask, flash, redirect, render_template, \
     request, url_for
from zeptrion_air.main import zeptrion_air_blpr

app = Flask(__name__, template_folder='templates', static_url_path='/static')
app.register_blueprint(zeptrion_air_blpr)

@app.route('/home')
def home():
    return render_template('home.html', app_title='hallo Guido')

@app.route('/')
def framework():
    return render_template('index.html')

@app.route('/startseite')
def startseite():
    return render_template('startseite.html')