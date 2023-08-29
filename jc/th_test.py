# -*- coding: utf-8 -*-
"""
    @File    :   th_test.py
    @Time    :   2023/09/08 20:44:00
    @Author  :   应无所住 、何生其心 
    @Version :   python3.10
    @Software:   VsCode 
"""

import requests
from lxml import etree
from threading import Thread
from queue import Queue
from requests.adapters import HTTPAdapter
s = requests.session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))

class GetRes:
    def __init__(self,url):
        self.url = url
        self.headers ={
            'authority': 'www.shenzuxs.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '"Chromium";v="21", " Not;A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'zh-CN,zh;q=0.9',
        }

        self.cookies = {
            'Hm_lvt_34742c534c5be2b6ac5803a7c6ae6107': '1693816523',
            'jieqiVisitId': 'article_articleviews%3D35818',
            'Hm_lvt_4b2f87826c608c0d97fbc58099f9aeba': '1693816479,1694137966',
            'Hm_lpvt_4b2f87826c608c0d97fbc58099f9aeba': '1694137966',
        }

    def get_page(self,):
        requests.packages.urllib3.disable_warnings()
        res = s.get(url=self.url,headers = self.headers,cookies = self.cookies, verify = False)
        return etree.HTML(res.content)

class PubData:
    def __init__(self, obj):
        self.res = obj
    def get_data(self):
        raise NotImplementedError()    

class GetUrlAll(PubData):
    def __init__(self,obj):
        super().__init__(obj)
    
    def get_data(self, ): 
        url_all = self.res.xpath('//*[@id="list"]/dl/dd[position()>9 and position()<1364]/a/@href')
        
        return [f'https://www.shenzuxs.com{url}' for url in url_all]

class SaveData:
    def __init__(self, title,txt ):
        self.title = title
        self.txt = txt 
    def save_data(self):
        with open('./jc/mn_f.txt ', "a" , encoding="utf-8") as f:
            f.write(self.title)
            f.write('\n')
            f.write(self.txt)
            f.write('\n')
    
class MyThread(Thread):
    def __init__(self,q,name):
        super().__init__()
        self.q = q
        self.name = name
    def run(self,):
        while not self.q.empty(): 
            global index
            data = self.q.get()
            page = GetRes(url = data[1]).get_page()
            title = ''.join(page.xpath('//*[@id="wrapper"]//h1/text()'))
            txt = '\n'.join(page.xpath('//*[@id="content"]/text()'))
            while data[0] > index + 1:
                pass
            if data[0] == index + 1:
                # SaveData(title,txt).save_data()
                index += 1
                print(f'线程{self.name}开始下载,{title}下载完成！！！！！！！！')
    
def main():
    q = Queue()
    r01 = GetRes('https://www.shenzuxs.com/shu35818/')
    u01 = GetUrlAll(r01.get_page()).get_data()
    for i ,url in enumerate(u01):
        q.put((i,url))
    ts = []
    for count in range(6):
        t = MyThread(q,name = f'{count}')
        t.start()            # 开始线程
        ts.append(t)    # 开始的线程加入列表ts
    for t in ts:
        t.join()
if __name__ == "__main__":
    index = -1
    main()
    print(f'{index}个文件，已全部完成下载！！！！！！！！！')
    
    
