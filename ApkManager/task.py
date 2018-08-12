# -*- coding: utf-8 -*-

#@author: weicheng

#@file: task.py

#@time: 2018/08/12

from WebTest.tasks import app


@app.task
def taskA(x,y):
    print ("task A")
    print (x+y)

