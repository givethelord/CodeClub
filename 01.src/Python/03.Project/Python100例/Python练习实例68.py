#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例68.py
# @Software: PyCharm

"""
题目：
    有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    n = input('整数 n 为:\n')
    number = []
    for i in range(n):
        number.append(input('输入一个数字:\n'))
    m = input('向后移 m 个位置为:\n')
    m_list = number[-1-m:-1]
    n_list = number[:n-m]
    print  m_list + n_list
