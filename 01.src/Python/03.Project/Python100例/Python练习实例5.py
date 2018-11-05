#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例5.py
# @Software: PyCharm

"""
题目：
    输入三个整数x,y,z，请把这三个数由小到大输出
-----------------------------------------------------
思路：
    x 与 y比较，选择最大的与z比较，如果z大，放到后面，如果z小再与最小的比得出顺序
-----------------------------------------------------
""" 
x = input("输入x：")
y = input("输入y：")
z = input("输入z：")

list =  [x,y,z]
list.sort()
print list