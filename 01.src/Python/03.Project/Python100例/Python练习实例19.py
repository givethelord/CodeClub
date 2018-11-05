#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例19.py
# @Software: PyCharm

"""
题目：
    一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
-----------------------------------------------------
思路：

-----------------------------------------------------
""" 

for i in range(1, 1001):
    sum = 0
    list = []
    for j in range(1, i):
        if i % j == 0:
            sum += j
            list.append(j)
    if sum == i:
        print(i)
        print(list)