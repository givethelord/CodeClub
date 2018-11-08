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
import numpy as np

base_list = [1, 2, 3]
base2_list = ["a", "b", "c"]
base_np = np.array(base_list)
base_np2 = np.array(base2_list)

# 一维数组基本运算
print(type(base_np))
print(base_np * 2)
print(base_np + base_np)

l = base_np < 2
print(l)
print(base_np[l])  # 获取符合条件的元素
print("a对应的数字:", base_np[base_np2 == "a"])  # 获取符合条件的元素
print("a不对应的数字:", base_np[base_np2 != "a"])  # 获取符合条件的元素


# n维数组基本运算
base_n_list = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 18]]
base_n_np = np.array(base_n_list)

print("类型:", type(base_n_np))
print("维度:", base_n_np.shape)  # 获取维度
print("第一列:", base_n_np[:, 0])  # 获取第一列
print(base_n_np * base_np)
print(base_n_np + base_np)
print("平均值:", np.mean(base_n_np))  # 获取平均值
print("中间元素:", np.median(base_n_np))  # 获取中间元素
print("标准差:", np.std(base_n_np))  # 获取标准差
print("相关系数:", np.corrcoef(base_n_np))  # 获取相关系数

