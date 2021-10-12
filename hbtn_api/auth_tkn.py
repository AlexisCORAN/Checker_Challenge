#!/usr/bin/python3
import requests as rq
from hbtn_api.urls import URL_AUTH

def auth(apikey, email, psswd, *args):
    data = {
        'api_key': apikey,
        'email': email,
        'password': psswd,
        'scope': 'checker'
    }
    r = rq.get(URL_AUTH, data=data)
    return r.json()
