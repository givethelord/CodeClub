#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例31.py
# @Software: PyCharm

"""
题目：
    请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
-----------------------------------------------------
思路：
    
-----------------------------------------------------
""" 


one = raw_input("请输入星期几的第一个字母：\n") 

if one.upper() == "M":
    print "The day is Monday"
elif one.upper() == "T":
    two = raw_input("请输入星期几的第二个字母：\n") 
    if two.upper() == "U":
        print "The day is Tuesday"
    else:
        print "The day is Thursday"
elif one.upper() == "W":
    print "The day is Wednesday"
elif one.upper() == "F":
    print "The day is Friday"
elif one.upper() == "S":
    two = raw_input("请输入星期几的第二个字母：\n") 
    if two.upper() == "A":
        print "The day is Saturday"
    else:
        print "The day is Sunday"


