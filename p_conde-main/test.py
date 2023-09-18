# -*- coding:utf-8 -*-
# @Time : 2021/10/8 17:29
# @Author: 应无所住，何生其心
# @File : test.py
# @Software : PyCharm


for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, 'x', j, '=', i * j, end=' ')
    print('')


from bs4 import BeautifulSoup as bf
from pandas import DataFrame as df
from openpyxl import Workbook as wb

import sys
import os
import xlrd
import xlwt
import numpy as np
import numpy as np