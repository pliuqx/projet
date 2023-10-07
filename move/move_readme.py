# -*- coding: utf-8 -*-
#@File:  move_readme.py
#@Time:  2023/10/08     16:00:17
#@Author: 应无所住 、何生其心 
#@Version: python3.10
#@Software: VsCode 

"""
    需求：
        1、获取电影片名
        2、获取电影主演
        3、获取电影类型
        4、获取电影简介
        5、获取电影导演
        6、获取电影状态
"""

import requests
from lxml import etree
from threading import Thread


class Node:
    def __init__(self,title='',performer = '', director='', state='', type='', introduction=''):
        """

        :param title:
        :param performer:
        :param director:
        :param state:
        :param type:
        :param introduction:
        """
        self.title = title     #片名
        self.director = director # 导演
        self.performer = performer # 演员
        self.state = state    # 状态
        self.type = type     # 类型
        self.introduction = introduction  #  简介

class Date_Get(Thread):
    def __init__(self):
        self.__list_date = []
        super().__init__()

    @property
    def list_date(self):
        return self.__list_date
    

    def get_url(self):
        for i in range(1, 200):
            page1 = Get_Page(f'http://www.taishengjx.com/dyttdy/index______{i}.html')
            # url = etree.HTML(page1.page().text).xpath('//*[@id="content"]/li/a/@href')
            url = self.x_path(page1.page().text, '//*[@id="content"]/li/a/@href')
            for jj in url:
                yield f'http://www.taishengjx.com{jj}'

    @staticmethod
    def x_path(res, rule):
        return etree.HTML(res).xpath(rule)
    
    def run(self):
        for i in self.get_url():
            res = Get_Page(i).page().text
            title = self.x_path(res,'//div[2]/ul/li[1]/h1/text()')
            performer = self.x_path(res,'//div[2]/ul/li[3]/a/text()')
            director = self.x_path(res,'//div[1]/div[2]/ul/li[6]/text()')
            state = self.x_path(res,'//div[2]/ul/li[4]/text()')
            type1 = self.x_path(res,'//div[1]/div[2]/ul/li[7]/a/text()')
            introduction = self.x_path(res,'//div[2]/ul/li[13]/p/text()')
            node = Node(title ,performer, director, state, type1, introduction)
            self.__list_date.append(node)
            # self.node.title = title
            # self.node.performer = performer
            # self.__list_date.append(self.node)
            print(f"{title}电影获取完毕！！！！！！！")

class Get_Page:
    def __init__(self,url):
        self.url = url

    def page(self):
        for i in range(3):
            try:
                return requests.get(self.url,cookies=cookies, headers=headers, verify=False,timeout = 3)
            except Exception as e:
                pass





if __name__=="__main__":
    cookies = {
        'td_cookie': '1681317069',
        'zanpian_playlog': 'think%3A%7B%22id_78223%22%3A%7B%22log_vid%22%3A%2278223%22%2C%22log_sid%22%3A%221%22%2C%22log_pid%22%3A%221%22%2C%22log_urlname%22%3A%22HD%22%2C%22log_maxnum%22%3A%221%22%2C%22log_addtime%22%3A%221696667770%22%7D%7D',
        'PHPSESSID': 'vd42310v7jsa7s5drf1e38dgp9',
        'Hm_lvt_ac29d0a3f969e649c7f730afc9d1657d': '1696665292,1696751551',
        'Hm_lpvt_ac29d0a3f969e649c7f730afc9d1657d': '1696751845',
    }
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'td_cookie=1681317069; zanpian_playlog=think%3A%7B%22id_78223%22%3A%7B%22log_vid%22%3A%2278223%22%2C%22log_sid%22%3A%221%22%2C%22log_pid%22%3A%221%22%2C%22log_urlname%22%3A%22HD%22%2C%22log_maxnum%22%3A%221%22%2C%22log_addtime%22%3A%221696667770%22%7D%7D; PHPSESSID=vd42310v7jsa7s5drf1e38dgp9; Hm_lvt_ac29d0a3f969e649c7f730afc9d1657d=1696665292,1696751551; Hm_lpvt_ac29d0a3f969e649c7f730afc9d1657d=1696751845',
    }
    txt = Date_Get()
    txt.run()
    for  j in txt.list_date:
        print(''.join(j.title) + ":" , j.performer)