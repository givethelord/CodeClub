#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例18.py
# @Software: PyCharm

"""
题目：
    ：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
-----------------------------------------------------
思路：
    
-----------------------------------------------------
""" 

n = input("输入项数：")
a = input("输入数字：")
sum = 0
sn = []
for i in range(1,n+1):
    sum += a * 10 ** (i-1)
    sn.append(sum)
print reduce(lambda x,y : x+y ,sn)