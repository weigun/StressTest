# -*- coding: utf-8 -*-
from locust import HttpLocust, task,TaskSet
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))

import config
from common.util import foreach,load_modules,Weight



# @task
def stop(self):
    self.interrupt()

def add_stop(cls):
    cls._stop = stop

mods = load_modules(except_file = config.EXCEPT_FILE)
# 增加stop方法
foreach(add_stop,mods)

class TaskWeight(Weight):
    '''
    任务权重类
    '''
    Signin = 2
    Info = 3



class Mix(TaskSet):
    tasks = TaskWeight()(mods)

class ApiUser(HttpLocust):
    task_set = Mix
    min_wait = 3000
    max_wait = 5000
