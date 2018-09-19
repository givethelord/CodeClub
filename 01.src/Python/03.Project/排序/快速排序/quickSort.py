#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/6/26 20:35
# @Author  : Administrator
# @Site    : 
# @File    : quickSort.py
# @Software: PyCharm

"""
-----------------------------------------------------
Function:
1）选择一个基准元素,通常选择第一个元素或者最后一个元素,
2）通过一趟排序讲待排序的记录分割成独立的两部分，其中一部分记录的元素值均比基准元素值小。另一部分记录的 元素值比基准值大。
3）此时基准元素在其排好序后的正确位置
4）然后分别对这两部分记录用同样的方法继续进行排序，直到整个序列有序。

-----------------------------------------------------
"""
import random

def quickSort(nums):
    if len(nums) <= 1:
        return nums

    lessList = []  #定义左边子数组
    largelist = [] #定义右边子数组
    baseNum = nums.pop() #定义基数

    for i in nums:
        if i < baseNum:
            lessList.append(i)
        else:
            largelist.append(i)

    return quickSort(lessList) + [baseNum] + quickSort(largelist)

if __name__ == '__main__':
    nums = random.sample(range(100), 10)
    print(quickSort(nums))