#coding=utf-8
import math

def move(x,y,step,angle):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny

x1,y1=move(0,0,100,math.pi/6)
print(x1,y1)

result=move(0,0,200,math.pi/6)
print(result)
