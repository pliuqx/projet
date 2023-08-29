# -*- coding: utf-8 -*-
'''
@File    :   lxobjet.py
@Time    :   2023/08/09 14:45:55
@Author  :   应无所住 、何生其心 
@Version :   python3.10
@Software:   VsCode 
'''


class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex
        pass

    def print_self_info(self):
        print(f'{self.name}年龄是{self.age},成绩是{self.score},性别是{self.sex}')

        pass


list01 = [
    Student("赵敏", 28, 100, "女"),
    Student("苏大强", 68, 62, "男"),
    Student("明玉", 30, 95, "女"),
    Student("无忌", 29, 70, "男"),
    Student("张三丰", 130, 96, "男"),
]
# 练习1:定义函数,在list01中查找name是"苏大强"的对象.
#      将名称与年龄打印在控制台中
# 14:12


def show():
    for i in list01:
        if i.name == '苏大强':
            return i
            # print(f'姓名:{i.name},年龄:{i.age}, 成绩:{i.score}')

    pass


# 练习2:定义函数,在list01中查找所有女同学.
#      将名称与性别打印在控制台中
# 14:33

def show01():
    sex1 = []
    for item in list01:
        if item.sex == '女':
            sex1.append(item)
    return sex1

    pass


def show02():

    pass


class Wife:
    count = 0

    def __init__(self, name=None, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex
        Wife.count += 1

    @classmethod
    def show01(cls):

        print(f'创建了{cls.count}个对象')


if __name__ == '__main__':
    '''
        st = show01()
        for i in st:
            print(f'姓名:{i.name},年龄:{i.age}, 成绩:{i.score}')
    '''
    f01 = Wife('无忌', 18, '男')
    f02 = Wife('赵敏', 18, '女')
    f03 = Wife('苏大强', 18, '男')
    f04 = Wife('明玉', 18, '女')
    f05 = Wife('小昭', 18, '女')
    Wife.show01()
    pass
