#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例81.py
# @Software: PyCharm

"""
题目：
    809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    a = 809

    for i in range(10,100):
        b = a * i
        if 10000 > b > 999 and 8 * i < 100 and 9 * i > 99:
            print i, b
