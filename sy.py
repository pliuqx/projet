# -*- coding: utf-8 -*-
'''
@File    :   sy.py
@Time    :   2023/08/14 15:48:11
@Author  :   应无所住 、何生其心 
@Version :   python3.10
@Software:   VsCode 
'''


"""
# 使用方法封装私有变量
class Enemy:
    def __init__(self,name,atk,hp):
        self.name = name
        # self.__atk = atk
        # self.__hp = hp
        self.set_atk(atk)
        self.set_hp(hp)

    def get_atk(self):
        return self.__atk
    # 使用方法封装私有变量
    def set_atk(self,value):
        if 30 <= value <= 60:
            self.__atk = value
        else:
            raise ValueError ('数据不对')

    def get_hp(self):
        return self.__hp

    # 使用方法封装私有变量
    def set_hp(self, value):
        if 50 <= value <= 100:
            self.__hp = value
        else:
            raise ValueError('数据不对')
"""

# 使用property封装变量
class Enemy:
    def __init__(self, name, atk, hp):

        self.name = name
        self.atk = atk  # 代表类变量
        self.hp = hp  # 代表类变量

    def get_atk(self):
        return self.__atk
    def set_atk(self, value):
        if 30 <= value <= 60:
            self.__atk = value
        else:
            raise ValueError('数据不对')
    atk = property(get_atk, set_atk)

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        if 50 <= value <= 100:
            self.__hp = value
        else:
            raise ValueError('数据不对')

    # hp = property(get_hp, set_hp)


if __name__ == "__main__":
    w01 = Enemy('无忌', 55, 90)
    # w01.atk = 40
    w01.hp = 60
    # print(w01.get_atk())
    print(w01.hp)
    pass