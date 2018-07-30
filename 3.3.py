"""
天天向上的力量 III
描述
一年365天，以第1天的能力值为基数，记为1.0。
当好好学习时，能力值相比前一天提高N‰；当没有学习时，能力值相比前一天下降N‰。
每天努力或放任，一年下来的能力值相差多少呢？其中，N的取值范围是0到100，N可以是小数，假设输入符合要求。
获得用户输入的N，计算每天努力和每天放任365天后的能力值及能力间比值，其中，能力值保留小数点后2位，能力间比值输出整数，输出结果间采用英文逗号分隔。
使用input()获得N。

输入
示例1：
1

输出
示例1：
1.44,0.69,2
"""
# -*- coding:utf-8 -*-
N=eval(input())
n=N*0.001
abi=1.0
def UP(a,b):
    for i in range(365):
        b=b*(1+a)
    return b
def DOWN(a,b):
    for i in range(365):
        b=b*(1-a)
    return b

up=UP(n,abi)

down=DOWN(n,abi)
bizhi=int(up/down)
#该处之所以使用int是因为在老师评测当中 取整数代表直接去掉小数部分
#而round函数是对其四舍五入
print("{:.2f},{:.2f},{}".format(up,down,bizhi))