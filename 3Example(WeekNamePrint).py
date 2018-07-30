#WeekNamePrint.py
#-*- coding:utf-8 -*-
"""
num=eval(input())
week=[1,2,3,4,5,6,7]
Week=[
    "星期一",
    "星期二",
    "星期三",
    "星期四",
    "星期五",
    "星期六",
    "星期日",
]
for i in range(6):
    if num == week[i]:
        print("现在是{}".format(Week[i]))
"""

"""
num=eval(input())
Week=[
    "星期一",
    "星期二",
    "星期三",
    "星期四",
    "星期五",
    "星期六",
    "星期日",
print("现在是{}".format(Week[num-1]))
"""

num=eval(input())
weekstr="星期一星期二星期三星期四星期五星期六星期日"
# start=3*(num-1)
# end=3*num
# i=weekstr[start:end]
i=weekstr[3*(num-1):3*num]
print("现在是{}".format(i))

