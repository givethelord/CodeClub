#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @File    : test_02_00_checkparameter.py

"""
测试特性:

-----------------------------------------------------
测试思路:
    进行所有队列的排列组合，去掉不符合条件

测试结果:
    pass:
    failed:
-----------------------------------------------------
"""

import unittest
from nose_parameterized import parameterized


class test_02_00_checkparameter(unittest.TestCase):
    """测试验证"""

    # 异常验证
    @parameterized.expand([
        ("01", 1, 1),
        ("02", 2, 2),
        ("03", 3, 3)
    ])
    def test_parameter(self, a, b):
        """参数化
        """
        self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()