# -*- coding: utf-8 -*-
#@File:  squeue.py
#@Time:  2023/09/18     16:28:57
#@Author: 应无所住 、何生其心 
#@Version: python3.10
#@Software: VsCode 

from sstack import *

class SQueueErro(Exception):  #异常类
    pass


class SQueue:
    def __init__(self):
        self.queue = []
    # 判断队列为空
    def is_empty(self):
        return self.queue == []
    # 入队
    def enqueue(self,val):
        self.queue.append(val)
        
    # 出队
    def dequeue(self):
        if not self.queue:
            raise SQueueErro("SQueue is None")
        return self.queue.pop(0)
    # 遍历队列
    def show(self):
        if not self.queue:
            raise SQueueErro("SQueue is None")
        for i in self.queue:
            print(i)
        
        
if __name__ == "__main__":
    sq = SQueue()
    for i in range(20):
        sq.enqueue(i)
    st = Sstack()
    while not sq.is_empty():
        st.push(sq.dequeue())
    while not st.is_empty():
        sq.enqueue(st.pop())
    while not sq.is_empty():
        print(sq.dequeue())
    