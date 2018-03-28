#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 20:47
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : f_product.py
# @Software: PyCharm

def product(*nums):
    result=1
    for n in nums:
        result=result*n
    return result

#测试
print('product(5)=',product(5))
print('product(5,6)=',product(5,6))
print('product(5,6,7)=',product(5,6,7))
print('product(5,6,7,9)=',product(5,6,7,9))
if product(5)!=5:
    print('测试失败！')
elif product(5,6)!=30:
    print('测试失败！')
elif product(5,6,7)!=210:
    print('测试失败！')
elif product(5,6,7,9)!=1890:
    print('测试失败！')

