#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    :
# @File    : Python练习实例61.py
# @Software: PyCharm

"""
题目：
    打印出杨辉三角形（要求打印出10行如下图）。
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
-----------------------------------------------------
思路：


-----------------------------------------------------
"""

if __name__ == "__main__":
    a = [[] for i in range(10)]
    n = 10
    for i in range(0, n):
        for j in range(0, i+1):
            if i > j > 0:
                a[i].append(a[i - 1][j] + a[i - 1][j - 1])
            else:
                a[i].append(1)
        print a[i]

