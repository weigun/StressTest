# -*- coding: utf-8 -*-
from locust import TaskSet, task
# import os
# import sys
# sys.path.append(os.getcwd())

import config
from common.util import random_user,header_maker,payload_maker,is_ok

# 继承的子类命名规则
# 必须和文件名同名，并且首字母要大写
class UserBehavior(TaskSet):
    """
    继承的子类命名规则
    必须和文件名同名，并且首字母要大写
    """
    _Token = ''
    def on_start(self):
        '''
        初始化函数，只执行一次，目前用来登录
        :return:
        '''
        r = self._post(config.Api.login,{"username": random_user(), "verifyCode": "1111","loginType":"0"},self._Token)
        if r:
            ret = r.json()
            assert ret['body'] != None
            self._Token = ret['body']['token']


    def _get(self,api,token = '',timeout = config.TIME_OUT):
        with self.client.get(api,headers = header_maker(token=token or self._Token),timeout = timeout,catch_response=True) as resp:
            if resp.status_code != 200:
                resp.failure(api + " failed,status_code is " + str(resp.status_code))
                return
            return resp

    def _post(self,api,payload_dict,token = '',timeout = config.TIME_OUT):
        payload = payload_maker(payload_dict)
        with self.client.post(api , payload , headers = header_maker(token=token or self._Token), timeout = timeout,catch_response=True) as resp:
            if resp.status_code != 200:
                resp.failure(api + " failed,status_code is " + str(resp.status_code))
                return
            return resp

    @task()
    def stop(self):
        self._stop()

    def _stop(self):
        pass
        # print('stop call')



