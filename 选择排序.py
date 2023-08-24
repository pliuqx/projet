# -*- coding:utf-8 -*-
# @Time : 2023/3/7 14:57
# @Author: 应无所住，何生其心
# @File : 选择排序.py
# @Software : PyCharm
'''
选择排序法
'''

def select_soft(aa_list):
    n = len(aa_list)      # 定义列表长度
    for j in range(n - 1):  #循环列表取得最小的值j
        min_index = j       # 取得最小值索引号
        for i in range(j + 1, n):  #循环列表
            if aa_list[min_index] > aa_list[i]:   # 列表最小值min_index,与所有数据进长比较大小
                min_index = i             # 比最小值还小的值 与最小值 交换索引位置
        aa_list[j], aa_list[min_index] = aa_list[min_index], aa_list[j] #列表数据位置交换


if __name__ == '__main__':
    aa_list = [21, 17, 123, 124, 121, 18, 21, 12, 14, 21212, 19, 1212, 10, 21, 2, 12, 212]
    print(aa_list)
    select_soft(aa_list)
    print(aa_list)
    pass