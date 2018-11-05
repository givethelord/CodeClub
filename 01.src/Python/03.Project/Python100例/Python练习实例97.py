#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例97.py
# @Software: PyCharm

"""
题目：
    从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    filename = raw_input("please input the file name.\n")
    f = open(filename, "a+")
    ch = ""
    while ch != "#":
        f.write(ch)
        ch = raw_input('please write the cha in the file:\n')
    f.close()
