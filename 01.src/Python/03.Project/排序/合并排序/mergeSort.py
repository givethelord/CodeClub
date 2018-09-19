#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/6/26 20:49
# @Author  : Administrator
# @Site    : 
# @File    : mergeSort.py
# @Software: PyCharm

"""
-----------------------------------------------------
Function:
是将两笔已排序的数据合并并进行排序，如果所读入的数据尚未排序，可以先利用其它的排序方式来处理这两笔数据，然后再将排序好的这两笔数据合并。

-----------------------------------------------------
"""
import random

def recursiveSort(number1, number2):
    """

    :param number1:
    :param number2:
    :return:

    递归实现
    """

    if len(number1) == 0:
        return number2
    elif len(number2) == 0:
        return number1
    elif number1[0] < number2[0]:
        return [number1[0]] + recursiveSort(number1[1:],number2)
    else:
        return [number2[0]] + recursiveSort(number2[1:],number1)

def sort(number1,number2):
    """

    :param number1:
    :param number2:
    :return:

    非递归
    """
    len1 = len(number1)
    len2 = len(number2)
    if len1 == 0:
        return number2
    elif len2 == 0:
        return number1
    else:
        i = 0
        j = 0
        list = []
        while i < len1 and j < len2:
            if number1[i] <= number2[j]:
                list.append(number1[i])
                i += 1
            else:
                list.append(number2[j])
                j += 1

        while i < len1:
            list.append(number1[i])
            i += 1
        while j < len2:
            list.append(number2[j])
            j += 1
    return list

if __name__ == "__main__":
    number1 = random.sample(range(100), 10)
    number2 = random.sample(range(100), 10)
    number1.sort()
    number2.sort()
    print(recursiveSort(number1,number2))
    print(sort(number1, number2))
