#!/usr/bin/python3
import storage
import requests as rq
from hbtn_api.urls import URL_TASK_CORRECTION
from hbtn_api.urls import URL_CORRECTION_RESULTS
from hbtn_api.urls import URL_PROJECT
from messages.formats import checks_fmt


def ask_correction(task_number=-1):
    storage.result_id = None
    try:
        task_number = int(task_number)
    except:
        return {'success': False, 'msg':'You must provide a number'}

    if storage.project is None:
        return {'success': False, 'msg':'You must select a project'}

    tasks = storage.project.get('tasks', [])

    if task_number < 0 or task_number >= len(tasks):
        return {'success': False, 'msg':'The index must be valid'}

    storage.task = task_id = tasks[task_number]
    task_id = tasks[task_number].get("id")
    
    url = URL_TASK_CORRECTION.replace(':id', str(task_id))
    res = rq.post(url)

    if res.status_code != 200:
        return {'success': False, 'msg':'I couldn\'t find the specified task'}

    result_id = res.json().get('id', None)
    if result_id == 0 or result_id is None:
        storage.result_id = None
        return {'success': False, 'msg':'Correction failed'}
        
    storage.result_id = result_id
    return {'success': True, 'msg':'The correction is been processed'}


def get_results(result_id):
    if result_id is None:
        return {'success': False, 'msg':'You must ask for correction first'}

    url = URL_CORRECTION_RESULTS.replace(':id', str(result_id))
    res = rq.get(url).json()
    if res.get('status') != "Done":
        return {'success': False, 'msg': 'You should wait a little bit more, try again in 5 seconds'}
        
    checks = res.get('result_display').get('checks', [])
    passed = res.get('result_display').get('all_passed', False)
    commit_id = res.get('result_display').get('github_commit_id', False)
    return {'success': True, 'msg':checks_fmt(checks, all_passed=passed, commit_id=commit_id)}
