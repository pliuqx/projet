# -*- coding:utf-8 -*-
# @Time : 2023/9/22 16:58
# @Author: 应无所住，何生其心
# @File : myrange.py
# @Software : PyCharm



class Myrange:
    def __init__(self,stop_val):
        self.stop_val = stop_val

    def __iter__(self):
        return MyrangeIter(self.stop_val)


class MyrangeIter:
    def __init__(self,end_val):
        self.end_val = end_val
        self.cont = 0

    def __next__(self):
        if self.cont == self.end_val:
            raise StopIteration
        temp = self.cont
        self.cont += 1
        return temp


if __name__ == "__main__":
    for i in Myrange(10):
        print(i)



    pass