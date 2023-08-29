# -*- coding: utf-8 -*-
'''
@File    :   lt_move.py
@Time    :   2023/08/10 14:41:29
@Author  :   应无所住 、何生其心 
@Version :   python3.10
@Software:   VsCode 
'''


class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def lift():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)


class DoubleListHelper:

    # 在二维列表中获取指定位置，指定方向，指定数量的元素.
    # 例如：list01　"10"　右边　３ --> "11", "12", "13"
    # 例如：list01　Vector2(1, 0)　Vector2.right()　３ --> "11", "12", "13"
    @staticmethod
    def get_elements(target, vect_pos, vece_dir, count):
        """
            在二维列表中获取指定位置，指定方向，指定数量的元素.
         :param target: 二维列表
         :param vect_pos: 指定位置
         :param vece_dir: 指定方向
         :param count: 指定数量
         :return: 列表
         """
        result_list = []
        for i in range(count):
            vect_pos.x += vece_dir.x
            vect_pos.y += vece_dir.y
            element = target[vect_pos.x][vect_pos.y]
            result_list.append(element)
        return result_list


if __name__ == "__main__":
    list01 = [
        ['00', '01', '02', '03'],
        ['10', '11', '12', '13'],
        ['20', '21', '22', '23'],
        ['30', '31', '32', '33'],
    ]
    re = DoubleListHelper.get_elements(list01, Vector2(3, 3), Vector2.up(), 3)
    print(re)
