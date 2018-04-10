from flask import Flask, flash, redirect, render_template, \
     request, url_for, Blueprint

zeptrion_air_blpr = Blueprint('zeptrion_air', __name__)

tabs = [
    {'name':'Smart Btn','url':'/zeptrion_air/smrt_btn'}, 
    # {'name':'Tap1','url':'/zeptrion_air/smrt_btn1'},
    # {'name':'Tap2','url':'/zeptrion_air/smrt_btn1'}
]

panels = [
    {'name':'Panel Kueche','url':'/zeptrion_air/smrt_btn','has_smrt_btn':True},
    {'name':'Panel Stube','url':'/zeptrion_air/smrt_btn','has_smrt_btn':True},
    {'name':'Panel Keller','url':'/zeptrion_air/smrt_btn','has_smrt_btn':False}
]

@zeptrion_air_blpr.route('/zeptrion_air/')
def zeptrion_air():
    return render_template('zeptrion_air.html', app_title='Zeptrion Air', tabs=tabs)

@zeptrion_air_blpr.route('/zeptrion_air/smrt_btn')
def zeptrion_air_smart_button():
    return render_template('zeptrion_air_smart_button.html', tab_name='Smart Btn', panels=panels)