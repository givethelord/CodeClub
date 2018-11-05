#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例14.py
# @Software: PyCharm

"""
题目：
   将一个正整数分解质因数
-----------------------------------------------------
思路：
    1.先找到一个最小的质数k=2
    2.如果k=n,则结束；k <> n,则 判断 n / k 是否能整除
    3.如果能整除,商为1,结束;商不为1,获取商重复步骤二;
    4.如果不能,判断 n / k+1 是否能整除 （因为如果除数是合数的话，被除数早就会比除数更小的质数整除）
-----------------------------------------------------
""" 

def reduceNum(n):

    for k in range(2,n+1):      
        if n % k == 0: # n 被k整除
            n /= k   #获取商
            if n == 1: # 如果k=n
                print k
                exit(0)  # 退出递归
            else:
                print '{} * '.format(k),
                reduceNum(n)

reduceNum(90)
