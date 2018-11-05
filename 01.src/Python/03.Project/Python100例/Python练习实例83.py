#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例83.py
# @Software: PyCharm

"""
题目：
    求0—7所能组成的奇数个数。
-----------------------------------------------------
思路：
组成1位数是4个。
组成2位数是7*4个。
组成3位数是7*8*4个。
组成4位数是7*8*8*4个。

-----------------------------------------------------
"""

if __name__ == "__main__":
    s = 4
    sum = 4
    for i in range(2,9):
        print sum
        if i <= 2:
            s *= 7
        else:
            s *= 8
        sum += s
    print sum