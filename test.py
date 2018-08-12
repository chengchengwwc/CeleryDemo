# -*- coding: utf-8 -*-

#@author: weicheng

#@file: test.py

#@time: 2018/08/12

import time
from ApkManager.task import taskA
from GmsLab.task import taskB


if __name__ == "__main__":
    Flag = True
    n = 1
    while Flag:
        time.sleep(10)
        taskA.delay(100,200)
        taskB.delay(100,200,300)
        n += 1
        if n >20:
            Flag = False



