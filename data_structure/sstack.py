# -*- coding: utf-8 -*-
#@File:  sstack.py
#@Time:  2023/09/17     20:10:46
#@Author: 应无所住 、何生其心 
#@Version: python3.10
#@Software: VsCode 

class sstackErro(Exception):  #异常类
    pass

class sstack:
    def __init__(self):
        self._elems = []
    
    def is_empty(self): # 判空
        return self._elems == []
    
    def push(self,val): # 入栈
        self._elems.append(val)
    
    def pop(self): # 弹栈
        if self.is_empty():
            raise sstackErro('sstack Erro')
        return self._elems.pop()
    
    def top(self): # 查看栈顶元素
        if self.is_empty():
            raise sstackErro("stack is empty")
        return self._elems[-1]
    
    
    
if __name__=="__main__":
    st = sstack()
    st.push(3)
    st.push(2)
    st.push(1)
    print(st.top())
    while not st.is_empty():
        print(st.pop())
    
    
    
    pass        
