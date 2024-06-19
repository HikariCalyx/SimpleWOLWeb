#!/usr/bin/env python3
"""
SimpleWOLWeb

2015-2024 (C) Hikari Calyx Tech. All Rights Reserved.
"""
import sys
from pythonping import ping
sys.path.append('.')
from flask import Flask, render_template
from gevent import pywsgi
from config import base_url, srv_config, ssl_config, target_wol_mac, target_ip, wait_timeout
from wakeonlan import send_magic_packet

app = Flask(__name__)

@app.route('/' + base_url + '/cover.css', methods=['GET'])
def cover():
    return render_template('cover.css')

@app.route('/' + base_url + '/PowerOnDevice', methods=['GET'])
def poweron():
    send_magic_packet(target_wol_mac)
    return render_template('wol_wait.html', wait_timeout=wait_timeout)

@app.route('/' + base_url + '/', methods=['GET'])
def ahome():
    if str(list(ping(target_ip, count=1, out=None))[0]) == 'Request timed out':
        is_disabled = ''
        power_on_status = 'Power On'
    else:
        is_disabled = 'disabled'
        power_on_status = 'Already Power On'
    return render_template('wol_frontend.html', power_on_status=power_on_status, is_disabled=is_disabled)

if __name__ == '__main__':
    print("SimpleWOLWeb\n2015-2024 (C) Hikari Calyx Tech. All Rights Reserved.\n")
    if srv_config['SSL']:
        server = pywsgi.WSGIServer((srv_config['ACL'], srv_config['port']), app, certfile=ssl_config['cert_file'], keyfile=ssl_config['pkey_file'])
    else:
        server = pywsgi.WSGIServer((srv_config['ACL'], srv_config['port']), app)
    print("Now listening on Port " + str(srv_config['port']))
    server.serve_forever()

