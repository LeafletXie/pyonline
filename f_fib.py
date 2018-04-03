#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 13:20
# @Author  : Wuhua Xie
# @Site    : Collage Of Civil Engineering, Hunan University
# @File    : f_fib.py
# @Software: PyCharm

def fib(n):
    i,a,b=0,0,1
    while i<n:
        yield b
        a,b=b,a+b
        i=i+1
    return 'done'

#测试
f=fib(6)
for x in f:
    print(x)

g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

