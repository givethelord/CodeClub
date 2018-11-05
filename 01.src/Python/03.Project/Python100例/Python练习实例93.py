#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例93.py
# @Software: PyCharm

"""
题目：
    时间函数举例3。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    import time
    start = time.clock()
    time.sleep(3)
    end = time.clock()
    print 'different is %6.3f' % (end - start)