#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例1.py
# @Software: PyCharm

"""
题目：
    有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
-----------------------------------------------------
思路：
    进行所有队列的排列组合，去掉不符合条件

Function:
    4个数的排列组合：有序

-----------------------------------------------------
"""
count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print i,j,k
                count += 1
                print count

