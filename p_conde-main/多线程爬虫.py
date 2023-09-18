# -*- coding:utf-8 -*-
# @Time : 2021/11/9 14:03
# @Author: 应无所住，何生其心
# @File : 多线程爬虫.py
# @Software : PyCharm

import time
from queue import Queue
import requests
from bs4 import BeautifulSoup
import pymysql
import threading
import os


# 生产者类，获取数据
class productor(threading.Thread):
    # 定义一个初始化方示
    def __init__(self,page_queue,data_queue):
        # 处理父类的初始化方法
        threading.Thread.__init__(self)
        self.page_queue = page_queue
        self.data_queue = data_queue
        pass
    # 复与run 方法
    def run(self):
        # 为了保证队列的url全部取出，必须写一个死循环
        while True:
            # 判断循环退出的条件,队我为空时退出
            if self.page_queue.empty():
                break
           # 从队列中取出url
            url = self.page_queue.get()
           # 调用get_content方法
            self.get_content(url)
        pass
    # 定义获取数据主方法
    def get_content(self,url):
        global content
        datalist = []
        request = requests.get(url, headers=head)
        res = request
        res.encoding = 'utf-8'
        html = res.text
        soup = BeautifulSoup(html, "html.parser")
        for itme in soup.find_all('div', class_="content"):
            data = []
            itme = str(itme)
            s_rep = itme.replace("<br/>\u3000\u3000","\n").replace('<p class="amiddle">安卓、IOS版本请访问官网https://www.biqugeapp.co下载最新版本。如浏览器禁止访问，请换其他浏览器试试；如有异常请邮件反馈。</p>','\n ').replace('</h1>\n<div class="posterror"><a class="red" href="javascript:postError();">章节错误,点此举报(免注册)</a>,举报后维护人员会在两分钟内校正章节内容,请耐心等待,并刷新页面。</div>\r\n','\n ').replace('<div class="content" id="content">\n<h1 class="title">','\n')

            data.append(s_rep)
            datalist.append(data)
            print('下载成功!!!!!')
            self.data_queue.put(datalist)
            pass
        pass
        # print(datalist)
    pass
# 创建消费者类，保存数据
class consumer(threading.Thread):
    # 定义初始化方法
    def __init__(self,page_queue,data_queue):
        threading.Thread.__init__(self)
        self.data_queue = data_queue
        self.page_queue = page_queue
    # 重写run方法
    def run(self):
        global index
        # 为了保证一直取数据，写一个死循环
        while True:
            # 判断退出条件
            if self.data_queue.empty() and self.page_queue.empty and switch == 1:
                break
            try:
                # 从队列data_queue中取出数据
                data = self.data_queue.get(timeout=2)
                self.save(data)
            except:
                break
        pass
    # 定义保存方法
    def save(self,data):
        file = open('zhaoxu.txt', 'a+', encoding='utf-8')
        file.write(str(data))
        index += 1
        # 插入数据
    #     for i in data:
    #         sql = "insert into xhaoxu(txt) values(%s)"
    #         cursor.execute(sql,i)
    #         conn.commit()
    # def __del__(self):
    #     file.close()
    #     cursor.close()
    #     # xs.close()

    pass
if __name__ == '__main__':
    # 定义开关
    switch = 0
    # # 连接数据库
    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8')
    # # 创建游标
    # cursor = conn.cursor()
    # # 打开数据库xs
    # cursor.execute('use xs')
    url_all = 'http://www.tstdoors.com/ldks/22447/'
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36" }
    index = -1  # 章节标记，表示保存的章数
    # 定义存放url的队列
    page_queue = Queue()
    # 定义存放数据的队列
    data_queue = Queue()
    for i in range(5611097, 5611102):
        u_url = url_all + (str(i) + '.html')
        page_queue.put(u_url)

        pass
    # 定义存放生产者的列表
    p_list = []
    # 创建定义三个生产者
    for i in range(3):
        # 实例化对象
        p = productor(page_queue,data_queue)
        p.start()
        p_list.append(p)


    #  创建定义三个消费者
    for j in range(3):
        # 实例化对象
        c = consumer(page_queue,data_queue)
        c.start()

    # 阻塞每一个生产者
    for p_zu in p_list:
        p_zu.join()
        pass

    # 程序结束后改变switch值
    switch = 1
    pass