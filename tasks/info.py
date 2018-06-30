# -*- coding: utf-8 -*-
from locust import HttpLocust, task
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))

import config
from behavior.behavior import UserBehavior
from common.util import is_ok

class Info(UserBehavior):

    @task(10)
    def user_info(self):
        r = self._get(config.Api.user_info)
        # is_ok(r)



class ApiUser(HttpLocust):
    task_set = Info
    min_wait = 2000
    max_wait = 3000

