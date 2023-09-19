# -*- coding:utf-8 -*-
# @Time : 2023/9/20 16:35
# @Author: 应无所住，何生其心
# @File : key.py
# @Software : PyCharm

import requests

url = 'https://hnzy.bfvvs.com/play/RdG2NzQb/enc.key'
key = requests.get(url).content

print(key)

if __name__ == "__main__":
    pass