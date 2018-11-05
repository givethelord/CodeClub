#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例87.py
# @Software: PyCharm

"""
题目：
    回答结果（结构体变量传递）
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    class student():
        x = 0
        c = 0

    def f(stu):
        stu.x = 20
        stu.c = 'c'
    a= student()
    a.x = 3
    a.c = 'a'
    f(a)
    print a.x,a.c
