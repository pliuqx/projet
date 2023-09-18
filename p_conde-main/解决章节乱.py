# -*- coding:utf-8 -*-
# @Time : 2021/11/10 14:35
# @Author: 应无所住，何生其心
# @File : 解决章节乱.py
# @Software : PyCharm

import requests
from lxml import etree
from threading import Thread
from queue import Queue


class MyThread(Thread):
    def __init__(self, q):
        Thread.__init__(self)
        self.q = q

    def run(self):
        global index
        while not self.q.empty():
            data = self.q.get()
            url = root + ''.join(data[1])
            response = requests.get(url, headers=headers)
            page = etree.HTML(response.content)

            chapter = page.xpath("//h1/text()")
            chapter = ''.join(chapter)
            print(f"爬取 -> {chapter}", index)

            content = page.xpath("//div[@id='content']/text()")
            content = '\n'.join(content)
            content = content.replace("\xa0\xa0\xa0\xa0", "\t")

            # 如果当前标记比保存的小说章节序号大于1，阻塞
            while data[0] > index + 1:
                pass

            # 刚好大于1时，通过，保存章节
            if data[0] == index + 1:
                print(f"保存 -> {chapter}", index)
                f.write('\n' + chapter + '\n')
                f.write(content)
                index += 1


if __name__ == '__main__':
    root = "http://www.booktxt.net/8_8455/"
    # root =  'http://www.tstdoors.com/ldks/22447/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

    index = -1  # 章节标记，表示保存的章数

    response = requests.get(root, headers=headers)
    page = etree.HTML(response.content)
    title = ''.join(page.xpath("//h1/text()"))  # 小说名
    print(title)

    with open(f"{title}.txt", 'w', encoding='utf8') as f:
        f.write(title)  # 先写入小说名
        hrefs = page.xpath("//div[@id='cotent']/dl/dt[2]/following-sibling::dd/a/@href")
        q = Queue()
        for i, href in enumerate(hrefs):
            q.put((i, href))

        ts = []
        for _ in range(3):
            t = MyThread(q)
            t.start()
            ts.append(t)
        for t in ts:
            t.join()