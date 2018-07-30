"""
星号三角形 I

描述
读入一个整数N，N是奇数，输出由星号字符组成的等边三角形，要求：

第1行1个星号，第2行3个星号，第3行5个星号，依次类推，最后一行共N的星号。

输入
示例1：3

输出
示例2：

 *
***

"""
"""
#-*- coding:utf-8 -*-
N=eval(input())
if N%2 == 0:
    print("请输入一个奇数")
else:
    for i in range(1,N+1):
        n=2*i-1
        xing=n*'*'
        all=2*N-1
        k=(all-n)//2
        kong=k*' '
        print("{}{}{}".format(kong,xing,kong))

#以上为杨辉三角 做错了。。。
"""
#-*- coding:utf-8 -*-
N=eval(input())
if N%2 == 0:
    print("请输入一个奇数")
else:
    for i in range(1,(N+1)//2+1):
        n=2*i-1
        xing=n*'*'
        k=(N-n)//2
        kong=k*' '
        print("{}{}{}".format(kong,xing,kong))


