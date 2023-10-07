# -*- coding:utf-8 -*-
# @Time : 2023/10/12 15:54
# @Author: 应无所住，何生其心
# @File : bitree.py
# @Software : PyCharm


class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Bitree:
    def __init__(self, root = None):
        self.root = root

    def preorder(self,node):
        if node is None:
            return
        print(node.val)
        self.preorder(node.left)
        self.preorder(node.right)

    def inOrder(self,node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.val)
        self.inOrder(node.right)

    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val)




if __name__ == "__main__":
    # B F G D I H E C A
    b = Node("B")
    f = Node("f")
    g = Node("G")
    d = Node("D",f,g)
    i = Node("I")
    h = Node("H")
    e = Node("E",i,h)
    c = Node("C",d,e)
    a = Node("A",b,c)
    bt = Bitree(a)
    # bt.preorder(bt.root)
    bt.postorder(bt.root)


    pass