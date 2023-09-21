# -*- coding:utf-8 -*-
# @Time : 2023/9/22 11:27
# @Author: 应无所住，何生其心
# @File : iteration.py
# @Software : PyCharm

"""
    员工迭代器
"""

class Employee:
    pass


class EmployeeManager:
    def __init__(self):
        self.__employees =[]
    def add_employees(self,val):
        self.__employees.append(val)
    def __iter__(self):
        return EmployeeIterator(self.__employees)



class EmployeeIterator:
    """
        员工迭代器（获取下一个数据）
    """
    def __init__(self,ems):
        self.__ems = ems
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__ems) -1:
            raise StopIteration
        temp = self.__ems[self.__index]
        self.__index += 1
        return temp




if __name__ == "__main__":
    manager = EmployeeManager()
    manager.add_employees(Employee())
    manager.add_employees(Employee())
    manager.add_employees(Employee())

    for item in manager:
        print(item)

    # 多态
    iterator = manager.__iter__()
    while True:
        try:
            item = iterator.__next__()
            print(item)
        except StopIteration:
            break