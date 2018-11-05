#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例29.py
# @Software: PyCharm

"""
题目：
    给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
-----------------------------------------------------
思路：

-----------------------------------------------------
""" 

def func(n):
    """"""

    """方法一"""
    # str_num = str(n)
    # print("%d是%d位数,逆序%s:" % (n,len(str_num),str_num[::-1]))

    """方法二"""
    
    list = []
    for i in range(4,-1,-1):
        num = n / 10 ** i
        if num > 0:
            list.append(num)
            n = n - num * 10 ** i
    
    print("%s是%d位数,逆序%s:" % (list,len(list),list[::-1]))

func(1212)
