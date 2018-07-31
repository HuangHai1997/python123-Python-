'''
#it's edit by HuangHai
#CalPiV1.py
#-*- coding:utf-8 -*-
pi=0
for k in range(1000):
    pi = pi + (1/pow(16,k))*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))

print(pi)
'''

"""
#it's edit by Mr.Song 
pi=0
N=100
for k in range(N):
    pi = pi + (1/pow(16,k))*\
#在python中使用 \ 进行换行
    (4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))

print("圆周率的值是:{}".format(pi))
"""
#-*- coding:utf-8 -*-
import random

s=1.00
num=0
N=1000**2
for i in range(N):
    x,y=random.random(),random.random()
if pow(pow(x,2)+pow(y,2),0.5)<=1.00:
    num+=1
print(4*(num/N))