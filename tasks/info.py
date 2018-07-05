# -*- coding: utf-8 -*-
from locust import task
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config
from behavior.behavior import UserBehavior
from common.util import is_ok
from behavior.client import Client

@Client.action
class Info(UserBehavior):

    @task(10)
    def user_info(self):
        r = self._get(config.Api.user_info)
        # is_ok(r)


# Client.task_set = Info
