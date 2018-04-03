#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 12:49
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : f_findMinAndMax.py
# @Software: PyCharm

def findMaxAndMin(L):
    if len(L)==0:
        return (None,None)
    max=L[0]
    min=L[0]
    for n in L:
        if n>max:
            max=n
        if n<min:
            min=n
    return (min,max)

# 测试
if findMaxAndMin([])!=(None,None):
    print('测试失败1！')
elif findMaxAndMin([7])!=(7,7):
    print('测试失败2！')
elif findMaxAndMin([7,1])!=(1,7):
    print('测试失败3！')
elif findMaxAndMin([7,1,3,9,5])!=(1,9):
    print('测试失败4！')
else:
    print('测试成功！')
