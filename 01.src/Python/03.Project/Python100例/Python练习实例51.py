#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例51.py
# @Software: PyCharm

"""
题目：
    学习使用按位与 &
-----------------------------------------------------
思路：
    0&0=0; 0&1=0; 1&0=0; 1&1=1
-----------------------------------------------------
"""

if __name__ == "__main__":

    num1 = 1
    num2 = 2
    if num1 & 1:
        print "the number1 is odd"
    else:
        print "the number1s is even"

    if num2 & 1:
        print "the number2 is odd"
    else:
        print "the number2 is even"
