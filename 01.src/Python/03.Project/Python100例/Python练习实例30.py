#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/30 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例23.py
# @Software: PyCharm

"""
题目：
    一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
-----------------------------------------------------
思路：

-----------------------------------------------------
""" 

a = int(raw_input("请输入一个数字:\n"))
x = str(a)
flag = True

for i in range(len(x)/2):
    if x[i] != x[-i-1]:
        print("%d不是回文数" % a)
        break
else:       
    print("%d是回文数" % a)
