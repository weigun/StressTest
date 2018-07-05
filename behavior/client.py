# -*- coding: utf-8 -*-
from locust import HttpLocust

class Client(HttpLocust):
    '''
    good luck
    '''
    task_set = None
    min_wait = 2000
    max_wait = 5000

    @classmethod
    def action(cls,_c):
        cls.task_set = _c
        return (lambda :_c)()





if __name__ == '__main__':
    @Client.action
    class TT(object):
        def h(self):
            print("2332")
    t = TT()
    print(t.h())


