# -*- coding:utf-8 -*-
# @Time : 2022/2/8 11:09
# @Author: 应无所住，何生其心
# @File : file_save.py
# @Software : PyCharm

def firl_save(title,data):
    file.write(title + '\n' + data + '\n')
    # file.close()



if __name__ == '__main__':
    file = open('zz.txt', 'w+', encoding='utf-8')
    firl_save(title, data)
    pass
