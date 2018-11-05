#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例74.py
# @Software: PyCharm

"""
题目：
    列表排序及连接。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5, 6]

    # 排序
    a.sort(reverse=True)
    print a  # 降序
    a.sort()
    print a  # 升序
    a.sort(lambda x,y:y+x)
    print a

    # 链接
    print a + b
    a.extend(b)
    print a
