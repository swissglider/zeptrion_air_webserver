from flask import Flask, flash, session, jsonify, redirect, render_template, \
     request, url_for, Blueprint
from time import sleep
import json
from zeptrionAirApi import ZeptrionAirHub

zeptrion_air_blpr = Blueprint('zeptrion_air', __name__)

#  ----------------------------------------------------------
#  Zeptrion Air Smart Button App

@zeptrion_air_blpr.route('/zeptrion_air_smt_btn_1')
def zeptrion_air_smt_btn_1():
    return render_template('zeptrion_air_app/zeptrion_air_smt_btn_1.html', title='Change Zeptrion AIr Smart Button', next_popup='/zeptrion_air_smt_btn_2')

@zeptrion_air_blpr.route('/zeptrion_air_smt_btn_2')
def zeptrion_air_smt_btn_2():
    return render_template('zeptrion_air_app/zeptrion_air_smt_btn_2.html', title='Change Zeptrion AIr Smart Button')

@zeptrion_air_blpr.route('/_zeptrion_air_smt_btn_2_status')
def zeptrion_air_smt_btn_2_status():
    result = change_smart_button(session['request'])
    if len(result) > 0 and result[0]:
        return_value = {}
        return_value['changed'] = result[0]['changed']
        return_value['tried to change'] = result[0]['tried to change']
        return_value['status_code'] = result[0]['status_code']
        return jsonify(return_value)
    return jsonify(result)

@zeptrion_air_blpr.route('/_change_smart_button')
def _change_smart_button():
    prog_elements = {
        'prog_req_type': request.args.get('request_type_input'),
        'prog_url': request.args.get('ip_input'),
        'prog_path': request.args.get('path_input'),
        'prog_typ': request.args.get('content_type_input'),
        'prog_header_field': '',
        'prog_port': int(request.args.get('port_input')),
        'prog_body': request.args.get('body_input'),
        'prog_body': str(request.args.get('body_input')).rstrip()
    }
    session['request'] = prog_elements
    
    # sleep(10)
    return jsonify(result='finished1')

#  ----------------------------------------------------------
#  Zeptrion Air Smart Button Model

def change_smart_button(prog_elements):
    hub = ZeptrionAirHub(3) 
    result = hub.programm_smart_btn(prog_elements)
    return result
