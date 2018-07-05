# -*- coding: utf-8 -*-
from locust import task
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from behavior.behavior import UserBehavior
from behavior.client import Client

@Client.action
class Login(UserBehavior):

    def on_start(self):
        # Override
        pass

    @task(10)
    def  login(self):
        super(Login, self).on_start()

# Client.task_set = Login