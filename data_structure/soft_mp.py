# -*- coding:utf-8 -*-
# @Time : 2021/9/26 8:27
# @Author: 应无所住，何生其心
# @File : 冒泡排序.py
# @Software : PyCharm
import random



def mp_soft(li):
    for i in range(len(li) - 1):  # 定义循环i趟来排序
        exchange = False    # 加一个交换标志
        for j in range(len(li) - i - 1):  # 定义每趟循环移动的指针
            if li[j] > li[j + 1]:      # （大于是升序，小于是降序）循环移动的指针与下一元素比较如果大于下一元素
                li[j], li[j + 1] = li[j + 1], li[j]  # 循环移动的指针与下一元素交换位置
                exchange = True  # 交换完后看标志是不是True
        if not exchange:   # 判断标志如果一趟结束后没有发生交换，后面结束函数
            return   # 结束函数



# # li = [9, 8, 7, 1, 2, 3, 4, 5, 6, ]
# li = [random.randint(1,1000) for i in range(10)]  # 用random随机生成数，for 后面是列表生成式

# print(li)
# mp_soft(li)
# print(li)