"""
turtle六边形绘制


描述
使用turtle库，绘制一个六边形。

注意：这不是自动评阅题目，仅用于练习，没有评阅。


输出示例
六边形效果如下：
img/2-2.png

"""
import turtle as t
t.setup(600,600,0,0)
t.speed(2)
t.pensize(3)
for i in range(6):
    t.fd(80)
    t.right(-60)
t.done()