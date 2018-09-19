# Python2.x与3​​.x版本区别

    Python的3​​.0版本，常被称为Python 3000，或简称Py3k。相对于Python的早期版本，这是一个较大的升级。
    为了不带入过多的累赘，Python 3.0在设计的时候没有考虑向下相容。
    许多针对早期Python版本设计的程式都无法在Python 3.0上正常执行。
    为了照顾现有程式，Python 2.6作为一个过渡版本，基本使用了Python 2.x的语法和库，同时考虑了向Python 3.0的迁移，允许使用部分Python 3.0的语法与函数。
    新的Python程式建议使用Python 3.0版本的语法。
    除非执行环境无法安装Python 3.0或者程式本身使用了不支援Python 3.0的第三方库。目前不支援Python 3.0的第三方库有Twisted, py2exe, PIL等。
    大多数第三方库都正在努力地相容Python 3.0版本。即使无法立即使用Python 3.0，也建议编写相容Python 3.0版本的程式，然后使用Python 2.6, Python 2.7来执行。
    Python 3.0的变化主要在以下几个方面:

## print 函数
print语句没有了，取而代之的是print()函数。 Python 2.6与Python 2.7部分地支持这种形式的print语法。在Python 2.6与Python 2.7里面，以下三种形式是等价的：
```python
print "fish"
print ("fish") #注意print后面有个空格
print("fish") #print()不能带有任何其它参数
```
然而，Python 2.6实际已经支持新的print()语法：
```python
from __future__ import print_function
print("fish", "panda", sep=', ')
```
## Unicode
Python 2 默认使用 ASCII 字母表,因此当您输入str() 类型Python 2 将以 ASCII 格式处理字符串。.unicode() 是单独的，不是 byte 类型。
现在， 在 Python 3，我们最终有了 Unicode (utf-8) 字符串，以及一个字节类：byte 和 bytearrays。
|python2|python3|表现|转换|作用|
由于 Python3.X 源码文件默认使用utf-8编码，这就使得以下代码是合法的：
>>> 中国 = 'china'
>>>print(中国)
china
Python 2.x
>>> str = "我爱北京天安门"
>>> str
'\xe6\x88\x91\xe7\x88\xb1\xe5\x8c\x97\xe4\xba\xac\xe5\xa4\xa9\xe5\xae\x89\xe9\x97\xa8'
>>> str = u"我爱北京天安门"
>>> str
u'\u6211\u7231\u5317\u4eac\u5929\u5b89\u95e8'
Python 3.x
>>> str = "我爱北京天安门"
>>> str
'我爱北京天安门'