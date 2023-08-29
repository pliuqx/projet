# -*- coding: utf-8 -*-
#@File    :   link_soft_merge.py
#@Time    :   2023/09/15 18:03:00
#@Author  :   应无所住 、何生其心 
#@Version :   python3.10
#@Software:   VsCode 


def merge(l1,l2):
    """
        要求:将L2合并到L1中
        思路: 1、定义一个变量P接收第一个链表的头部(p.head),定义第二个变量q接收第二个链表的指针(q.head.next);
              2、定义无限循环,结束条件是:while p.next is not None:
                 判断if,p.next.val < q.val: 如果第一个链表的值小于第二个链表的值
                 就将指针移动到下一个元素。
                 否则,1步、用过渡指针接收第一个链表的指会   (p.next)
                      2步、将第一个链表的指针(p.next)指向q(p.next=q)
                      3步、第一个链表的指针向下移动       (p=p.next)
                      4步、将第二个链表的q指向过渡指针tmp (q = tmp)
              3、第一个链表的指针(p.next)指向q            (p.next = q)
    """
    p = l1.head
    q = l2.head.next
    while p.next is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            tmp = p.next
            p.next = q
            p = p.next
            q = tmp
    p.next = q