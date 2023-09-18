# -*- coding:utf-8 -*-
# @Time : 2021/11/8 10:09
# @Author: 应无所住，何生其心
# @File : 多线程写法.py
# @Software : PyCharm

import threading
import time
import requests
from bs4 import BeautifulSoup
import pymysql
import _thread

exitFlag = 0

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        # print ("Starting " + self.name)
        # print_time(self.name, self.counter, 5)
        # print ("Exiting " + self.name)


        def main():
            url_all = 'https://www.xuanshu.com/book/5013/'
            # url_all = 'http://ldytt.com/List/1-pg-'
            # # 1.爬取网页
            datalist = data_get(url_all)
            # savepath = "豆瓣电影Top250.xls"  # 当前目录新建XLS，存储进去
            # # dbpath = "movie.db"              #当前目录新建数据库，存储进去
            # # 3.保存数据
            # saveData(datalist, savepath)  # 2种存储方式可以只选择一种
            # # saveData2DB(datalist,dbpath)
            txt_save(datalist)


        def data_get(url_all):
            datalist = []
            j = 1
            for i in range(1450250, 1450255):
                url = url_all + (str(i) + '.html')
                html = askURL(url)
                soup = BeautifulSoup(html, "html.parser")
                # print(soup)
                for itme in soup.find_all('div', id="content1"):
                    data = []
                    itme = str(itme)
                    data.append(itme)
                    datalist.append(data)
                    print(f'下载成功11111  {j}')
                    j += 1
            return datalist


        def askURL(url):
            head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
                "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
            }
            # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
            request = requests.get(url, headers=head)
            res = request
            res.encoding = 'utf-8'
            html = res.text
            # print(html)
            return html

        #
        # def txt_save(datalist):
        #     file = open('zhaoxu.txt', 'w+', encoding='utf-8')
        #     file.write(str(datalist))
        #     file.close()

        def txt_save(datalist):
            # 连接数据库
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8')
            # 创建游标
            cursor = conn.cursor()
            cursor.execute('use xs')
            for i in datalist:
                sql = ("insert into xhaoxu(txt) values(%s)")
                cursor.execute(sql, (i))
                conn.commit()
            # print(datalist)

if __name__ == '__main__':
    main()
    print("爬取完毕!!!!！")

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            _thread.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

# print ("Exiting Main _Thread")