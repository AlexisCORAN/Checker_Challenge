#!/usr/bin/python3
import storage
import requests as rq
from hbtn_api.urls import URL_PROJECT
from messages import PROJECT_TITLE
from messages import CURR_PROJECT_TITLE
from messages.formats import tasks_fmt

def project_info(project_id=-1):
    url = URL_PROJECT.replace(':id', project_id)
    res = rq.get(url)
    try:
        body = res.json()
        name = body.get('name', None)

        if name is None:
            storage.project = None
            return {'success': False, 'msg': 'The project was not found'}

        storage.project = body

        name = PROJECT_TITLE.format(name)
        tasks = body.get('tasks', [])

        return {'success':True, 'msg':'{}\n{}'.format(name, tasks_fmt(tasks))}
    except Exception as e:
        storage.project = None
        return {'success':False, 'msg':'The project was not found'}
