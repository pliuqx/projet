# -*- coding: utf-8 -*-
"""
    @File    :   aaqq.py
    @Time    :   2023/09/08 20:48:04
    @Author  :   应无所住 、何生其心 
    @Version :   python3.10
    @Software:   VsCode 
"""

import requests
from threading import Thread
from queue import Queue
from requests.adapters import HTTPAdapter
from Crypto.Cipher import AES

s = requests.session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))
cookies = {
    'td_cookie': '99684960',
    '__51cke__': '',
    'Hm_lvt_9343a05d94d95ae7979dadfc92d59a6e': '1695170034',
    '__tins__21747207': '%7B%22sid%22%3A%201695170033473%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201695171844584%7D',
    '__51laig__': '2',
    'Hm_lpvt_9343a05d94d95ae7979dadfc92d59a6e': '1695170045',
}

headers = {
 'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://g.cjy-skf.com/dongzuopian/diezhongdie7zhimingqingsuanshang/2-1.html',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': 'td_cookie=99684960; __51cke__=; Hm_lvt_9343a05d94d95ae7979dadfc92d59a6e=1695170034; __tins__21747207=%7B%22sid%22%3A%201695170033473%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201695171844584%7D; __51laig__=2; Hm_lpvt_9343a05d94d95ae7979dadfc92d59a6e=1695170045',

}


class MyThread(Thread):  # 定义一个类，继承Thread
    def __init__(self, q, name):  # 初始化方法，接收q,name参数。
        Thread.__init__(self)  # 继承父类的初始化方法。
        self.q = q
        self.name = name

    def run(self):  # 重写run方法
        global index  # 更改全局变量（index）
        key = requests.get('https://hnzy.bfvvs.com/play/RdG2NzQb/enc.key').content  #解密代码
        cryptor = AES.new(key, AES.MODE_CBC, key)  # 解密代码

        while not self.q.empty():  # 定义循环not队列不为空时（empyt）程序继续执行
            data = self.q.get()  # 取出队列数据赋给变量data
            url = data[1]  # URL拼接data变量组成完整的URL
            res = s.get(url, headers = headers, timeout = (3, 7))
            while data[0] > index + 1:
                pass
            if data[0] == index + 1:
                with open(f'h:/m3u8/ts/{100001 + index}.ts', 'wb') as file:
                    file.write(cryptor.decrypt(res.content)) # 将文件解密后写入
                    print(self.name, f'{index}--------保存成功！！！!!')
                    index += 1

if __name__=="__main__":
    urls = []
    with open('h:/m3u8/https.txt', 'r') as f:
        lines = f.readlines()
        urls.extend(iter(lines))
    index = -1
    q = Queue()
    for count, url in enumerate(urls):
        q.put((count,url))
    ts = []
    for ii in range(5):   # 创建5个线程
        t = MyThread(q, name = f'线程--->{ii}')  # 实例化mythread,类，把队队Q,参数name传过去。
        t.start()            # 开始线程
        ts.append(t)    # 开始的线程加入列表ts
    for t in ts:
        t.join()
    print(f'下载{index}个文件，已全部完成下载！！！！！！！！！')