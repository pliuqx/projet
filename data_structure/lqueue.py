# -*- coding:utf-8 -*-
# @Time : 2023/9/18 17:57
# @Author: 应无所住，何生其心
# @File : lqueue.py
# @Software : PyCharm


class SQueueErro(Exception):  #异常类
    pass

class Node:
    """
        思路:将自定义的类视为节眯的后成类,实例对包含数据部分和指向下一个节点的next
    """
    def __init__(self,val,next = None):
        self.val = val   # 有用数据
        self.next = next  # 循环下一个节点关系

class Lqueue:
    def __init__(self):
        self.front = self.rear = Node(None)
        
    # 判空
    def is_empty(self):
        return self.front == self.rear
    
    # 入队操作
    def enqueue(self,val):
        self.rear.next = Node(val)
        self.rear = self.rear.next
    # 出队操作
    def dequeue(self):
        if self.front == self.rear:
            raise SQueueErro("LQueue is empty")
        self.front = self.front.next
        return self.front.val



if __name__ == "__main__":
    lq = Lqueue()
    for i in range(10):
        lq.enqueue(i)
    while not lq.is_empty():
        print(lq.dequeue())



