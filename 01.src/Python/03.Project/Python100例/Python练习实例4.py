#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例4.py
# @Software: PyCharm

"""
题目：
    输入某年某月某日，判断这一天是这一年的第几天？
-----------------------------------------------------
思路：
    每个月份对应之前的天数之和+加上输入日
    年判断是否是闰年，如果是且月份大于2，就加一天
-----------------------------------------------------
""" 

year = input("输入年：")
month = input("输入月份：")
day = input("输入日：")

if month not in range(1,13):
    raise Exception("Invalid month!", month)

if (0 < day and day < 32):
    raise Exception("Invalid day!", day)

total_day = (0,31,59,90,120,151,181,212,243,273,304,334)

sum = total_day[month-1] + day

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) and (month > 2):
    sum += 1

print sum
