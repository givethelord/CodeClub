#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    :
# @File    : Python练习实例80.py
# @Software: PyCharm

"""
题目：
    海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
-----------------------------------------------------
思路：
    问海滩上原来最少有多少个桃子，基数越小，总数越小。
-----------------------------------------------------
"""

if __name__ == "__main__":
    i = 0
    base_num = 1
    num_peach = 0
    while i < 5:
        num_peach = 4 * base_num
        for i in range(5):
            if num_peach % 4 != 0:
                break
            else:
                i += 1  # 为了最后一次退出while循环
            num_peach = num_peach / 4 * 5 + 1
        base_num += 1
    print num_peach

