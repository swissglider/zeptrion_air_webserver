import os
from flask import Flask, redirect, render_template, \
     request, url_for
from zeptrion_air.main import zeptrion_air_blpr

app = Flask(__name__, template_folder='templates', static_url_path='/static')
app.register_blueprint(zeptrion_air_blpr)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'

app.static_folder=app.root_path + '/static'

programm = {
    'title':'Swissglider apps',
    'moto':'Home Automation Apps - from Swissglider',
    'projects': [],
    'about': {'text1':'Ich bin Text 1','text2':'Ich bin Text 2'}
}
programm['projects'] = [
    {'name': 'ZeptrionAir', 'id': 'zeptrionAir', 'title': 'Zeptrion Air - Apps', 'apps':[]},
    {'name': 'Zeptrion', 'id': 'zeptrion', 'title': 'Zeptrion - Apps', 'apps':[]}
]

programm['projects'][0]['apps'].append({
    'first_modul_id': '/zeptrion_air_smt_btn_1',
    'picture_link': 'static/img/portfolio/zeptrionAIr.jpeg',
    'caption_text': 'Zeptrion Air Smart Button Configuration'
})
programm['projects'][0]['apps'].append({
    'first_modul_id': '/dummy_app',
    'picture_link': 'static/img/portfolio/zeptrionAIr.jpeg',
    'caption_text': 'Zeptrion Air Smart Button Configuration'
})
programm['projects'][0]['apps'].append({
    'first_modul_id': '/dummy_app',
    'picture_link': 'static/img/portfolio/zeptrionAIr.jpeg',
    'caption_text': 'Zeptrion Air Smart Button Configuration'
})

@app.route('/')
def framework():
    return render_template('index.html', programm=programm)
