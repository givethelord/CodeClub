#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例99.py
# @Software: PyCharm

"""
题目：
    有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    with open("A", "r+") as f1, open("B", "r+") as f2:
        a = f1.read()
        b = f2.read()
        with open("C", "a+") as f3:
            f3.write(a)
            f3.write(b)


