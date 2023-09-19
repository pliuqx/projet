# -*- coding: utf-8 -*-
#@File:  jm.py
#@Time:  2023/09/20     16:20:30
#@Author: 应无所住 、何生其心 
#@Version: python3.10
#@Software: VsCode 

import requests
from Crypto.Cipher import AES
 
inputfile = r'c:\test.ts'
outputfile = r'c:\测试.mp4'
keyfile = r'c:\key.m3u8'
 
with open(inputfile, 'rb') as f:
    video = f.read()
with open(keyfile, 'rb') as f:
    key = f.read()
 
aes = AES.new(key, AES.MODE_CBC, b'0000000000000000')
with open(outputfile, 'ab+') as f:
    f.write(aes.decrypt(video))