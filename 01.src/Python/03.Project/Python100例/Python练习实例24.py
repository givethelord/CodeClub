#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例24.py
# @Software: PyCharm

"""
题目：
    有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
-----------------------------------------------------
思路：
    
-----------------------------------------------------
""" 

def sum(n):
    """数列的前20项之和"""
    sum = 0.0
    a = 1.0
    b = 1.0
    for i in range(n):
        a,b = b,a+b
        sum += a / b
    print sum

sum(20)


