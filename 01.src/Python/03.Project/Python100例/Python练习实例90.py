#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例37.py
# @Software: PyCharm

"""
题目：
    列表使用实例。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    list = [i for i in range(50) if i >20]  # 生成列表
    print list
    print len(list)  # 列表个数
    print list[0]
    print list[:4]
    print list[2:4]
    print list[2:]
    print list[-1]
    print list[-8:-1]

    list.append(111)  # 追加元素
    print list

    list.pop(0)  # 删除指定索引的元素
    print list
    print list.index(22)  # 寻找元素索引

    list.extend([1213])  # 扩展列表
    print list

    list.insert(0,12122)  # 插入元素
    print list

    list.remove(12122)  # 插入元素
    print list

    list.sort()  # 列表升序排序
    print list

    list.reverse()  # 列表反转
    print list


