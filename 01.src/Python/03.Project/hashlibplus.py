#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/25 21:59
# @Author  : Administrator
# @Site    :
# @File    : hashlibplus.py
# @Software: PyCharm

"""
-----------------------------------------------------
Function:


-----------------------------------------------------
"""
import hashlib


var_str = "hello world"
# md5方法接收byte类型的数据即b'', hexdigest转为md5值
md5_obj = hashlib.md5(var_str.encode()).hexdigest()
print(type(md5_obj), md5_obj)