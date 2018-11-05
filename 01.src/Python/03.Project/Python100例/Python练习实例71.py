#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    :
# @File    : Python练习实例71.py
# @Software: PyCharm

"""
题目：
    编写input()和output()函数输入，输出5个学生的数据记录。
-----------------------------------------------------
思路：

-----------------------------------------------------
"""
N = 5
stu = [['', '', []] for i in range(N)]


def stu_input(stu):
    for i in range(N):
        stu[i][0] = raw_input("input student's num:")
        stu[i][1] = raw_input("input student's name:")
        for j in range(3):
            stu[i][2].append(input("input student's score:"))

def stu_output(stu):
    for i in range(N):
        print "num:(%s) name(%s)" % (stu[i][0], stu[i][1])
        for j in range(3):
            print "score %d: %d" % (j + 1, stu[i][2][j])

if __name__ == '__main__':
    stu_input(stu)
    print stu
    stu_output(stu)
