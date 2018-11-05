#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例25.py
# @Software: PyCharm

"""
题目：
    求1+2!+3!+...+20!的和
-----------------------------------------------------
思路：
    
-----------------------------------------------------
""" 

def sum_phrase(n):
    """N阶求和"""

    T = 1
    sum = 0
    for i in range(1,n+1):
        T *= i
        sum += T
    print("1+2!+3!+...+%d!的和为%d。" % (n,sum))

sum_phrase(20)




