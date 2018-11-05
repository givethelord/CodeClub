#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例10.py
# @Software: PyCharm

"""
题目：
    暂停一秒输出，并格式化当前时间
-----------------------------------------------------
思路：
    暂停 time.sleep
    格式化时间 time.strftime
-----------------------------------------------------
""" 
import time


print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
time.sleep(1)
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))