#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例12.py
# @Software: PyCharm

"""
题目：
    判断101-200之间有多少个素数，并输出所有素数。
-----------------------------------------------------
思路：
    素数，又称质数，定义是：除了1和它本身以外不再有其他的除数整除。
    1.按照定义，从2到n-1判断有没有能整除n的数。如果有，则不是素数，否则，是素数 算法复杂度：O(n)
    2.从2一直算到sqrt(n)，这样算法复杂度降低了很多 O(sqrt(n))
    3.米勒拉宾素数(伪素数):如果p为素数，x是小于p的正整数， 且x^2 mod p = 1 ，说明p能够整除（x+1）（x-1）。但是p是素数，那么只可能是x-1能被p整除(此时x=1)或x+1能被p整除(此时 x=p-1)

    去掉1和2、偶数
-----------------------------------------------------
""" 
 
from math import sqrt

def prime_number(a,b):
    prime_list = range(a,b+1)

    for i in prime_list[:]:
        # if i !=2 and not i & 1: # 位运算判断偶数
        #     prime_list.remove(i) # 移除合数
        #     continue
        k = int(sqrt(i + 1))
        for j in range(2,k+1):
            if i % j == 0:
                prime_list.remove(i)
                break

    
    print "total:%d" % len(prime_list)
    print prime_list

prime_number(101,200)
        

          
