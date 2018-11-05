#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例46.py
# @Software: PyCharm

"""
题目：
    求输入数字的平方，如果平方运算后小于 50 则退出
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":

    flag = True
    print "输入的数字小于 50，程序将停止运行"

    while flag:
        num = input("请输入数字:\n")
        if num ** 2 < 50:
            flag = False
        else:
            flag = True