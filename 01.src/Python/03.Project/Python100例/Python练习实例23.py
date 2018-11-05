#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例23.py
# @Software: PyCharm

"""
题目：
    打印出如下图案（菱形）
   *
  ***
 *****
*******
 *****
  ***
   *
-----------------------------------------------------
思路：
    str.center(width[,fillchar]) 
    center=>居中，width=》宽度，fill=》填充，char=》字符
-----------------------------------------------------
""" 


for i in range(4):
    i = 2 * i + 1
    str = "*"
    str *= i
    print str.center(7," ")

for i in range(3):
    i = 5 - 2 * i
    str = "*"
    str *= i
    print str.center(7," ")


