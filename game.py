# -*- coding: utf-8 -*-
'''
@File    :   game.py
@Time    :   2023/08/11 10:07:14
@Author  :   应无所住 、何生其心 
@Version :   python3.10
@Software:   VsCode 
'''

"""
4. 定义敌人类
    -- 数据:姓名,血量,基础攻击力,防御力
    -- 行为:打印个人信息

   创建敌人列表(至少４个元素),并画出内存图。
   查找姓名是"灭霸"的敌人对象
   查找所有死亡的敌人
   计算所有敌人的平均攻击力
   删除防御力小于10的敌人
   将所有敌人攻击力增加50
"""


class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def show(self):
        print(self.name, self.hp, self.atk, self.defense)


class Find:

    @staticmethod
    def name_find():
        for itme in list01:
            if itme.name == "灭霸":
                print(Enemy.show(itme))

    @staticmethod
    def hp_find():
        hp_list = []
        for itme in list01:
            if itme.hp == 0:
                hp_list.append(itme)
        return hp_list

    @staticmethod
    def atk_find():
        sum_atk = 0
        for i in list01:
            sum_atk += i.hp
        return sum_atk / len(list01)

    @staticmethod
    def defense_find():
        for i in range(len(list01)-1, -1, -1):
            if list01[i].defense < 10:
                del(list01[i])

    @staticmethod
    def atk_all():
        for i in list01:
            i.atk += 50


if __name__ == "__main__":
    list01 = [
        Enemy("玄冥二老", 86, 120, 58),
        Enemy("成昆", 0, 100, 5),
        Enemy("谢逊", 120, 130, 60),
        Enemy("灭霸", 0, 1309, 690),
    ]
    # print(Find.atk_find())
    # Find.atk_all()
    # for i in list01:
    # i.show()
    # Find.defense_find()
    # for i in list01:
    # i.show()
    # Find.name_find()
    re = Find.hp_find()
    for i in re:
        i.show()

    pass
