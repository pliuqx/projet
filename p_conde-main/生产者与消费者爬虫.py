# -*- coding:utf-8 -*-
# @Time : 2021/11/9 14:00
# @Author: 应无所住，何生其心
# @File : 生产者与消费者爬虫.py
# @Software : PyCharm

#  导入模块


import threading
import random


# 定义银行存款
g_money = 100


#  1、定义生产者类

class productor(threading.Thread):
    # 复写run方法

    def run(self):
        global g_money
      # 定义生产者赚的钱
        money = random.randint(100, 1000)
        global += money
        pass

    pass


# 2.定义消费者模式
class consumer(threading.Thread):
    # 复写run方法
    def run(self):
        pass

    pass


if __name__ == '__name__':

    # 定义三个生产者
    for i in range(3):
        # 实例化对象
        p = productor()
        p.start()

    #  定义三个消费者
    for j in range(5):
        # 实例化对象
        c = consumer()
        c.start()

    pass