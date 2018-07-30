"""
turtle同切圆绘制


描述
使用turtle库，绘制一个同切圆。

注意：这不是自动评阅题目，仅用于练习，没有评阅。


输出示例
同切圆效果如下：
img/2-4.png

"""
# -*- coding:utf-8 -*-
import turtle as t
t.setup(600,600,0,0)
t.penup()
t.seth(-90)
t.fd(150)
t.seth(0)
t.pendown()
t.speed(3)
t.pensize(3)
list=[100,120,140,160]
for i in list:
    t.circle(i)
t.done()
