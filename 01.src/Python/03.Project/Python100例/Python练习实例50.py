#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例50.py
# @Software: PyCharm

"""
题目：
    输出一个随机数。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""
import random

if __name__ == "__main__":
    print random.uniform(1,100)  # 生成一个指定范围内的随机符点数
    print random.random()  # 生成一个0到1的随机符点数
    print random.randint(1,100) # 生成一个指定范围内的整数
    print random.randrange(1,100,2)  # 从指定范围内，按指定基数递增的集合中 获取一个随机数
    print random.choice(range(10, 100, 2))  # 从序列中获取一个随机元素

    list1 = ["Python", "is", "best", "language"]
    random.shuffle(list1)
    print list1  # 将一个列表中的元素打乱
    print random.sample(range(100),5)  # 从指定序列中随机获取指定长度的片断
