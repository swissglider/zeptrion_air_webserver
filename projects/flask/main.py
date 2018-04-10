from flask import Flask, flash, jsonify, redirect, render_template, \
     request, url_for
from zeptrion_air.main import zeptrion_air_blpr
from time import sleep

app = Flask(__name__, template_folder='templates', static_url_path='/static')
app.register_blueprint(zeptrion_air_blpr)

app.static_folder=app.root_path + '/static2'

@app.route('/home')
def home():
    return render_template('home.html', app_title='hallo Guido')

@app.route('/')
def framework():
    return render_template('index.html')

@app.route('/startseite')
def startseite():
    return render_template('startseite.html')

@app.route('/bstest')
def test():
    return render_template('bootstap_test.html')

@app.route('/_change_smart_button')
def _change_smart_button():
    ip_input = request.args.get('ip_input')
    port_input = request.args.get('port_input')
    path_input = request.args.get('path_input')
    content_type_input = request.args.get('content_type_input')
    request_type_input = request.args.get('request_type_input')
    body_input = request.args.get('body_input')

    print('ip_input: \t' + str(ip_input))
    print('port_input: \t' + str(port_input))
    print('path_input: \t' + str(path_input))
    print('content_type_input: \t' + str(content_type_input))
    print('request_type_input: \t' + str(request_type_input))
    print('body_input: \t' + str(body_input))
    
    sleep(10)
    return jsonify(result='finished')
