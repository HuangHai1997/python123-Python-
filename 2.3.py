"""
turtle叠边形绘制


描述
使用turtle库，绘制一个叠边形，其中，叠边形内角为80度。

注意：这不是自动评阅题目，仅用于练习，没有评阅。


输出示例
叠边形效果如下：
img/2-3.png

"""
import turtle as t
t.setup(600,600,0,0)
t.speed(2)
for i in range(9):
    t.fd(100)
    t.left(80)
t.done()