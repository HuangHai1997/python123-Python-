"""
整数加减和


描述
编写程序计算如下数列的值：

1-2+3-4...966

其中，所有数字为整数，从1开始递增，奇数为正，偶数为负

输入格式
该题目没有输入。

输入输出示例

 	    输入  	输出
示例 1	无	    111（仅表示输出样式，不是输出结果）
"""

"""
# -*- coding: utf-8 -*-
sum=0
for i in range(1,966+1):
    if i%2 == 0:
        i = -i
    sum = sum+i
print(sum)
"""

#以上为题目要求作答
#在下方加入自己的一个想法：输出整个算式
# -*- coding: utf-8 -*-

def SuanShi(N):
    sum = 0
    shizi = ""
    for i in range(1,N+1):
        if i%2 == 0:
            out = -i
            outstr = str(out)
        else:
            out = i
            outstr = "+"+str(out)
        shizi=shizi+outstr
        sum = sum+out
    print("{}={}".format(shizi[1:],sum))

SuanShi(996)