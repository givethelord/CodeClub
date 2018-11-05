#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    :
# @File    : Python练习实例67.py
# @Software: PyCharm

"""
题目：
    输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    list = []
    for i in range(6):
        list.append(input('输入一个数字:\n'))
    n = len(list)
    max_i = 0
    min_i = 0
    for i in range(1,n):
        if list[max_i] < list[i]:
            max_i = i
    list[max_i], list[0] = list[0], list[max_i]

    for i in range(1,n):
        if list[min_i] > list[i]:
            min_i = i

    list[min_i], list[n - 1] = list[n - 1], list[min_i]
    print list

