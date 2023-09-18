# -*- coding: utf-8 -*-
#@File:  lstack.py
#@Time:  2023/09/18     15:56:02
#@Author: 应无所住 、何生其心 
#@Version: python3.10
#@Software: VsCode 

class LstackErro(Exception):  #异常类
    pass

class Node:
    """
        思路:将自定义的类视为节眯的后成类,实例对包含数据部分和指向下一个节点的next
    """
    def __init__(self,val,next = None):
        self.val = val   # 有用数据
        self.next = next  # 循环下一个节点关系

class Lstack:
    def __init__(self):
        self._top = None
    
    def is_empty(self):
        return self._top is None
    
    def push(self,val):
        self._top = Node(val,self._top)
    
    def pop(self):
        if self._top is None:
            raise LstackErro("Lstack is_empty")
        value = self._top.val
        self._top = self._top.next
        return value
    
    def top(self):
        if self._top is None:
            raise LstackErro("Lstack is_empty")
        return self._top.val

if __name__ == "__main__":
    ls = Lstack()
    ls.push(1)
    ls.push(1)
    ls.push(2)
    ls.push(3)
    ls.push(4)
    print(ls.pop())
    print(ls.pop())
    print(ls.pop())
    print(ls.pop())
    print(ls.pop())