# -*- coding: utf-8 -*-
from locust import task,TaskSet
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import config
from common.util import is_ok
from behavior.client import Client

@Client.action
class tt(TaskSet):

    def on_start(self):
        # Override
        pass

    @task(100)
    def test_json(self):
        r = self._get(config.Api.test)

    # @task()
    # def stop(self):
    #     self._stop()
    #     # if self.in_mix:
    #     #     self.interrupt()
    #     # print('info')
    #
    # def _stop(self):
    #     print('stop')

# Client.task_set = tt


