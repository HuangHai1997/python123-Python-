"""
用户登录（三次机会）
描述
给用户三次输入用户名和密码的机会，要求如下：

1）如输入第一行输入用户名为‘Kate’,第二行输入密码为‘666666’，输出‘登录成功！’，退出程序；

2）当一共有3次输入用户名或密码不正确输出“3次用户名或者密码均有误！退出程序。”。



输入输出示例

示例 1

 	输入
Kate
666666

输出
登录成功！

示例 2

输入
kate
123
alice
456
john
111111

输出
3次用户名或者密码均有误！退出程序。
"""
# -*- coding:utf-8 -*-
def RightUser(rootname,rootpw):
    time = 0
    while True:
        time = time +1
        username=input()
        userpw=input()
        if username==rootname and userpw==rootpw:
            print("登录成功！")
            break
        elif time >= 3:
            print("3次用户名或者密码均有误！退出程序。")
            break
        else:
            continue

RightUser("Kate","666666")