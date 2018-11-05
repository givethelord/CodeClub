#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例38.py
# @Software: PyCharm

"""
题目：
    求一个3*3矩阵主对角线元素之和
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    list = [(1,2,3),(4,5,6),(7,8,9)]
    sum = 0
    for i in range(len(list)):
        sum += list[i][i]

    print sum
