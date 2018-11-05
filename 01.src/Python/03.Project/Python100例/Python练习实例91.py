#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例91.py
# @Software: PyCharm

"""
题目：
    时间函数举例1。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    import time
    print time.time()
    print time.localtime()
    print time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    print time.ctime(time.time())
    print time.asctime(time.localtime(time.time()))
    print time.asctime(time.gmtime(time.time()))