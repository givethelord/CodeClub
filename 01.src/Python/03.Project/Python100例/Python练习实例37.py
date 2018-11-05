#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例37.py
# @Software: PyCharm

"""
题目：
    对10个数进行排序
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    list = [11,2,5,21,33,11,55,12,33,55]
    # list.sort()

    """交换法 稳定性不好,复杂度为O(n2)"""
    N = len(list)
    for i in range(N-1):
        min = i
        for j in range(i+1,N):
            if list[min] > list[j] : min = j # 如果最小值大于比较值，比较值就是最小值
        list[i],list[min] = list[min],list[i] # 交换最小值的位置跟当前位置

    print list
