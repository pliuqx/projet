# -*- coding:utf-8 -*-
# @Time : 2023/9/19 14:30
# @Author: 应无所住，何生其心
# @File : app_stack.py
# @Software : PyCharm

"""
  要求：
    1、将一段字符中的（）[]{},找出来看看有没有不配对的，嵌套的不影响
"""



from lstack import Lstack

def parenthesis_matching(str_txt):
    st = Lstack()
    left = "([{"
    right = ")]}"
    for i in str_txt:
        if i in left:
            st.push(i)
        else:
            if i in right and st.is_empty():
                print(f"{i}没有匹配到")
            elif i in right:
                st.pop()
            
                
    while not st.is_empty():
        print(st.pop())
        # print(st.top())





if __name__ == "__main__":
    txt = "(董向荣认为，(韩国)检方调查李在明很早就已经开始。韩国政治通常是“胜者为王、败者为寇”，当选者对{政治对}手进行清算或者打击是韩国政坛比较常见的政治斗争手段。此时提起对李在明的拘捕申请，也有向李在明“泼脏水”的意味。保守派可以引导韩国民众质疑[李在明]，让[民众]怀疑他有可能渎职贪腐、没有那么“伟大”。)"
    parenthesis_matching(txt)
    pass