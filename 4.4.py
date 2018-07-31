"""
四叶玫瑰数


描述
四叶玫瑰数是4位数的自幂数。自幂数是指一个 n 位数，它的每个位上的数字的 n 次幂之和等于它本身。（例如：当n为3时，有1^3 + 5^3 + 3^3 = 153，153即是n为3时的一个自幂数，3位数的自幂数被称为水仙花数）


输入格式
该题目没有输入。




 输入输出示例



 	输入
示例 1	无 （红色字体只表示输入格式）
输出
1111

2222

3333 （红色字体只表示输出格式，不是四叶玫瑰数）

"""
# -*-coding:utf-8 -*-
def RoseNum(n):
    num=0
    while True:

        if len(str(num))>n:
            break
        else:
            sum=0
            for i in str(num):
                sum+=pow(eval(i),n)
            if sum == num and len(str(sum))==n:
                print(sum)
        num+=1



RoseNum(4)
"""
list=[]
strn=str(n)
for i in strn:
    list.append(i)
for j in list:
"""