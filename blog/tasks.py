from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .cache_manager import sync_click

"""
@task()
def Task_A(message):
    Task_A.update_state(state='PROGRESS', meta={'progress': 0})
    sleep(10)
    Task_A.update_state(state='PROGRESS', meta={'progress': 30})
    sleep(10)
    return message

def get_task_status(task_id):
    task = Task_A.AsyncResult(task_id)

    status = task.state
    progress = 0

    if status == u'SUCCESS':
        progress = 100
    elif status == u'FAILURE':
        progress = 0
    elif status == 'PROGRESS':
        progress = task.info['progress']

    return {'status': status, 'progress': progress}

"""

@shared_task()
def sync_click_task():
    sync_click()
