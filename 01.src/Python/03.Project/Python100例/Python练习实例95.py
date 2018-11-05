#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例95.py
# @Software: PyCharm

"""
题目：
    字符串日期转换为易读的日期格式。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    from datetime import datetime
    text = '2012-09-20'
    y = datetime.strptime(text, '%Y-%m-%d')
    print y