# -*- coding: utf-8 -*-
'''
    @File    :   aaa.py
    @Time    :   2023/08/22 16:24:07
    @Author  :   应无所住 、何生其心 
    @Version :   python3.10
    @Software:   VsCode 
'''

class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        if isinstance(graphic, Graphic):
            self.__graphics.append(graphic)
        else:
            raise ValueError()

    def get_total_area(self):
        total_area = 0
        # 遍历图形列表，累加每个图形的面积
        for item in self.__graphics:
            # 多态：
            # 调用的是图形
            # 执行的是圆形/矩形...
            total_area += item.calculate_area()
        return total_area

class Graphic:
    def calculate_area(self):
        # 如果子类不重写，则异常.
        raise NotImplementedError()
#-----------------------------------
class Circle(Graphic):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius **2


class Rectanlge(Graphic):
    def __init__(self,length,width):
        self.lenght = length
        self.width = width


    def calculate_area(self):
        return self.lenght *  self.width


c01 = Circle(5)
r01 = Rectanlge(10,20)
manager = GraphicManager()
manager.add_graphic(c01)
manager.add_graphic(r01)
re = manager.get_total_area()
print(re)