"""
求100以内的素数和
描述
求100以内的素数之和并输出。

输入格式
 该题目没有输入

输入输出示例
 	    输入  	                                输出
示例1	无（红色字体不是OJ的输入）	                说明：直接输出100以内的素数之和。（红色字体不是OJ的输出）
"""
#-*- coding:utf-8 -*-


#输出X是/不是素数
def SuShu(N):
    sum=0
    for i in range(1,N+1):# i 代表的是要判断是否为素数的数
        if i==1 :
            continue
        elif i==2:
            print("{}是素数".format(i))
            continue
        for j in range(2,i):# j 代表的是要被i整除的除数 其范围在2到他本身
            if i%j !=0:
                continue
            elif i%j == 0:
                print("{}不是素数".format(i))
                break
        else:
            print("{}是素数".format(i))

def SuShuHe(N):
    sum=0
    for i in range(1,N+1):# i 代表的是要判断是否为素数的数
        if i == 2:
            sum=sum+i
            continue
        elif i == 1:
            continue
        for j in range(2,i):# j 代表的是要被i整除的除数 其范围在2到他本身
            if i%j !=0:
                continue
            elif i%j == 0:
                break
        else:
            sum=sum+i
    print(sum)
SuShuHe(100)
SuShu(3)







"""
2018.7.31 1:19
写于深夜思考身旁无纸

什么是素数呢？
素数只有1 和 它 本身两个因数
所以 任何一个素数除以另一个数（除了1和他本身）的余数都不为0
"""



