#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例94.py
# @Software: PyCharm

"""
题目：
    时间函数举例4,一个猜数游戏，判断一个人反应快慢。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    import time
    import random

    start = time.time()
    random_num = random.randint(1,100)
    while True:
        num = input("please gusee the num from 1 to 100.\n")

        if num == random_num:
            print "you are right"
            break
        elif num > random_num:
            print "the numer is large."
        else:
            print "the number is small"
    end = time.time()
    print "you use the time is %d second" % (end - start)
