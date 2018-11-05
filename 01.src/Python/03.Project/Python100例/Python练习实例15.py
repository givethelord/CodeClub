#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例5.py
# @Software: PyCharm

"""
题目：
    利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
-----------------------------------------------------
思路：
    条件判断
-----------------------------------------------------
""" 


score = input("输入成绩：")

if score >= 90:
    print "A"
elif score >= 60:
    print "B"
else:
    print "C"