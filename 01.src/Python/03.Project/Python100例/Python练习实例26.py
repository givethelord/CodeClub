#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例26.py
# @Software: PyCharm

"""
题目：
    利用递归方法求5!
-----------------------------------------------------
思路：

-----------------------------------------------------
""" 

"""方法一"""
def reduce_fuc(n):
    """求n阶"""

    if n == 1:
        return 1
    return n * reduce_fuc(n-1)

print reduce_fuc(5)


"""方法二：递归函数,也可做个死循环,循环五次"""

print reduce(lambda x,y : x*y,range(1,6))