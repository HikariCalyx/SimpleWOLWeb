#!/usr/bin/env python3
"""
SimpleWOLWeb for Python 3 Configuration File
Version 1.0

After every edits, you must restart service so all changes will take effect.
"""

# from commonModule import baseVariablePath as bvp

"""
Server Domain, SSL enabling and Port

This depends on if you're going to use NGINX or provide access directly.
"""

base_url = 'random_base_url_here'

srv_config = {
    'domain': 'domain.example.com',
    'port': 28800,
    'ACL': '0.0.0.0',
    'SSL': False
}

ssl_config = {
    'cert_file': '/etc/letsencrypt/live/' + srv_config['domain'] + '/fullchain.pem',
    'pkey_file': '/etc/letsencrypt/live/' + srv_config['domain'] + '/privkey.pem',
}

"""
WOL Address

Provide the device you want to send magic packet to.
"""
target_wol_mac = 'AABBCCDDEEFF'
target_ip = '192.168.5.1'
wait_timeout = 25