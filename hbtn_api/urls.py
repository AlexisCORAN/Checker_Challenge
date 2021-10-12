#!/usr/bin/python3
"""This module defines the allowed  to make use of HolbertonChecker API"""

"""
POST /users/auth_token.json
----------------
params: auth_token

GET /users/me.json
GET /projects/:id.json
GET /tasks/:id.json
POST /tasks/:id/start_correction.json
GET /correction_requests/:id.json
"""

auth_tkn=''
query = 'auth_token={}'.format(auth_tkn)

URL_BASE = 'https://intranet.hbtn.io'
URL_AUTH = '{}/users/auth_token.json'.format(URL_BASE)
URL_ME = '{}/users/me.json?{}'.format(URL_BASE, query)
URL_PROJECT = '{}/projects/:id.json?{}'.format(URL_BASE, query)
URL_TASK = '{}/tasks/:id.json?{}'.format(URL_BASE, query)
URL_TASK_CORRECTION = '{}/tasks/:id/start_correction.json?{}'.format(URL_BASE, query)
URL_CORRECTION_RESULTS = '{}/correction_requests/:id.json?{}'.format(URL_BASE, query)
