# -*- coding: utf-8 -*-
'''
@File    :   open_clos.py
@Time    :   2023/08/28 10:32:31
@Author  :   应无所住 、何生其心 
@Version :   python3.10
@Software:   VsCode 
'''

class Staff:
    def __init__(self):
        self.__sta_list = []
    
    @property
    def sta_list(self):
        return self.__sta_list
    
    def add_staff(self,staff):
        self.__sta_list.append(staff)
        

class Programmer:
    def __init__(self,salary= 0):
        self.salary = salary    
    
    def commission(self,val):
        return val * 0.05
    
    
    
