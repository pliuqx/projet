"""
    练习1：
        将day11/day10_exercise/exercise01.py中的
        Vector2和DoubleListHelper定义到
          double_list_helper.py模块中.
    练习2:
        在exercise03.py模块中，实现
        (1)在二维列表中，获取13位置，向左，3个元素

        (2)在二维列表中，获取22位置，向上，2个元素

        (3)在二维列表中，获取03位置，向下，2个元素
    要求：使用三种导入方式
    体会：哪一种更合适。
"""

list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
# 在二维列表中，获取13位置，向左，3个元素
# 方式1:
# import double_list_helper as helper
# re = helper.DoubleListHelper.get_elements(list01, helper.Vector2(1, 3), helper.Vector2.left(), 3)

# 方式2:
# from double_list_helper import DoubleListHelper
# from double_list_helper import Vector2
#
# re = DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)

# 方式3：
from double_list_helper import *
re = DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)

