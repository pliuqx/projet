# -*- coding: utf-8 -*-
'''
@File    :   test_01.py
@Time    :   2023/08/21 14:14:20
@Author  :   应无所住 、何生其心 
@Version :   python3.10
@Software:   VsCode 
'''



class Tclass:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex


class Tclass01(Tclass):
    def __init__(self,name,age,sex,id):
        self.id = id
        super().__init__(name,age,sex)
            
            
    def fun01(self):
    
        pass
    
if __name__=="__main__":
    t01 = Tclass01('zs',19,'男',100)
    print(t01.name,t01.age,t01.sex,t01.id)