# -*- coding: utf-8 -*-
'''
@File    :   f_j_d.py
@Time    :   2023/08/22 15:12:06
@Author  :   应无所住 、何生其心 
@Version :   python3.10
@Software:   VsCode 
'''

"""
        定义图形管理器类
        1. 管理所有图形
        2. 提供计算所有图形总面积的方法

    具体图形:
        圆形(pi × r ** 2)
        矩形(长*宽)
        ...

    测试：
        创建1个圆形对象，1个矩形对象，添加到图形管理器中.
        调用图形管理器的计算面积方法，输出结果。

    要求：增加新图形，不修改图形管理器的代码.
    体会：面向对象三大特征：
            封装/继承/多态
         面向对象设计原则：
            开闭/单一/倒置
"""


# 定义一个图形类
class Figuer:
    def __init__(self,c = 0 ,k = 0 ,r =0):
        self.a = c
        self.b = k
        self.r = r
        pass
    pass


# 计算方法类
class Compute:
    def pub_run(self):
        raise NotImplementedError()
        pass 

# 定义一个图形管理器
class FigureSystem:
    def __init__(self,):
        self.fig_list = []   #初始化图形列表
    
    def add_fig(self,fig_info):   # 增加新的图形
        if not isinstance(fig_info,Compute):
            raise ValueError()
        else:
            self.fig_list.append(fig_info)
         
    def sum_fig(self,):
        con_sum = 0
        for item in self.fig_list:
            con_sum += item.pub_run()
        return con_sum


class Circle(Compute):
    def __init__(self,radius):
        self.radius = radius
    
    def pub_run(self):
        return self.radius * 3.1415926 ** 2
    
    
class Rect(Compute):
    def __init__(self,lenght,high):
        self.lenght = lenght
        self.high = high
    
    def pub_run(self):
        return self.lenght * self.high
    
    
    
if __name__=="__main__":
    f01 = FigureSystem()
    c01 = Circle(5)
    r01 = Rect(5,6)
    f01.add_fig(c01)
    f01.add_fig(r01)
    re = f01.sum_fig()
    print(re)
    
    pass