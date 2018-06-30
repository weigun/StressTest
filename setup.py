# -*- coding: utf-8 -*-
from  __future__ import print_function

import os
import sys
import glob
from traceback import print_exc


sys.path.append(os.path.dirname(__file__))
print(sys.path)

# 安装依赖，设置环境
try:
    from locust import HttpLocust, task
except:
    requirements_path = os.path.dirname(__file__)
    requirements_path = os.path.join(requirements_path,"requirements.txt")
    os.system("pip install -r "  + requirements_path)

def start_test(task_name, master ="172.18.8.125"):
    '''
    启动slave和对应的任务脚本
    :param task_name:
    :return:
    '''
#     locust -f index.py  --host https://www.xmwar.com --slave
#     locust - f locust_files / my_locust_file.py - -slave --master - host = 192.168.0.100 - -host = http: // example.com
    host = "https://www.xmwar.com"
    task_name = os.path.join(os.path.dirname(__file__),'tasks',task_name)
    cmd = "locust -f {}  --host {} --slave --master-host={}".format(task_name, host, master)
    print(cmd)
    os.system(cmd)

def myinput(msg = u"请选择任务:"):
    '''
    封装input,兼容py2和py3
    :param msg:
    :return:
    '''
    try:
        return raw_input(msg)
    except:
        return input(msg)

def get_task():
    '''
    获取任务
    :return:
    '''
    print('-' * 30)
    task_folder = os.path.join(os.path.dirname(__file__), 'tasks')
    tasks_map = {}
    i = 1
    for p in glob.iglob(os.path.join(task_folder,'*.py')):
        base_name = os.path.basename(p)
        if '__init__' not in base_name:
            print('{}.{}'.format(i,base_name))
            tasks_map[i] = base_name
            i+=1
    print('-'*30)
    return tasks_map[int(myinput())]



if __name__ == '__main__':
    try:
        selected = get_task()
        start_test(selected,*sys.argv[1::])
    except:
        print_exc()
        myinput("enter to exit.....")


