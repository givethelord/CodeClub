#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例13.py
# @Software: PyCharm

"""
题目：
    打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
-----------------------------------------------------
思路：
    利用for循环控制100-999个数，每个数分解出个位，十位，百位
-----------------------------------------------------
""" 

def narcissistic(a,b):
    list = []
    for f in range(a,b+1):
        i = f / 100
        j = f / 10 % 10
        k = f % 10

        if i ** 3 + j ** 3 + k ** 3  == f:
            list.append(f)
    print "number:%d" % len(list)
    print list

narcissistic(100,999)