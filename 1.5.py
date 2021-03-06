# -*- coding:utf-8 -*-

"""
货币转换 I
描述
人民币和美元是世界上通用的两种货币之一，写一个程序进行货币间币值转换，其中：

人民币和美元间汇率固定为：1美元 = 6.78人民币。

程序可以接受人民币或美元输入，转换为美元或人民币输出。人民币采用RMB表示，美元USD表示，符号和数值之间没有空格。

注意：

(1) 这是一个OJ题目，获得输入请使用input()



输入


示例1：RMB123

示例2：USD20

输出


示例1：USD18.14

示例2：RMB135.60
"""

i=input()
try:
    money=eval(i[3:])
    if i[0:3]=="USD":
        mon = 6.78*money
        print("RMB{:.2f}".format(mon))
    elif i[0:3]=="RMB":
        mon = money / 6.78
        print("USD{:.2f}".format(mon))
    else:
        print("请在输入开头添加RMB（人民币）或 USD（美元）")
except:
    print("输入的格式为货币种类（RMB/USD)+货币数值")