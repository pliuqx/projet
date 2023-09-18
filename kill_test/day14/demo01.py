"""
    内置可重写函数
    练习:exercise01.py
"""

class StudentModel:
    def __init__(self, name="", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    # 对象 --> 字符串 (随意格式)
    def __str__(self):
        return "我叫%s,编号是%d,年龄是%d,成绩是:%d"%(self.name,self.id,self.age,self.score)

    # 对象 --> 字符串(解释器可识别,有格式)
    def __repr__(self):
        return "StudentModel('%s',%d,%d,%d)"%(self.name,self.age,self.score,self.id)


s01 = StudentModel("无忌",27,100,101)
str01 = str(s01)
print(str01)
print(s01)

str02 =repr(s01)
print(str02)

# 根据字符串执行python代码
re = eval("1+2*5")
# exec
print(re)

# 克隆对象
# repr 返回python格式的字符串
# eval根据字符串执行代码
s02 = eval(repr(s01))
s02.name = "老张"
print(s01.name)









