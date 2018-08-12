# -*- coding: utf-8 -*-

#@author: weicheng

#@file: celeryconfigure.py

#@time: 2018/08/12

from kombu import Exchange,Queue

BROKER_URL = "redis://127.0.0.1:6379/1"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/2"

CELERY_QUEUES = (
Queue("default",Exchange("default"),routing_key="default"),
Queue("for_task_A",Exchange("for_task_A"),routing_key="for_task_A"),
Queue("for_task_B",Exchange("for_task_B"),routing_key="for_task_B")
)

CELERY_ROUTES = {
'ApkManager.task.*':{"queue":"for_task_A","routing_key":"for_task_A"},
'GmsLab.task.*':{"queue":"for_task_B","routing_key":"for_task_B"}
}
