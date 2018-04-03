#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 15:52
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : iteration.py
# @Software: PyCharm

for x in [1,2,3,4,5]:
    print(x)

it=iter([1,2,3,4,5])
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break
