# -*- coding: utf-8 -*-
from locust import task,TaskSet
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import config
from common.util import foreach,load_modules,Weight
from behavior.client import Client



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
    Signin = 100
    Info = 100
    Map = 100
    Findred = 100
    Getred = 100


@Client.action
class Mix(TaskSet):
    tasks = TaskWeight()(mods)

# TODO 将Client.task_set  设计成一个装饰器
# Client.task_set = Mix
Client.min_wait = 3000
Client.max_wait = 5000
