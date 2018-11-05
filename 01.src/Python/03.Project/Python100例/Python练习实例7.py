#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例7.py
# @Software: PyCharm

"""
题目：
    将一个列表的数据复制到另一个列表中。
-----------------------------------------------------
思路：
    深层拷贝：[:]
-----------------------------------------------------
""" 
old_list = [1,2,3]
list = old_list[:]
print list