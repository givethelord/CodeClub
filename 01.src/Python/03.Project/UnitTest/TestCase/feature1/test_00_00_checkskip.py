#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @File    : test_00_00_checkskip.py

"""
测试特性:
    有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
-----------------------------------------------------
测试思路:
    进行所有队列的排列组合，去掉不符合条件

测试结果:
    pass:
    failed:
-----------------------------------------------------
"""

import unittest
from TestContent.mathfunc import *
from Resource.common_init import common_init

if os.environ["run_env"] == "alpha":
    from Variables.alpha import *
elif os.environ["run_env"] == "beta":
    from Variables.beta import *
else:
    from Variables.gamma import *


class test_00_00_checkskip(unittest.TestCase):
    """测试skip"""

    @classmethod
    def setUpClass(cls):
        common_init.setUpClass()

    def setUp(self):
        common_init.setUp()

    def tearDown(self):
        common_init.tearDown()

    @classmethod
    def tearDownClass(cls):
        common_init.tearDownClass()

    @unittest.skip("我想临时跳过这个测试用例.")
    def test_add(self):
        """测试业务方法add"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """测试业务方法minus"""
        self.skipTest('跳过这个测试用例')
        self.assertEqual(1, minus(3, 2))

    @unittest.skipIf(1 == 1, "我想临时跳过这个测试用例.")
    def test_multi(self):
        """测试业务方法multi"""
        self.assertEqual(6, multi(2, 3))

    @unittest.skipUnless(1 == 2, "我想临时跳过这个测试用例.")
    def test_divide(self):
        """测试业务方法divide"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

    def test_print(self):
        """测试业务方法打印"""
        print("5 pass")


if __name__ == "__main__":
    unittest.main()
