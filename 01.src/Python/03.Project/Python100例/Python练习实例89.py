#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    : 
# @File    : Python练习实例89.py
# @Software: PyCharm

"""
题目：
    某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

if __name__ == "__main__":
    num = raw_input("please input four digit:\n")
    list = []
    for i in range(len(num)):
        print i
        list.append((int(num[i]) + 5) % 10)

    print str(list[3]) + str(list[2]) + str(list[1]) + str(list[0])

