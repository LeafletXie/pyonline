#coding=utf-8
import math #导入数学模块
list1=[12.2,9.8,7.7]

def area_sum(x): # 定义area_sum函数，圆的面积计算公式
    area=math.pi*x*x
    print(area) #输出圆的面积

for i in list1:
    area_sum(i) #调用函数
exit()

