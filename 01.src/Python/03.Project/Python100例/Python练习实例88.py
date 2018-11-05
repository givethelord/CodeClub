#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例88.py
# @Software: PyCharm

"""
题目：
    读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    i = 0
    while i < 7:
        num = input("input a number:\n")

        if 50 >= num >= 1:
            print "*" * num
            i += 1
