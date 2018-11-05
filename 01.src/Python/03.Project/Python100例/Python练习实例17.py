#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例17.py
# @Software: PyCharm

"""
题目：
    输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
-----------------------------------------------------
思路：
    可以利用for while循环
    1.
    英文字母：isalpha() 
    空格：isspace()
    数字：isdigit()
    2.正则
    3.利用字符在ASCII码中的位置逐个统计
-----------------------------------------------------
""" 

str = raw_input("输入一行字符:")
alpha_num,space_num,digit_num,other_num = 0,0,0,0

for i in str:
    if i.isalpha():
        alpha_num += 1
    elif i.isspace():
        space_num += 1
    elif i.isdigit():
        digit_num += 1
    else:
        other_num += 1

print "alpha_num:%d space_num:%d digit_num:%d ,other_num:%d" % (alpha_num,space_num,digit_num,other_num)


