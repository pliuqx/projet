# -*- coding: utf-8 -*-
#@File:  tt.py
#@Time:  2023/10/09     08:24:36
#@Author: 应无所住 、何生其心 
#@Version: python3.10
#@Software: VsCode 



from lxml import etree
import re
import requests
from pandas import DataFrame




class Node:

    def __init__(self, name = '', age = 0, sex = None):
        """

        :param name:
        :param age:
        """
        self.name = name
        self.age = age
        self.sex = sex




class Get_date:
    def __init__(self):
        # self.node = Node()
        self.__list_date = []
        
    @property
    def list_date(self):
        return self.__list_date
        
    
    def get_txt(self):
        for i in range(1,100):
            node = Node("张三", 18)
            self.__list_date.append(node)
            # self.node.name = f"xs"
            # self.node.age = 18
            # self.__list_date.append(self.node)

if __name__ == "__main__":
    tt = Get_date()
    tt.get_txt()
    # for i in tt.list_date:
    #     print(i.name)
    print(len(tt.list_date))