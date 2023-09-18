# -*- coding:utf-8 -*-
# @Time : 2021/11/1 10:31
# @Author: 应无所住，何生其心
# @File : mysqlxx.py
# @Software : PyCharm

import pymysql


def my_sql():
    # 连接数据库

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8')
    # 创建游标
    cursor = conn.cursor()

    # 创建析的数据库
    # cursor.execute('create database jc1 default charset utf8 collate utf8_general_ci')
    # 执行创建新数据库的操作
    # conn.commit()
    cursor.execute('use jc1 ')
    # 创建数据表
    # cursor.execute('create table 税种表 (id INT(11),name VARCHAR(25),deptId INT(11),salary FLOAT)')
    # 发送指令显示全部数据库文件
    cursor.execute('show tables')
    # 用db 接收指令的的结果并显示出来
    # db = cursor.fetchall()
    #插入三条记录
    cursor.execute('insert into 税种表(name, banji, age, xuehao) values("zhangsan", "J1802", "18", "2018030438")')
    cursor.execute('insert into 税种表(name, banji, age, xuehao) values("zhangsi", "J1802", "18", "2018030439")')
    cursor.execute('insert into 税种表(name, banji, age, xuehao) values("zhangwu", "J1802", "18", "2018030436")')
    cursor.execute('insert into 税种表(name, banji, age, xuehao) values("zhangsan", "J1802", "18", "2018030438")')
    cursor.execute('insert into 税种表(name, banji, age, xuehao) values("zhangsi", "J1802", "18", "2018030439")')
    cursor.execute('insert into 税种表(name, banji, age, xuehao) values("zhangwu", "J1802", "18", "2018030436")')
    # 执行插入记录的操作
    conn.commit()
    # 查询表结构
    cursor.execute('select * from 税种表')
    db = cursor.fetchall()


    print(db)
my_sql()
