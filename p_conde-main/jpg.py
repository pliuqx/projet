# -*- coding:utf-8 -*-
# @Time : 2021/12/21 15:16
# @Author: 应无所住，何生其心
# @File : jpg.py
# @Software : PyCharm

import requests
import re
from lxml import etree
import os
import sys

def data_jpg():
    y = 1
    for i in range(2,100):
        x = 0
        url = f'https://pic.netbian.com/4kmeinv/index_{i}.html'
        url1 = 'https://pic.netbian.com/4kmeinv/index.html'
        aa = 'https://pic.netbian.com'
        res = requests.get(url)
        page = etree.HTML(res.content)
        li_list = page.xpath('//*[@id="main"]/div[3]/ul/li')  # 将li对象列表赋值给li_list变量
        for li in li_list:
            x += 1
            txt_title = li.xpath(f'//*[@id="main"]/div[3]/ul/li[{x}]/a/b/text()')[0]
            txt_title = txt_title[:][:4]
            # print(txt_title)
            url_1 = li.xpath(f'//*[@id="main"]/div[3]/ul/li[{x}]/a/@href')[0]
            res_1 = requests.get(aa + url_1)
            page_1 = etree.HTML(res_1.content)
            # print(page_1)
            res_2 = page_1.xpath('//*[@id="img"]/img/@src')[0]
            # print(res_2)
            url_data = aa + res_2
            with open('d:/photo/' + txt_title +'.jpg', 'wb') as f:
                r = requests.get(url_data)
                r.raise_for_status()
                f.write(r.content)
                print(f'爬取成功{y}')
                y += 1


if __name__ == '__main__':
    data_jpg()
    pass
