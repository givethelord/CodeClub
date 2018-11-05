#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    :
# @File    : Python练习实例73.py
# @Software: PyCharm

"""
题目：
    反向输出一个链表。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    list = [input("please input the number:\n") for i in range(4)]
    print list
    list.reverse()
    print list