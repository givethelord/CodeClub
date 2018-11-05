#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例6.py
# @Software: PyCharm

"""
题目：
    斐波那契数列 {1,1,2,3,5,8......}
-----------------------------------------------------
思路：
    当n为1的时候，A1为1
    当n为n的时候, An为An-1 + An-2
-----------------------------------------------------
""" 


""" 方法1 """
# def fib1(n):

#     list,a,b = [1],0,1
#     if n == 1:
#         return list
#     for i in range(n-1):
#         a,b = b,b+a
#         list.append(b)
#     return list
        
# print fib1(11)

""" 方法2 """
def fib2(n):
    
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]    

    fibs = [1,1]    
    for i in range(2,n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print fib2(22)
