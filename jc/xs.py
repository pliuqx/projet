# -*- coding: utf-8 -*-
"""
    @File    :   xs.py
    @Time    :   2023/09/04 09:47:24
    @Author  :   应无所住 、何生其心 
    @Version :   python3.10
    @Software:   VsCode 
"""

import sniffio
import httpx
import requests
from lxml import etree
from threading import Thread
from queue import Queue
from requests.adapters import HTTPAdapter
s = requests.session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))


class GetRes():
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
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.baidu.com/link?url=3mdcAmh1ONi4u46NtgrsktnWTD5PmxWcxgeJzc3HwZSaXy7hpyYhIebWlKt8WYJx&wd=&eqid=f828bade0001b9cf0000000264f59692',
            'accept-language': 'zh-CN,zh;q=0.9',
            # 'cookie': 'jieqiVisitId=article_articleviews%3D35818; Hm_lvt_4b2f87826c608c0d97fbc58099f9aeba=1693816479; Hm_lpvt_4b2f87826c608c0d97fbc58099f9aeba=1693816479; Hm_lvt_34742c534c5be2b6ac5803a7c6ae6107=1693816523; Hm_lpvt_34742c534c5be2b6ac5803a7c6ae6107=1693816523',
        }

        self.cookies = {
            'jieqiVisitId': 'article_articleviews%3D35818',
            'Hm_lvt_4b2f87826c608c0d97fbc58099f9aeba': '1693816479',
            'Hm_lpvt_4b2f87826c608c0d97fbc58099f9aeba': '1693816479',
            'Hm_lvt_34742c534c5be2b6ac5803a7c6ae6107': '1693816523',
            'Hm_lpvt_34742c534c5be2b6ac5803a7c6ae6107': '1693816523',
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
    
class GetTitle(PubData):
    def __init__(self,obj):
        super().__init__(obj)
    def get_data(self,):
        return ''.join(self.res.xpath('//*[@id="wrapper"]//h1/text()'))

class GetTxt(PubData):
    def __init__(self,obj):
        super().__init__(obj)
        
    def get_data(self, ):
        return '\n'.join(self.res.xpath('//*[@id="content"]/text()'))

class GetUrlAll(PubData):
    def __init__(self,obj):
        super().__init__(obj)
    
    def get_data(self, ): 
        url_all = self.res.xpath('//*[@id="list"]/dl/dd[position()>9 and position()<130]/a/@href')
        
        return [f'https://www.shenzuxs.com{url}' for url in url_all]

class SaveData:
    def __init__(self, d_dict):
        self.d_dict = d_dict
    def save_data(self):
        with open('./mn_f.txt ', "a" , encoding="utf-8") as f:
            f.write(self.d_dict['title'][0])
            f.write('\n')
            f.write(self.d_dict['txt'][0])
            f.write('\n')
            
            
    pass

def main():
    r01 = GetRes('https://www.shenzuxs.com/shu35818/')
    u01 = GetUrlAll(r01.get_page()).get_data()
    for i in u01:
        data_dict = {}
        # print(i)
        title = GetTitle(GetRes(i).get_page()).get_data()
        txt = GetTxt(GetRes(i).get_page()).get_data()
        data_dict.setdefault('title', []).append(title)
        data_dict.setdefault('txt', []).append(txt)
        SaveData(data_dict).save_data()
        print(f'{title}下载完成！！！！！！！！')
    # print(data_dict['title'])
        
if __name__ == "__main__":
    main()
    print('全部下载完成！！！！！！！！！！！！')