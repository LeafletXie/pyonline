#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 11:39
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : list comprehensions.py
# @Software: PyCharm

L1=['Hello','World',18,'Apple',None]
L2=[x.lower() if isinstance(x,str) else x for x in L1]

#测试
print(L2)
if L2==['hello','world','apple']:
    print('测试通过！')
else:
    print('测试失败！')
