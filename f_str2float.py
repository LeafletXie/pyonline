#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 17:00
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : f_str2float.py
# @Software: PyCharm

from functools import reduce
DIGITS={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
L1,L2=[],[]
def str2float(s):
    for i in range(len(s)):
        if s[i]!='.':
            L1.append(s[i])
        else:
            j=i+1
            break
    L2=s[j:]
    return reduce(lambda x,y:x*10+y,map(char2num,L1))+reduce(lambda x,y:x*10+y,map(char2num,L2))/10**(len(s)-j)

#测试
print(str2float('123.456'))
