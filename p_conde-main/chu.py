# -*- coding:utf-8 -*-
# @Time : 2022/2/14 14:39
# @Author: 应无所住，何生其心
# @File : chu.py
# @Software : PyCharm

import requests
from lxml import etree
from requests.adapters import HTTPAdapter
s = requests.session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))

def main():
    base = 'https://www.bige9.com/book/44550/'
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }
    res = requests.get(base, headers=head)
    page = etree.HTML(res.text)
    title = page.xpath('//div[@class="book"]//h1/text()')[0]
    f.write(title + '\n')
    # print(title)
    for i in range(1853,2040):
        url = f'https://www.bige9.com/book/44550/{i}.html'
        head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
        }
        res = s.get(url, headers = head,timeout = (3,7))
        page = etree.HTML(res.text)
        title_1 = page.xpath('//div[@class="book reader"]//h1/text()')[0]
        text_1 = page.xpath('//*[@id="chaptercontent"]/text()')
        text_1 = '\n'.join(text_1)
        f.write(title_1 + '\n' + text_1 + '\n')
        print(f'{title_1}--------下载结束！！！！！')
    f.close()
    print('下载全部结束！！！！')

if __name__ == '__main__':
    f = open('./chuchen1.txt', 'a+', encoding='utf-8')
    main()