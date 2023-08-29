# -*- coding: utf-8 -*-
#@File    :   linked_list.py
#@Time    :   2023/09/15 10:23:39
#@Author  :   应无所住 、何生其心 
#@Version :   python3.10
#@Software:   VsCode 



class Node:
    """
        思路:将自定义的类视为节眯的后成类,实例对包含数据部分和指向下一个节点的next
    """
    def __init__(self,val,next = None):
        self.val = val   # 有用数据
        self.next = next  # 循环下一个节点关系


class LinkList:
    """
        思路：单链表类，生成对象可以进行增删改查操作
                具体操作通过调用具体方法完成
    """
    def __init__(self,):
        """
            初始化链表，标记一个链表的开端，以便于获取后续的节点
        """
        self.head = Node(None)
    # 通过list_为链表添加一组节点
    def init_list(self,list_):
        p = self.head    # 作为移动变量
        for i in list_:     # 遍历列表 list_
            p.next = Node(i)
            p = p.next
    # 遍历链表
    def show(self,):
        p = self.head.next # 第一个有效节点
        while p is not None:
            print(p.val)
            p = p.next   # P向后移动
    # 判断链表是否为空
    def is_empty(self):
        if self.head.next is not None:
            return True
        else:
            return False
    # 清空链表
    def clear(self):
        self.head.next = None
    # 增加节点
    def append(self,val):
        p = self.head
        while p.next is not None: # 循环判断p.next是不是等于空，等于空就跳出循环
            p = p.next
        p.next = Node(val)  # 将新的节点Node(val),挂在p.next
    # 头部插入
    def head_insert(self,val):
        node = Node(val)       # 生成节点
        node.next = self.head.next # 新节点的NEXT 挂在  self.head.next
        self.head.next = node   # self.head.next 挂在新节点
    # 位置插入
    def insert(self,index,val):
        p = self.head
        for i in range(index):
            if p.next is None:  # 超出位置最大范围结束循环
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node
    # 删除节点
    def del_node(self,val):
        p = self.head
        while p.next and p.next.val != val:
            p.next = p.next.next
        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next
    # 获取节点值,传入节点位置获取节点值 
    def get_index(self,index):
        # if index < 0:
        #     raise IndexError("list index  out range")
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("list index  out range")
            p = p.next
        return p.val
    # 修改节点值 ,传入节点位修改节点值  
    def modify_node(self,index,val):
        if index < 0:
            raise IndexError("list index  out range")
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("list index  out range")
            p = p.next
        p.val = val
        
        


if __name__=="__main__":
    l = LinkList()
    l.insert(100,5)
    l.init_list([6,5,9,8,7,])
    print(l.get_index(2))
    l.modify_node(4,9)
    l.show()






