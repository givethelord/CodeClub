#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例8.py
# @Software: PyCharm

"""
题目：
    输出 9*9 乘法口诀表
-----------------------------------------------------
思路：
    分行与列考虑，共9行9列，i控制行，j控制列
-----------------------------------------------------
""" 

for i in range(1,10):
    print
    for j in range(1,i+1):
        print '%d*%d=%d' % (i,j,i*j),