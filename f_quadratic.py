#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 21:52
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : f_quadratic.py
# @Software: PyCharm

import math
def quadratic(a,b,c):
    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1,x2

#测试
print('2x^2+3x+1=0的解为',quadratic(2,3,1))
print('x^2+3x-4=0的解为',quadratic(1,3,-4))

if quadratic(2,3,1)!=(-0.5,-1.0):
    print('测试失败')
elif quadratic(1,3,-4)!=(1.0,-4.0):
    print('测试失败')
else:
    print('测试成功')
