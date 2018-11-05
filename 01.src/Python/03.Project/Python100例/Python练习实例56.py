#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例56.py
# @Software: PyCharm

"""
题目：
    画图，学用circle画圆形
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    from Tkinter import *

    canvas = Canvas(width=800, height=600, bg='yellow')  # 设置800x600的黄色画布
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)  # 通过两个坐标确定一个矩形,然后画出内切圆
        k += j
        j += 0.3

    mainloop()