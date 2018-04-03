#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 16:52
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : f_prod.py
# @Software: PyCharm

from functools import reduce
def f(x,y):
    return x*y
def prod(L):
    return reduce(f,L)

#测试
print('3*5*7*9=',prod([3,5,7,9]))
if prod([3,5,7,9])==945:
    print('测试成功！')
else :
    print('测试失败！')
