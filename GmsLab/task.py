# -*- coding: utf-8 -*-

#@author: weicheng

#@file: task.py

#@time: 2018/08/12


from WebTest.tasks import app


@app.task
def taskB(x,y,z):
    print ("taskB")
    print (x+y+z)