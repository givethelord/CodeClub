#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例66.py
# @Software: PyCharm

"""
题目：
    输入3个数a,b,c，按大小顺序输出。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    a = input("输入a:\n")
    b = input("输入b:\n")
    c = input("输入c:\n")
    list = [a,b,c]

    for i in range(1,len(list)):
        if list[i-1] > list[i]:
            list[i-1],list[i] = list[i],list[i-1]
    print list