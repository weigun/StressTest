# -*- coding: utf-8 -*-
from  __future__ import print_function
from locust import TaskSet, task
# import os
# import sys
# sys.path.append(os.getcwd())

import config
from common.util import get_random,header_maker,payload_maker,is_ok

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
        r = self._post(config.Api.login, {"username": get_random(), "verifyCode": "1111", "loginType": "0"}, self._Token, start_flag = True)
        if r:
            ret = r.json()
            assert ret['data'] != None
            self._Token = ret['data']['token']
        else:
            self.on_start()



    def _get(self,api,payload = None,token = '',timeout = config.TIME_OUT,start_flag = False):
        # token为空时，跳过这个测试，避免影响数据
        if not start_flag and not self._Token:
            return
        with self.client.get(api,params = payload,headers = header_maker(token=token or self._Token),timeout = timeout,catch_response=True) as resp:
            if resp.status_code != 200:
                resp.failure(api + " failed,status_code is " + str(resp.status_code))
                # print(resp.text + "----->" + token)
                return
            return resp

    def _post(self,api,payload_dict = None,token = '',timeout = config.TIME_OUT,start_flag = False):
        # token为空时，跳过这个测试，避免影响数据
        if not start_flag and not self._Token:
            return
        if payload_dict:
            payload = payload_maker(payload_dict)
        else:
            payload = ""
        with self.client.post(api , payload , headers = header_maker(token=token or self._Token), timeout = timeout,catch_response=True) as resp:
            if resp.status_code != 200:
                # print(payload,header_maker(token=token or self._Token))
                resp.failure(api + " failed,status_code is " + str(resp.status_code))
                return
            return resp

    @task()
    def stop(self):
        self._stop()

    def _stop(self):
        pass



