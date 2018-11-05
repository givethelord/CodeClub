#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    :
# @File    : Python练习实例79.py
# @Software: PyCharm

"""
题目：
    字符串排序。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    str1 = "abcde"
    str2 = "efdis"
    str3 = "adk"

    if str1 > str2 : str2, str1 = str1, str2
    if str1 > str3 : str3, str1 = str1, str3
    if str2 > str3 : str2, str3 = str3, str2

    print str1, str2, str3

