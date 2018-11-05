#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例98.py
# @Software: PyCharm

"""
题目：
    从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    str1 = raw_input("please input the string:\n")
    with open("test", "a+") as f:
        f.write(str1.upper())
