# -*- coding:utf-8 -*-
# @Time : 2022/2/15 9:36
# @Author: 应无所住，何生其心
# @File : 多线程楚尘.py
# @Software : PyCharm
import requests
from lxml import etree
from threading import Thread
from queue import Queue
from requests.adapters import HTTPAdapter
s = requests.session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))


class MyThread(Thread):  # 定义一个类，继承Thread
    def __init__(self, q,name):  # 初始化方法，接收q,name参数。
        Thread.__init__(self)   # 继承父类的初始化方法。
        self.q = q
        self.name = name
    def run(self):   # 重写run方法
        global index    # 更改全局变量（index）
        while not self.q.empty():   # 定义循环not队列不为空时（empyt）程序继续执行
            data = self.q.get()     # 取出队列数据赋给变量data
            url = data[1] #  URL拼接data变量组成完整的URL
            head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
            }
            res = s.get(url, headers=head, timeout=(3, 7))
            page = etree.HTML(res.text)
            title_1 = page.xpath('//div[@class="book reader"]//h1/text()')[0]
            text_1 = page.xpath('//*[@id="chaptercontent"]/text()')
            text_1 = '\n'.join(text_1)
            while data[0] > index + 1:
                pass
            if data[0] == index + 1:
                f.write(title_1 + '\n' + text_1 + '\n')           # 章节内容
                print(self.name,f'{title_1}--------保存成功！！！!!')
                index += 1
if __name__ == '__main__':
    index = -1  # 章节索引标记，表示保存的章数
    base = 'https://www.bige9.com/book/17291/'
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }
    res = s.get(base, headers = head ,timeout=(3,7))
    page = etree.HTML(res.text)
    title = page.xpath('//div[@class="book"]//h1/text()')[0]
    # f = open(f'./{title}.txt', 'w+', encoding='utf-8')
    with open(f'./{title}.txt', 'w+', encoding='utf-8') as f:
        f.write(title + '\n')
        qq = []
        q = Queue()
        for i in range(1,5):
            url =f'https://www.bige9.com/book/17291/{i}.html'
            qq.append(url)
            # print(qq)
        for j in enumerate(qq):
            q.put(j,qq)
            # print(q.get())
        ts = []
        for ii in range(5):   # 创建5个线程
            t = MyThread(q, name = f'线程--->{ii}')  # 实例化mythread,类，把队队Q,参数name传过去。
            t.start()            # 开始线程
            ts.append(t)    # 开始的线程加入列表ts
        for t in ts:
            t.join()
    print('下载全部结束!!!!!!!')