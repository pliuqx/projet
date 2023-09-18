"""
    模块
    17:00
    练习:exercise03.py
"""
# 导入方式1
# 本质：使用变量名module01关联模块地址
# import module01
# module01.fun01()
# my02 = module01.MyClass02()
# my02.fun02()

# as 为导入的成员其另外一个名称
import module01 as m01
m01.fun01()
my02 = m01.MyClass02()
my02.fun02()

# 导入方式2
# 本质：将指定的成员导入到当前模块作用域中
# 小心：导入进来的成员不要和当前模块成员名称相同
# from module01 import fun01
# from module01 import MyClass02
#
# def fun01():
#     print("当前模块fun01")
#
# fun01()
# my02 = MyClass02()
# my02.fun02()

# 导入方式3
# 本质：将指定模块的所有成员导入到当前模块作用域中
# 小心：导入进来的成员和其他模块成员冲突
from module01 import *

fun01()
my02 = MyClass02()
my02.fun02()
