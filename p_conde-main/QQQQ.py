# -*- coding:utf-8 -*-
# @Time : 2021/11/5 17:20
# @Author: 应无所住，何生其心
# @File : QQQQ.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup
import pymysql




def main():
    url_all = 'http://www.tstdoors.com/ldks/22447/'
    # # 1.爬取网页
    datalist = data_get(url_all)
    txt_save(datalist)
    # savepath = "豆瓣电影Top250.xls"  # 当前目录新建XLS，存储进去
    # # dbpath = "movie.db"              #当前目录新建数据库，存储进去
    # # 3.保存数据
    # saveData(datalist, savepath)  # 2种存储方式可以只选择一种
    # # saveData2DB(datalist,dbpath)



def data_get(url_all):
    datalist = []
    j = 1
    for i in range(5611097, 5611101):
        url = url_all + (str(i) + '.html')
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        for itme in soup.find_all('div', class_="content"):
            data = []
            itme = str(itme)
            s_rep = itme.replace("<br/>\u3000\u3000","\n").replace('<p class="amiddle">安卓、IOS版本请访问官网https://www.biqugeapp.co下载最新版本。如浏览器禁止访问，请换其他浏览器试试；如有异常请邮件反馈。</p>','\n ').replace('</h1>\n<div class="posterror"><a class="red" href="javascript:postError();">章节错误,点此举报(免注册)</a>,举报后维护人员会在两分钟内校正章节内容,请耐心等待,并刷新页面。</div>\r\n','\n ').replace('<div class="content" id="content">\n<h1 class="title">','\n')
            data.append(s_rep)
            datalist.append(data)
            print(f'下载成功!!!!!  {j}')
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
        sql = "insert into xhaoxu(txt) values(%s)"
        cursor.execute(sql,i)
        conn.commit()
    # print(datalist)

if __name__ == '__main__':
    main()
    # for i in range(1):
    #     t = threading.Thread(target=main)
    #     t.start()
    # # print("爬取完毕!!!!！")