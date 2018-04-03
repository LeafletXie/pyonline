#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 16:41
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : f_normalize.py
# @Software: PyCharm

def normalize(name):
    return name[0:1].upper()+name[1:].lower()

# 测试
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)
