#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例76.py
# @Software: PyCharm

"""
题目：
    编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    n = input("please input the num:\n")
    sum = 0.0
    if n & 1 :
        for i in range(1, n + 1,2):
            sum += 1.0 / i
    else:
        for j in range(2, n + 1,2):
            sum += 1.0 / j
    print sum