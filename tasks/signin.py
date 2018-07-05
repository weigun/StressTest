# -*- coding: utf-8 -*-
from locust import task
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import config
from behavior.behavior import UserBehavior
from common.util import is_ok
from behavior.client import Client

# 类命名规则
# 必须和文件名同名，并且首字母要大写
@Client.action
class Signin(UserBehavior):

    @task(10)
    def useer_signin(self):
        # header=header_maker(token=self._Token)
        # r = self.client.get(config.Api.signin,headers = header,timeout = config.TIME_OUT)
        r = self._get(config.Api.signin)
        # ret = r.json()
        # print(ret)
        # is_ok(r)

# Client.task_set = Signin

