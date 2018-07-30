#DayDayUp.py
# -*- coding:utf-8 -*-

#定义函数DayUp(df) 表示一年365天，每周工作5天休息2天，休息日下降1%,df表示工作日每天进步的程度
def DayUp(df):
    d=1.0
    for i in range(365):
        if i%7 in [0,6]:
            d = (1-0.01) * d
        else:
            d = (1+ df) * d
    return round(d,2)


#定义函数NoStop(fac) 表示一年365天都在进步，不停歇   fac代表每天进步程度
def NoStop(fac):
    d=1.0
    for i in range(365):
        d = (1+fac) * d
    return round(d,2)


#以下为MAIN函数

day=0.01

while DayUp(day) < NoStop(0.01):
    day=day+0.001

print("B君需要在工作日每天进步{:.3f}".format(day))

