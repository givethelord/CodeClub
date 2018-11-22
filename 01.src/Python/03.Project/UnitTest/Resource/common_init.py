#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/11/22 19:22
# @Author  : Administrator
# @Site    :
# @File    : common_init.py
# @Software: PyCharm

"""
-----------------------------------------------------
Function:


-----------------------------------------------------
"""
import unittest
import os

class common_init(unittest.TestCase):
    """进行用例前的准备工作"""

    # TestCase基类方法,所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        print("这里是所有测试用例前的准备工作")


    # TestCase基类方法,所有case执行之后自动执行
    @classmethod
    def tearDownClass(cls):
        print("这里是所有测试用例后的清理工作")

    @classmethod
    # TestCase基类方法,每次执行case前自动执行
    def setUp(cls):
        print("这里是一个测试用例前的准备工作")

    @classmethod
    # TestCase基类方法,每次执行case后自动执行
    def tearDown(cls):
        # os.rmdir("aaaa")
        print("这里是一个测试用例后的清理工作")
