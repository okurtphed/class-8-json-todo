from datetime import datetime

from .exceptions import (
    InvalidTaskStatus, TaskAlreadyDoneException, TaskDoesntExistException)
from .utils import parse_date, parse_int


def new():
    return []


def create_task(tasks, name, description=None, due_on=None):
    if due_on and type(due_on) != datetime:
        due_on = parse_date(due_on)

    task = {
        'task': name,
        'description': description,
        'due_on': due_on,
        'status': 'pending'
    }
    tasks.append(task)


def list_tasks(tasks, status='all'):
    
    task_list = []
    
    if status not in ('pending','done', 'all'):
        raise InvalidTaskStatus()
        
    for idx, task in enumerate(tasks, 1):
        
        if task['due_on'] is not None:
            due_on = task['due_on'].strftime('%Y-%m-%d %H:%M:%S')
        else:
            due_on = None

        t = (idx, task['task'], due_on, task['status'])
        if status == 'all' or task['status'] == status:
            task_list.append(t)

    return task_list


def complete_task(tasks, name):
    new_tasks = []
    #task_list = []
    task_found = False
    for idx, task in enumerate(tasks, 1):
        if name == task['task'] or name == str(idx):
            task_found = True
            if task['status'] == 'done':
                raise TaskAlreadyDoneException()
        if name == task['task'] or name == str(idx):
            task = task.copy()
            task['status'] = 'done'
        new_tasks.append(task)
        
    if not task_found:
        raise TaskDoesntExistException()
    '''
    #Another solution
    
    for task in tasks:  #same loop can be used
        task_list.append(task['task'])
    if name not in task_list:
        raise TaskDoesntExistException()
    '''
        

    return new_tasks

