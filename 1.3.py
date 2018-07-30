# -*- coding:utf-8 -*- #
#编写一个程序，计算输入数字N的0次方到5次方结果，并依次输出这6个结果，输出结果间用空格分隔。其中：N是一个整数或浮点数。#
"""
i=input()
try:
    i=eval(i)
    # if isinstance(i,int) and isinstance(i,float):
    #     print("Input Wrong!")
    # else:
    p=[i**0,i**1,i**2,i**3,i**4,i**5]
    for I in p:
        print(I,end=" ")    #输出以空格代替换行

except:
    print("The type of what you input is not INT OR FLOAT")

# 以上代码为自己思考得出，与答案相比多出最后一个“ ”
"""
i=input()
try:
    i=eval(i)
    list=[]
    for n in range(6):
        num=i**n
        list.append(str(num))
    print(" ".join(list))
#在第一次编写当中，直接使用了list.append(num)；在join函数中报错
except:
    print("The type of what you input is not INT OR FLOAT")
# i=input()
# i = eval(i)
# list = []
# for n in range(6):
#     num = i ** n
#     list.append(str(num))
# print(" ".join(list))