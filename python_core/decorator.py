# -*- coding: utf-8 -*-
# @File:  decorator.py
# @Time:  2023/10/07     16:44:08
# @Author: 应无所住 、何生其心
# @Version: python3.10
# @Software: VsCode


# 装饰器练习
def dec_ator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return func


@dec_ator
def deposit(money):
    print(f"存{money}钱喽")


@dec_ator
def withdraw(login_id, pwd):
    print("取钱喽", login_id, pwd)


deposit(1000)
withdraw("myid", 123456)
