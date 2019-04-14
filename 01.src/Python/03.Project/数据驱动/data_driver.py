#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/4/13 17:02
# @Author  : Administrator
# @Site    :
# @File    : data_driver.py
# @Software: PyCharm

"""
-----------------------------------------------------
Function:


-----------------------------------------------------
"""
import unittest
import ddt
import time

test_data = [(
             'test_name', 'post', 'https://www.douban.com', '{"key": "value"}',
             '{"Content-Type": "text/plain;charset=UTF-8"}',
             '{"projectName": "pipe", "jobId": "70558866DFF6567A"}', 'data'), (
             'test_name2', 'get', 'https://www.douban.com', '{"key": "value"}',
             '{"Content-Type": "text/plain;charset=UTF-8"}',
             '{"projectName": "pipe", "jobId": "60558866DFF6567B"}', 'json')]
test_tuple = [('str1', 'type1'), ('str2', 'type2')]
test_list = ["var1", "var2", "var3"]
test_dict = [{"username": "zhangsan", "pwd": "zhangsan"},
             {"username": "lisi", "pwd": "lisi"},
             {"username": "wangwu", "pwd": "wangwu"},
             ]


@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(*test_data)
    @ddt.unpack
    def test_data_scence(self, test_name, method, url, dict, header, param,
                         type):
        print(
            "test_data_scence",
            test_name,
            method,
            url,
            eval(dict),
            eval(header),
            eval(param),
            type,
            time.asctime())

    @ddt.data(*test_list)
    def test_list_scence(self, var):
        print("test_list_scence", var)

    @ddt.unpack
    @ddt.data(*test_tuple)
    def test_tuple_scence(self, tuple_1, tuple_2):
        print("test_tuple_scence", tuple_1, tuple_2)

    @ddt.data(*test_dict)
    def test_dict_scence(self, dict):
        print("test_dict_scence", dict.get('username', None))


if __name__ == "__main__":
    unittest.main(verbosity=1)
