#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/11/7 19:13
# @Author  : Administrator
# @Site    :
# @File    : practice_numpy.py
# @Software: PyCharm

"""
-----------------------------------------------------
Function:


-----------------------------------------------------
"""
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))  # 画布的大小为长8cm高6cm

x_list = [100, 200, 300, 400, 500]
y_list = [2012, 2013, 2014, 2015, 2016]
colour = ["red", "black", "blue", "green", "gray"]
point_shape = "s"
point_bright = 1
point_size = [1, 2, 3, 4, 5]
line_width = [1, 2, 3, 4, 5]

plt.plot(x_list, x_list)  # 根据坐标画线
plt.show()  # 显示图像
plt.clf()  # 清理上个图像

plt.scatter(
    x_list,
    x_list,
    s=point_size,
    c=colour,
    marker=point_shape,
    alpha=point_bright,
    linewidths=line_width)  # 根据坐标打点 点的大小 颜色 形状 亮度 线宽
plt.xscale('log')  # 改变x坐标的刻度值
plt.show()
plt.clf()

plt.hist(x_list)  # 直方图 可选参数bins=10
plt.show()
plt.clf()

plt.hist(x_list, 10)   # 直方图，显示五条数据，可选参数bins默认为10

plt.show()
plt.clf()

xlab = "x-content"
ylab = "y-content"
title = "the title"

plt.xlabel(xlab)  # 设置横坐标的标签
plt.ylabel(ylab)  # 设置纵坐标的标签
plt.title(title)  # 设置标题
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
plt.xticks(tick_val, tick_lab)  # 设置横坐标的刻度值和显示标签
plt.grid()  # 生成网格

plt.show()
plt.clf()
