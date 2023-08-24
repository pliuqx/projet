# -*- coding: utf-8 -*-
'''
@File    :   obj_test.py
@Time    :   2023/08/14 14:46:31
@Author  :   应无所住 、何生其心 
@Version :   python3.10
@Software:   VsCode 
'''


class Person:
    def __init__(self, name,sex):
        self.name = name
        self.sex = sex
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    def teach(self,other,kill):
        print(self.name,"教",other,kill)
    
    def work(self,money):
        print(self.name,"上班赚了",money,'元')
        
        
    @staticmethod    
    def atk_jy(val01,val02):
        print(val01,'教',val02,'九阳神功')
        
    @staticmethod
    def atk_hz(val01,val02):
        print(val01, "教", val02, "化妆")
        
    @staticmethod
    def money(val):
        if val == "无忌":
            print(val, "上班赚了1万元钱")
        else:
            print(val, "上班赚了6仟元钱")
            
if __name__ == "__main__":
     p01 = Person('无忌', "男")
     p02 = Person("赵敏", "女")
     p01.teach(p02.name,'九阳神功')
     p02.teach(p01.name,"化妆")
     p01.work(10000)
     p02.work(6000)
     Person.atk_jy(p01.name,p02.name)
     Person.atk_hz(p02.name,p01.name)
     Person.money(p01.name)
     Person.money(p02.name)
    
     pass
 
 
 
