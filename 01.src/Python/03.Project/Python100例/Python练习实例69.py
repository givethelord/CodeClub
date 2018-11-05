#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例69.py
# @Software: PyCharm

"""
题目：
    有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    n = input("请输入总人数:\n")
    circle = []
    for i in range(1,n+1):
        circle.append(i)

    i = 0
    count = 0
    del_num = 0
    while del_num < n -1:
        if circle[i] != 0 : count += 1
        if count == 3:
            circle[i] = 0
            count = 0
            del_num += 1
        i += 1
        if i == n : i = 0

    i = 0
    while circle[i] == 0: i += 1
    print i,circle[i]

