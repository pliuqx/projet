# -*- coding:utf-8 -*-
# @Time : 2023/10/8 9:53
# @Author: 应无所住，何生其心
# @File : sequence_table.py
# @Software : PyCharm


from lxml import etree
import requests
import re
from threading import Thread


class Node:
    def __init__(self, title = None, txt = None):
        self.name = title
        self.age = txt
        

class Get_Page(Thread):
    def __init__(self):
        super().__init__(self)
        
    def run(self):
        pass
        






if __name__ == "__main__":
    pass