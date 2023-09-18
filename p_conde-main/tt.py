# -*- coding:utf-8 -*-
# @Time : 2021/11/5 13:53
# @Author: 应无所住，何生其心
# @File : tt.py
# @Software : PyCharm

import pymysql
list=[20,5,'wangyan']
datalist = ['男单第一轮，刘丁硕3-2击败普拉托诺夫，6-11、9-11、11-9、11-7、11-7；梁靖崑3-0击败德沃斯，11-4、11-4、12-10；王楚钦3-0击败尼日利亚选手Olajide OMOTAYO，11-8、11-4、11-5；林高远3-1击败托奇克，7-11、11-7、11-6、11-3！国乒4人晋级16强。']
def txt_save(datalist):
    # 连接数据库
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='',
        charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    cursor.execute('use xs ')
    # sql = "insert into test(age,id,name) values(" + str(list[0]) + "," + str(list[1]) + "," + "'" + list[2] + "'" + ")"
    for i in datalist:
        sql = ("insert into xhaoxu(txt) values(%s)")
        cursor.execute(sql,(i))
        conn.commit()

txt_save(datalist)