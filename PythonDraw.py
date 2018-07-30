# -*- coding:utf-8 -*-
#PythonDraw.py
"""
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,100)
turtle.fd(40*2/3)
turtle.done()

#以上为python蟒蛇绘制实例代码
"""

"""

import turtle
import math
import random
def step1(x,y):
    turtle.goto(x,y)
    turtle.speed(10)
    turtle.seth(45)
    turtle.fd(200)
    turtle.seth(-45)
    turtle.fd(200)
    turtle.seth(180)
    i = math.sqrt(2*200**2)
    turtle.fd(i)

count=1
list=[]
for t in range(50):
    list.append(t)
print(list)
while count<10:
    a=random.choice(list)
    b=random.choice(list)
    print(a,b)
    step1(a,b)
    count+=1


"""


"""
以上代码为自己测试使用turtle函数不断绘制一个等腰直接三角形
缺陷：   1.运行完后画布自动关闭
            //在程序结尾加入turtle.done() 程序在运行完后需手动关闭窗口
        2.在循环时，无法做到每次运行函数时都抬笔重新定义画笔的坐标，都是从上一个坐标画到下一个
            //使用函数turtle.penup()和turtle.pendown()
        3.“海龟“的初始函数无法自定义，需要学习下turtle.setup函数
        4.画布开启时候无法做到全屏化
        5.无法在画完一个完整图形化对其内部进行填充
        6.希望在接下去的代码中加入对与turtle的画笔的粗细大小颜色的定义以及样式的改变
        2018/7/25 15:36 Edit By：HuangHai
"""



