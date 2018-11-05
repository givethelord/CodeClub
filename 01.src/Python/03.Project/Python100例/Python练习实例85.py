#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例85.py
# @Software: PyCharm

"""
题目：
    输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    num = input("输入一个奇数:\n")
    i = 1
    sum = 9
    while sum % num != 0:
        sum += 9 * 10 ** i
        i += 1
    print sum


