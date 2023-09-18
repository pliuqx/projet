# -*- coding:utf-8 -*-
# @Time : 2022/1/5 14:39
# @Author: 应无所住，何生其心
# @File : FileSave.py
# @Software : PyCharm



def save(self, data):
    file = open('zz.txt', 'a+', encoding='utf-8')
    file.write(telte + '\n' + str(data))  # 写入章节名字,加入换行符,写入文章正文
    # file.write('\r\n')  # 加入换行符
    # file.write(str(data))  # 写入文章正文


if __name__ == '__main__':
    pass
