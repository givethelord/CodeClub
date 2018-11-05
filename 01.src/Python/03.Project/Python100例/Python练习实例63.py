#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例63.py
# @Software: PyCharm

"""
题目：
    画椭圆。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    from Tkinter import *

    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width=400, height=600, bg='white')
    for i in range(20):
        canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()