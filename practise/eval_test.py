# -*- coding: utf-8 -*-
'''
@File    :   staff_test.py
@Time    :   2023/08/22 17:24:55
@Author  :   应无所住 、何生其心 
@Version :   python3.10
@Software:   VsCode 
'''


"""
# 练习：创建Enemy类对象，将对象打印在控制台中(格式自定义)
#      克隆Enemy类对象，体会克隆对象变量的改变不影响原对象。

class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
"""

from pandas import DataFrame



class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
    
    def __str__(self):
        return f"我的名字是{self.name},血量{self.hp},攻击力{self.atk},防御力{self.defense}"
    
    def __repr__(self):
        return f"Enemy('{self.name}',{self.hp},{self.atk},{self.defense})"
    
    
e01 = Enemy('zs',100,20,30)
re =eval(repr(e01))
re.name = 'ls'
print(e01)
print(re)