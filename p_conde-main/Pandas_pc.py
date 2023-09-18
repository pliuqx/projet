# -*- coding:utf-8 -*-
# @Time : 2021/12/15 17:02
# @Author: 应无所住，何生其心
# @File : Pandas_pc.py
# @Software : PyCharm

import scrapy
import requests
from lxml import etree
# from threading import Thread
# from queue import Queue

def main():

    url =" "
    url_1 = 'http://c.biancheng.net'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    resp = requests.get(url, headers = headers  )
    page = etree.HTML(resp.content)

    for i in range(3,37):
        url_date = page.xpath(f'//*[@id="contents"]/dd[{i}]/a/@href')
        for j in url_date:
            url_all.append(url_1 + str(j))
    return url_all
def page_jx(url_all):
    for x in url_all:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        resp = requests.get(x, headers = headers)
        page_all = etree.HTML(resp.content)

        for page in page_all:
            #title = ''.join(page.xpath('//*[@id="article"]/h1/text()'))
            txt = page.xpath('//*[@id="arc-body"]/text() ') # 提取字符串
            txt_j = ''.join(txt) # 转换列表为字符串
            txt_j = txt_j.replace("', '\n', '\nSeries"," ") # 去掉无用的字符
            print(txt_j)

if __name__ == '__main__':
    url_all = []
    main()
    page_jx(url_all)
    # print(url_all)
    url ="http://c.biancheng.net/pandas/"
    url_1 = 'http://c.biancheng.net'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    resp = requests.get(url, headers = headers  )
    page = etree.HTML(resp.content)