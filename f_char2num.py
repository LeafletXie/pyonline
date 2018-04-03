#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 16:19
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : f_char2num.py
# @Software: PyCharm

from functools import reduce
def fn(x,y):
    return x*10+y

def char2num(s):
    digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn,map(char2num,'12345')))


