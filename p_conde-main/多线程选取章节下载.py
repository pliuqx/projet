# -*- coding:utf-8 -*-
# @Time : 2021/11/24 14:38
# @Author: 应无所住，何生其心
# @File : 多线程选取章节下载.py
# @Software : PyCharm

import requests
from lxml import etree
from threading import Thread
from queue import Queue

'''
题的根本原因在于：因为爬取和保存的一致性，混乱的爬取顺序使得保存顺序也变得混乱。
解决方案：将爬取过程和保存过程分离，多线程爬取数据，但按顺序保存数据。
比如一本小说，在爬取章节的过程中可以使用多线程，但不要在爬取之后立即保存，等待时机，精准写入。
那这个时机是什么呢？
可以在爬取章节的过程中，给每个章节一个带序号的标记，这个序号即小说章节的序号；保存时，从序号0开始保存，记录这一个序号，再检测当前爬取的章节中有没有比记录的序号刚好大于1的（大于1相当于下一个章节），有就写入，没有就等待。
具体过程:
爬取目录页，抽取出所有的章节链接。
将所有待爬取的链接扔到一个队列里面去，同时给每个链接一个标记。
开5个线程，不断地从队列里面拿链接进行爬取。
单个章节爬取之后，让爬取这个链接的线程阻塞。
申明一个成员变量，表示保存的章节序号，从-1开始
当前线程的链接标记是否刚好比章节序号大于1，是就保存，不是就继续阻塞
因为是从队列中取数据，就能够保证这5个章节是还没有被爬取的前5个章节
'''

class MyThread(Thread):
    def __init__(self, q):
        Thread.__init__(self)
        self.q = q

    def run(self):   # 重写run方法
        global index    # 更改全局变量（index）
        while not self.q.empty():   # 定义循环not队列不为空时（empyt）程序继续执行
            data = self.q.get()     # 取出队列数据赋给变量data
            url = root + ''.join(data[1])  #  URL拼接data变量组成完整的URL
            response = requests.get(url, headers=headers)  # requests.get 解析网页
            page = etree.HTML(response.content)  # 用二进制的方式解析网页
            chapter = page.xpath("//h1/text()")  # 拿到小说的名字
            chapter = ''.join(chapter)   # 截取文字部分
            print("爬取 -> %s 成功！！！" % chapter, index)

            content = page.xpath("//div[@id='content']/text()")  # 获取文章内容
            content ='' .join(content)   # 截取文章内容
            # 截取多余的元素替换成空格
            content = content.replace("\xa0\xa0\xa0\xa0",'').replace("请记住本书首发域名：ddyueshu.com。顶点小说手机版阅读网址：m.ddyueshu.com",'').replace("请记住本书首发域名：booktxt.net。顶点小说手机版阅读网址：m.booktxt.net",'')

            # 如果当前标记比保存的小说章节序号大于1，阻塞
            while data[0] > index + 1:
                pass

            # 刚好等于indes + 1时，通过，保存章节
            if data[0] == index + 1:
                print("保存 -> %s,成功！！！！！" % chapter, index)
                f.write('\n' + chapter)    # 章节名字
                f.write(content)            # 章节内容
                index += 1


if __name__ == '__main__':
    root = "https://www.booktxt.net/29_29254/"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

    index = -1  # 章节索引标记，表示保存的章数

    response = requests.get(root, headers=headers)
    page = etree.HTML(response.content)
    title = ''.join(page.xpath("//h1/text()"))  # 小说名
    print(title)

    with open("%s.txt" % title, 'a+', encoding='utf8') as f:
        f.write(title)  # 先写入小说名
        # hrefs = page.xpath("//div[@id='list']/dl/dt[2]/following-sibling::dd/a/@href")
        hrefs = page.xpath("//*[@id='list']/dl/dd[2932]/following-sibling::dd/a/@href")
        q = Queue()  # 建立队列
        for i, href in enumerate(hrefs):  # 用枚举的方法遍历
            q.put((i, href))           # 将遍历出来的（i）索引，与（href）地址数据存入队列

        ts = []
        for i in range(5):   # 创建5个线程
            t = MyThread(q)
            t.start()            # 开始线程
            ts.append(t)    # 开始的线程加入列表ts
        for t in ts:
            t.join()


