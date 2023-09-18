# -*- coding:utf-8 -*-
# @Time : 2021/11/8 15:26
# @Author: 应无所住，何生其心
# @File : url_list.py
# @Software : PyCharm


import requests
from bs4 import BeautifulSoup
import pymysql
import threading
import time
import _thread


def main():
    url_all = 'https://www.xuanshu.com/book/5013/'
     # 获取全部URL
    data_get(url_all)


def data_get(url_all):
    url_list = []

    for i in range(1450250, 1450314):
        url = url_all + (str(i) + '.html')

        url_list.append(url)
    print(url_list)
if __name__ == '__main__':
    main()