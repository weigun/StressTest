# -*- coding: utf-8 -*-
import random
import json
import importlib
import os
import sys
import glob

def random_user(min = 0,max = 99999999999):
    '''
    随机用户
    :return:
    '''
    return str(random.randint(min,max))


def tojson(d):
    '''
    转json字符串
    :param d:as dict
    :return: json str
    '''
    return json.dumps(d)


def header_maker(token = ""):
    '''
    创建头部
    :param args:
    :param kwargs:
    :return:
    '''
    header = {"Authorization": token, "Content-Type": "application/json"}
    return header

def payload_maker(body,head = {}):
    '''
    生成载荷
    :param d:dict
    :return: json str
    '''
    payload = {"head": {},"body" : {}}
    payload["head"].update(head)
    payload["body"].update(body)
    return tojson(payload)

def is_ok(resp):
    '''
    检查code是否200
    :param resp:
    :return:
    '''
    if resp.status_code != 200:
        resp.failure("failed,status_code is " + resp.status_code)


def foreach(func,*args):
    '''
    类似map的函数
    :param func:
    :param args:
    :return:
    '''
    for x in args:
        if isinstance(x,dict):
            for i in x.values():
                func(i)
        else:
            func(x)

def load_modules(except_file = []):
    '''
    批量载入模块
    :return:module map
    '''
    mod_map = {}
    path = os.path.join(os.path.dirname(os.getcwd()),'tasks','*.py')
    for file in glob.glob(path):
        name,_ = os.path.splitext(os.path.basename(file))
        if os.path.basename(file) not in except_file and '__init__.py' not in file:
            mod = importlib.import_module('.'.join(['tasks', name]))
            mod_map[name.capitalize()] = getattr(mod, name.capitalize())
            # mod_objs.append()
    return mod_map



class Weight(object):
    '''
    任务权重基类
    '''
    def __call__(self, mods,*args, **kwargs):
        _weight =  {}
        for item in self.__class__.__dict__:
            if not item.startswith('_'):
                if item in mods:
                    _weight[mods[item]] = self.__class__.__dict__[item]
        return _weight


if __name__ == '__main__':
    oo = load_modules(except_file =['test.py','login.py','mix.py'])
    def show(x):
        print(x)

    foreach(show,oo)

