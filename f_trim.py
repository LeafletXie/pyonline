#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 22:08
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : f_trim.py
# @Software: PyCharm

def trim(s):
    if s[:1]==' ':
        s=s[1:]
    if s[-1:]==' ':
        s=s[:-1]
    return s

#测试
if trim('hello ')!='hello':
    print('测试失败！')
elif trim(' hello')!='hello':
    print('测试失败！')
elif trim(' hello ')!='hello':
    print('测试失败！')
elif trim(' hello world ')!='hello world':
    print('测试失败！')
elif trim('')!='':
    print('测试失败！')
elif trim('  ')!='':
    print('测试失败！')
else:
    print('测试成功!')
