"""
合格率计算

描述
输入一个数字n作为合格标准，然后，输入一系列的数字，每次输入换行表示，空换行结束，输出合格率。

合格率指输入元素中合格元素与全部元素的比值。


输入输出示例
 	输入
示例 1
60
50
75
90
(这里有一个换行 )

输出
合格率为66.67%


示例 2
75
65
70
90
(这里有一个换行 )

合格率为33.33%
"""

# 该函数用于获取多行输入的值 当且仅当输入为数字时候将数字列入数组list
# 当输入为空时候，跳出while循环 ； 当输入为负数或者浮点数时候，跳出提示信息

def INPUT():
    list=[]
    while True:
        try:
            inp = eval(input())
            # 该程序缺陷所在 无法用int代替eval 否则在空输入后会直接跳到except 而不会break该循环
            # 该思考为何在int 函数中 空输入不会出现SyntaxError异常
            if inp >= 0:
                list.append(inp)
            else:
                print("请输出非负整数")
        except SyntaxError:
            break
        except:
            print("请输入非负整数")
    return list


NUM=INPUT()
n=NUM[0]
Pass=0
NoPass=0
for i in NUM[1:]:
    if i<n:
        NoPass+=1
    else:
        Pass+=1
Total=NoPass+Pass
if Total==0:
    out=100
else:
    out=100*Pass/(NoPass+Pass)
print("合格率为{:.2f}%".format(out))

"""
#以下为嵩天老师给出的代码

i=0
j=0
m=int(input())
s=input()
while s!="stop":
    i=i+1
    num=int(s)
    if num>=m:
        j=j+1
    s=input()
if j==0:
    print("及格率为100%")
else:
    print("及格率为{:.2f}%".format((j/i)*100))

"""
