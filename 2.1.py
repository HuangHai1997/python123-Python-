"""

turtle正方形绘制


描述
使用turtle库，绘制一个正方形。

注意：这不是自动评阅题目，仅用于练习，没有评阅。


输出示例
正方形效果如下：
img/2-1.png


"""

# -*- coding:utf-8 -*-
import turtle as t
t.penup()
t.fd(-200)
t.pendown()
t.speed(1)
"""
t.fd(80)
t.seth(90)
t.fd(80)
t.left(90)
t.fd(80)
t.left(90)
t.fd(80)
t.left(90)
t.done()

#该方法为简略方法 下面使用循环语句
# turtle.left()/right() 中 ()内应该写上海龟转动的度数而非距离 该函数中海龟也是只转动不移动
"""
for i in range(4):
    t.fd(80)
    t.left(90)
t.done()