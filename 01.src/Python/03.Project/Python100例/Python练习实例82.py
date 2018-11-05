#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例82.py
# @Software: PyCharm

"""
题目：
    八进制转换为十进制
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    num = raw_input("8进制数：\n")

    sum = 0
    for i in range(len(num)):
        sum += 8 ** i * int(num[len(num) - 1 - i])
    print("转成10进制数为：%s" % sum)