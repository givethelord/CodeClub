#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例54.py
# @Software: PyCharm

"""
题目：
    取一个整数a从右端开始的4〜7位。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    # 取整数十进制的4〜7位
    # a = str(input('input a number:\n'))
    # if len(a) < 6:
    #     print "please input seven digits"
    # else:
    #     print "From third to senventh digits about the digit(%s) is %s." % (a,a[-7:-3])

    # 取整数二进制的4〜7位
    a = input('input a number:\n')
    b = a >> 3  # 向右移动三位
    c = ~(~0 << 4)   # 设置一个低4位全为1,其余全为0的数
    d = b & c
    print '%d\t%s' % (a, bin(d).lstrip("0b").zfill(4))