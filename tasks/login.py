# -*- coding: utf-8 -*-
from locust import HttpLocust, task
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from behavior.behavior import UserBehavior

class Login(UserBehavior):

    def on_start(self):
        # Override
        pass

    @task(10)
    def  login(self):
        super(Login, self).on_start()

class ApiUser(HttpLocust):
    task_set = Login
    min_wait = 2000
    max_wait = 5000

