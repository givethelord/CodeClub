#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例33.py
# @Software: PyCharm

"""
题目：
    按逗号分隔列表
-----------------------------------------------------
思路：
    
-----------------------------------------------------
""" 

list = [1,2,3,4,5,6]

s1 = ','.join(str(n) for n in list)
print s1