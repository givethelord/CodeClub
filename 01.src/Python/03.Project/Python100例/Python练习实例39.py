#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例39.py
# @Software: PyCharm

"""
题目：
    有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
-----------------------------------------------------
思路：
    有序且元素少的使用二分插入排序法
-----------------------------------------------------
"""

list = [1,4,6,9,13,16,19,28,40,100]

num = input("输入一个数字:\n")




if num >= list[-1]:
    list.append(num)
else:
    n = 1
    while n > 0:
        n  = len(list)/2 
        if num > list[n]:
    
        elif num == list[-1]:
    
    else:




print list


