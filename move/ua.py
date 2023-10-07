# -*- coding:utf-8 -*-
# @Time : 2023/10/11 15:15
# @Author: 应无所住，何生其心
# @File : ua.py
# @Software : PyCharm

from fake_useragent import UserAgent
import random

ua = UserAgent()


for _ in range(20):
    print(ua.random)






if __name__ == "__main__":
    pass