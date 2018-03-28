#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 21:16
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : f_recursion.py
# @Software: PyCharm

def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c,)
        move(n-1,b,a,c)

move(4,'A','B','C')
