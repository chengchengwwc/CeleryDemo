# -*- coding: utf-8 -*-

#@author: weicheng

#@file: task.py

#@time: 2018/08/12


from celery import Celery


app = Celery(include=["ApkManager.task","GmsLab.task"])

app.config_from_object('WebTest.celeryconfigure')






