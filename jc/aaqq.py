# -*- coding: utf-8 -*-
"""
    @File    :   aaqq.py
    @Time    :   2023/09/08 20:48:04
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
cookies = {
    '__51uvsct__3FgrooI6uIBQDjjF': '1',
    '__51vcke__3FgrooI6uIBQDjjF': 'b4e535c7-79a5-506c-94d7-7eae8c33e8f9',
    '__51vuft__3FgrooI6uIBQDjjF': '1693882843938',
    'ewave_history': '%7Blog%3A%5B%7B%22id%22%3A%2271271%22%2C%22name%22%3A%22%E7%A2%9F%E4%B8%AD%E8%B0%8D%E7%AC%AC7%E9%83%A8%22%2C%22playname%22%3A%22HD%22%2C%22link%22%3A%22%2Frfd2%2F71271.html%22%2C%22playlink%22%3A%22https%3A%2F%2Fwww.rfd9.com%2Frfd4%2F71271-1-1.html%22%7D%5D%7D',
    '__vtins__3FgrooI6uIBQDjjF': '%7B%22sid%22%3A%20%228840a85d-b9c2-5919-826c-6e0fd843e0b8%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%20979664%2C%20%22dr%22%3A%20761413%2C%20%22expires%22%3A%201693885623536%2C%20%22ct%22%3A%201693883823536%7D',
}

headers = {
    'authority': 'www.rfd9.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="21", " Not;A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.rfd9.com/rfd4/71271-1-1.html',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': '__51uvsct__3FgrooI6uIBQDjjF=1; __51vcke__3FgrooI6uIBQDjjF=b4e535c7-79a5-506c-94d7-7eae8c33e8f9; __51vuft__3FgrooI6uIBQDjjF=1693882843938; ewave_history=%7Blog%3A%5B%7B%22id%22%3A%2271271%22%2C%22name%22%3A%22%E7%A2%9F%E4%B8%AD%E8%B0%8D%E7%AC%AC7%E9%83%A8%22%2C%22playname%22%3A%22HD%22%2C%22link%22%3A%22%2Frfd2%2F71271.html%22%2C%22playlink%22%3A%22https%3A%2F%2Fwww.rfd9.com%2Frfd4%2F71271-1-1.html%22%7D%5D%7D; __vtins__3FgrooI6uIBQDjjF=%7B%22sid%22%3A%20%228840a85d-b9c2-5919-826c-6e0fd843e0b8%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%20979664%2C%20%22dr%22%3A%20761413%2C%20%22expires%22%3A%201693885623536%2C%20%22ct%22%3A%201693883823536%7D',
}


class MyThread(Thread):  # 定义一个类，继承Thread
    def __init__(self, q, name):  # 初始化方法，接收q,name参数。
        Thread.__init__(self)  # 继承父类的初始化方法。
        self.q = q
        self.name = name

    def run(self):  # 重写run方法
        global index  # 更改全局变量（index）
        while not self.q.empty():  # 定义循环not队列不为空时（empyt）程序继续执行
            data = self.q.get()  # 取出队列数据赋给变量data
            url = data[1]  # URL拼接data变量组成完整的URL
            res = s.get(url, headers = headers, timeout = (3, 7))
            while data[0] > index + 1:
                pass
            if data[0] == index + 1:
                with open(f'./ts/{index}.ts', 'wb') as file:
                    file.write(res.content)
                    print(self.name, f'{index}--------保存成功！！！!!')
                    index += 1

if __name__=="__main__":
    urls = []
    with open('./https.txt', 'r') as f:
        lines = f.readlines()
        urls.extend(iter(lines))
    index = -1
    q = Queue()
    for count, url in enumerate(urls):
        q.put((count,url))
        # print(q.get())
    ts = []
    for ii in range(5):   # 创建5个线程
        t = MyThread(q, name = f'线程--->{ii}')  # 实例化mythread,类，把队队Q,参数name传过去。
        t.start()            # 开始线程
        ts.append(t)    # 开始的线程加入列表ts
    for t in ts:
        t.join()
    # print(f'下载{url}完成！！！！！')
    print(f'下载{index}个文件，已全部完成下载！！！！！！！！！')