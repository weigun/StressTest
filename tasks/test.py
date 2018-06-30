# -*- coding: utf-8 -*-
from locust import HttpLocust, task,TaskSet
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))

import config
from behavior.behavior import UserBehavior
from common.util import is_ok

class tt(TaskSet):

    @task(5)
    def user_info(self):
        print(666666)
        # r = self._get(config.Api.user_info)
        # is_ok(r)
        # header=header_maker(token=self._Token)
        # r = self.client.get(config.Api.user_info,headers = header,timeout = config.TIME_OUT)
        # ret =  r.json()
        # print(ret   )
        # print(ret['body']['username'])
        # assert r.status_code == 200
        # assert ret['body']['username'] != ''

    @task()
    def stop(self):
        self._stop()
        # if self.in_mix:
        #     self.interrupt()
        # print('info')

    def _stop(self):
        print('stop')


class ApiUser(HttpLocust):
    task_set = tt
    min_wait = 2000
    max_wait = 3000

