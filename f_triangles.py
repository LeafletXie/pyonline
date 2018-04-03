#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 13:51
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : f_triangles.py
# @Software: PyCharm

def triangles():
    L=[1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]

# 测试
n=0
result=[]
for t in triangles():
    print(t)
    result.append(t)
    n=n+1
    if n==10:
        break

