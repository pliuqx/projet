# -*- coding:utf-8 -*-
# @Time : 2021/10/20 9:04
# @Author: 应无所住，何生其心
# @File : SSS.py
# @Software : PyCharm

import os

file_dir = './ts_file'
if not os.path.exists(file_dir):
    os.mkdir(file_dir)
# m3u8文件URL
m3u8_url = "https://vod8.wenshibaowenbei.com/20211001/DeQItwdd/1000kb/hls/index.m3u8"
# 提取文件名
file_name = m3u8_url.split('/')[-1]
file_path = os.path.join(file_dir, file_name)

print(file_path)
