#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例27.py
# @Software: PyCharm

"""
题目：
    利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来

-----------------------------------------------------
思路：

-----------------------------------------------------
""" 


str = raw_input("所输入的5个字符:").rstrip("\r")

print reduce(lambda x,y: (x,y) ,str[::-1])


