#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例16.py
# @Software: PyCharm

"""
题目：
    输出指定格式的日期
-----------------------------------------------------
思路：
    使用 datetime 模块
-----------------------------------------------------
""" 

import datetime

# 输出今日日期，格式为 dd/mm/yyyy

print (datetime.date.today()).strftime("%d/%m/%Y")

# 创建日期对象
create_date = datetime.date(1922,3,2)

print create_date.strftime("%d/%m/%Y")


# 日期算术运算
tomorrow = create_date + datetime.timedelta(days=1)

print tomorrow

# 日期替换

src_date = datetime.date(1944,3,2)

print src_date

des_date = src_date.replace(year=tomorrow.year + 1)

print des_date


import time

print "UTC:",time.time()

print "Local Time:",time.localtime()

print "Format Time:",time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())