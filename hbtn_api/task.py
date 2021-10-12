#!/usr/bin/python3
import storage
import requests as rq
from hbtn_api.urls import URL_TASK

def task_info(task_id):
    url = URL_TASK.replace(':id', task_id)
    res = rq.get(url)
    return res.json()
