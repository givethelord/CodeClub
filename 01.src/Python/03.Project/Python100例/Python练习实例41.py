#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    :
# @File    : Python练习实例41.py
# @Software: PyCharm

"""
题目：
    模仿静态变量的用法
-----------------------------------------------------
思路：

-----------------------------------------------------
"""

# 通过类的__init__和__call__方法


class foo:
    def __init__(self, n=0):
        self.n = n

    def __call__(self, i):
        self.n += i
        return self.n


a = foo()
print a(1)
print a(2)
print a(3)
print a(4)

# 在函数中定义一个类

def foo2 (n=0):
  class acc:
    def __init__ (self, s):
      self.s = s
    def inc (self, i):
      self.s += i
      return self.s
  return acc (n).inc

a=foo2()
print a(1)
print a(2)
print a(3)
print a(4)

# 使用堆上的匿名参数
def foo3 (i, L=[]):
  if len(L)==0:
    L.append(0)
  L[0]+=i
  return L[0]

print foo3(1)
print foo3(2)
print foo3(3)
print foo3(4)
