# -*- coding: utf-8 -*-
#@File:  ts_url.py
#@Time:  2023/09/21     09:17:32
#@Author: 应无所住 、何生其心 
#@Version: python3.10
#@Software: VsCode 

import re
import os


def ts(txt_str):
    url_all = []
    pet = re.compile("https://hnts.ymuuy.com:65/hls/115/20230712/1752663/(.*?).ts")
    with open(txt_str,"r")  as f:
        line = f.readlines()
        line = ','.join(line)   
        url = re.findall(pet,str(line))
        for i in range(len(url)):
            url_a = f"https://hnts.ymuuy.com:65/hls/115/20230712/1752663/{url[i]}.ts"
            url_all.append(url_a)
            # print(url_all)
    return url_all   

txt_s = "h:/m3u8/MM.txt"

print(ts(txt_s))