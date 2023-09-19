# -*- coding:utf-8 -*-
# @Time : 2023/9/20 17:05
# @Author: 应无所住，何生其心
# @File : decrypt_func.py
# @Software : PyCharm

import requests
from Crypto.Cipher import AES

def decrypt(key_url,str_txt):
    key = requests.get(key_url).content
    cryptor = AES.new(key, AES.MODE_CBC, key)
    # ts.write(cryptor.decrypt(res_ts))
    pass

if __name__ == "__main__":
    pass