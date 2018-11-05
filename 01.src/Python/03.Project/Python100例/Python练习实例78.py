#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例78.py
# @Software: PyCharm

"""
题目：
    找到年龄最大的人，并输出。请找出程序中有什么问题。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    max = "li"

    for key in person.keys():
        if person[key] > person[max]:
            max = key
    print max,person[max]