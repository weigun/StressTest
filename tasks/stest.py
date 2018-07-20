# -*- coding: utf-8 -*-
from locust import task
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import config
from behavior.behavior import UserBehavior
from behavior.client import Client

@Client.action
class Stest(UserBehavior):

    def on_start(self):
        # Override
        pass

    @task(100)
    def test_json(self):
        r = self._get(config.Api.test,start_flag = True)

# Client.task_set = Login