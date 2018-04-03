#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 13:30
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : f_odd.py
# @Software: PyCharm

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

#测试
o=odd()
next(o)
next(o)
next(o)
