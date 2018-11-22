#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @File    : test_01_00_checkverify.py

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


class test_01_00_checkverify(unittest.TestCase):
    """测试验证"""

    # 异常验证
    def test_assertRaises(self):
        """异常验证
        assertRaises(
        exception,  # 待验证异常类型
        callable,  # 待验证方法
        *args,  # 待验证方法参数
        **kwds # 待验证方法参数(dict类型)
        )
        """
        self.assertRaises(ZeroDivisionError, add(), 1, 2)


    def test_assertRaisesRegexp(self):
        """异常匹配验证

        assertRaisesRegexp(exception, regexp, callable, *args, **kwds)
        """
        self.assertRaisesRegexp(1, minus(3, 2))

    # 基本断言方法
    def test_assertEqual(self):
        """assertEqual(arg1, arg2, msg=None)
        验证arg1=arg2，不等则fail
        """
        self.assertEqual(1, 1)

    def test_assertNotEqual(self):
        """assertNotEqual(arg1, arg2, msg=None)

        验证arg1 != arg2, 相等则fail
        """
        self.assertNotEqual(1, 2)

    def test_assertTrue(self):
        """assertTrue(expr, msg=None)

        验证expr是true，如果为false，则fail
        """
        self.assertTrue(True)

    def test_assertFalse(self):
        """assertFalse(expr,msg=None)
        验证expr是false，如果为true，则fail
        """
        self.assertFalse(False)

    def test_assertIs(self):
        """assertIs(arg1, arg2, msg=None)
        验证arg1、arg2是同一个对象，不是则fail
        """
        self.assertIs(1, 2)

    def test_assertIsNot(self):
        """assertIsNot(arg1, arg2, msg=None)
        验证arg1、arg2不是同一个对象，是则fail
        """
        self.assertNotEqual(1, 2)

    def test_assertIsNone(self):
        """assertIsNone(expr, msg=None)
        验证expr是None，不是则fail
        """
        self.assertIsNone(1, 2)

    def test_assertIsNotNone(self):
        """assertIsNotNone(expr, msg=None)
        验证expr不是None，是则fail
        """
        self.assertIsNotNone(1, 2)

    def test_assertIn(self):
        """assertIn(arg1, arg2, msg=None)
        验证arg1是arg2的子串，不是则fail
        """
        self.assertIn(1, 2)

    def test_assertIsNone(self):
        """assertNotIn(arg1, arg2, msg=None)
        验证arg1不是arg2的子串，是则fail
        """
        self.assertNotIn(1, 2)

    def test_assertIsInstance(self):
        """assertIsInstance(obj, cls, msg=None)
        验证obj是cls的实例，不是则fail
        """
        self.assertIsInstance(1, 2)

    def test_assertNotIsInstance(self):
        """assertNotIsInstance(obj, cls, msg=None)
        验证obj不是cls的实例，是则fail
        """
        self.assertNotIsInstance(1, 2)

    # 比较断言
    def test_assertAlmostEqual(self):
        """assertAlmostEqual(first, second, places = 7, msg = None, delta = None)
        验证first约等于second。
        palces: 指定精确到小数点后多少位，默认为7
        """
        self.assertAlmostEqual(1, 2)

    def test_assertNotAlmostEqual(self):
        """assertNotAlmostEqual (first, second, places, msg, delta)
        验证first不约等于second。
        palces: 指定精确到小数点后多少位，默认为7
        """
        self.assertNotAlmostEqual(1, 2)

    def test_assertGreater(self):
        """assertGreater(first, second, msg = None)
        验证first > second，否则fail
        """
        self.assertGreater(1, 2)

    def test_assertGreaterEqual(self):
        """assertGreaterEqual(first, second, msg = None)
        验证first ≥ second，否则fail
        """
        self.assertGreaterEqual(1, 2)

    def test_assertAlmostEqual(self):
        """assertAlmostEqual(first, second, places = 7, msg = None, delta = None)
        验证first约等于second。
        palces: 指定精确到小数点后多少位，默认为7
        """
        self.assertAlmostEqual(1, 2)

    def test_assertLess(self):
        """assertLess (first, second, msg = None)
        验证first < second，否则fail
        """
        self.assertLess(1, 2)

    def test_assertLessEqual(self):
        """assertLessEqual (first, second, msg = None)
        验证first ≤ second，否则fail
        """
        self.assertLessEqual(1, 2)

    def test_assertRegexpMatches(self):
        """assertRegexpMatches (text, regexp, msg = None)
        验证正则表达式regexp搜索==匹配==的文本text。
        regexp：通常使用re.search()
        """
        self.assertRegexpMatches(1, 2)

    def test_assertNotRegexpMatches(self):
        """assertNotRegexpMatches(text, regexp, msg = None)
        验证正则表达式regexp搜索==不匹配==的文本text。
        regexp：通常使用re.search()
        """
        self.assertNotRegexpMatches(1, 2)

    # 复杂断言
    def test_assertListEqual(self):
        """assertListEqual (list1, list2, msg = None)
        验证列表list1、list2相等，不等则fail，同时报错信息返回具体的不同的地方
        """
        self.assertListEqual(1, 2)

    def test_assertRegexpMatches(self):
        """	assertTupleEqual (tuple1, tuple2, msg = None)
        验证元组tuple1、tuple2相等，不等则fail，同时报错信息返回具体的不同的地方
        """
        self.assertTupleEqual(1, 2)

    def test_assertSetEqual(self):
        """assertSetEqual(set1, set2, msg = None)
        验证集合set1、set2相等，不等则fail，同时报错信息返回具体的不同的地方
        """
        self.assertSetEqual(1, 2)

    def test_assertDictEqual(self):
        """	assertDictEqual(expected, actual, msg = None)
        验证字典expected、actual相等，不等则fail，同时报错信息返回具体的不同的地方
        """
        self.assertDictEqual(1, 2)


if __name__ == "__main__":
    unittest.main()
