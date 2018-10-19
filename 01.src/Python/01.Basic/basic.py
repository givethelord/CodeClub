#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
在 Windows 下可以不写第一行注释:
#!/usr/bin/python
第一行注释标的是指向 python 的路径，告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器。
此外还有以下形式（推荐写法）：
#!/usr/bin/env python
这种用法先在 env（环境变量）设置里查找 python 的安装路径，再调用对应路径下的解释器程序完成操作。
"""

# -*- coding:utf-8 -*-
import logging

"""
第二行是
Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了
Python3.X 源码文件默认使用utf-8编码，所以可以正常解析中文，无需指定 UTF-8 编码。
"""
# @Time    : 2018/2/11 22:55
# @Author  : Administrator
# @Site    : 
# @File    : websocket.py
# @Software: PyCharm

"""
-----------------------------------------------------
Function:


-----------------------------------------------------
"""

"""
第三部分是文件描述
"""

import threading
import hashlib
import socket
import base64


"""
第四部分是引入的三方库
"""
