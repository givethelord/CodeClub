#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例52.py
# @Software: PyCharm

"""
题目：
    学习使用按位或 | 。
-----------------------------------------------------
思路：
    0|0=0; 0|1=1; 1|0=1; 1|1=1
-----------------------------------------------------
"""

if __name__ == "__main__":

    num1 = 1
    num2 = 3
    num3 = 2
    num4 = 4
    print num1 | num2
    print num1 | num3
    print num3 | num4
