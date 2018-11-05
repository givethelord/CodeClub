#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例36.py
# @Software: PyCharm

"""
题目：
    求100之内的素数
-----------------------------------------------------
思路：
    同实例12
-----------------------------------------------------
""" 


from math import sqrt

def prime_number(a,b):
    prime_list = range(a,b+1)

    for i in prime_list[:]:
        k = int(sqrt(i + 1))
        for j in range(2,k+1):
            if i % j == 0:
                prime_list.remove(i)
                break
  
    print "total:%d" % len(prime_list)
    print prime_list

prime_number(1,100)
        

