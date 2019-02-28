# Pytest

pytest是python的一种单元测试框架，与python自带的unittest测试框架类似，但是比unittest框架使用起来更简洁，效率更高,适合从简单的单元到复杂的功能测试。

* 非常容易上手，入门简单，文档丰富，文档中有很多实例可以参考
* 能够支持简单的单元测试和复杂的功能测试
* 支持参数化
* 执行测试过程中可以将某些测试跳过，或者对某些预期失败的case标记成失败
* 支持重复执行失败的case
* 支持运行由nose, unittest编写的测试case
* 具有很多第三方插件，并且可以自定义扩展
* 方便持续集成工具集成

[Home Page](http://pytest.org)

## 安装

```bash
pip install -U pytest # 通过pip安装
py.test --version  # 验证版本
py.test --help  # 帮助信息
```

## 样例

1. 创建一个test开头的文件
    ```python
    #coding=utf-8

    # 功能
    def func(x):
        return x + 1

    # =====fixtures========
    def setup_module(module):
        print ("\n")
        print ("setup_module================>在所有测试用例执行之前执行")

    def teardown_module(module):
        print ("teardown_module=============>在所有测试用例执行之后执行")

    def setup_function(function):
        print ("setup_function------>在每个测试用例执行之前执行")

    def teardown_function(function):
        print ("teardown_function--->在每个测试用例执行之后执行")

    # 测试用例
    def test_answer():
        assert func(3) == 5
    ```
2. 创建执行文件
    ```python
    if __name__ == '__main__':
    pytest.main("-q test_sample.py")  # main默认是当前目录下所有符合条件的文件,也可以加入执行参数 路径 文件名
    ```
3. 执行用例:
    * 在文件所在目录,执行py.test
    * 执行执行文件

## 用例规范

* 测试文件以test_开头（以_test结尾也可以）
* 测试类以Test开头，并且不能带有 __init__ 方法
* 测试函数以test_开头
* 断言使用基本的assert即可

## 执行用例

```dos
py.test               # run all tests below current dir
py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test -k stringexpr # only run tests with names that match the
                      # the "string expression", e.g. "MyClass and not method"
                      # will select TestMyClass.test_something
                      # but not TestMyClass.test_method_simple
py.test test_mod.py::test_func # only run tests that match the "node ID",
			                   # e.g "test_mod.py::test_func" will select
                               # only test_func in test_mod.p
```

## 测试报告

* 生成HTML格式报告(需要pytest-html)：
    ```dos
    py.test --html=HtmlTestReport/report.html
    ```

* 生成XML格式的报告：
    ```dos
    py.test --junitxml=HtmlTestReport/report.xml
    ```
* 生成测试结果的url：
    ```python
    py.test test_class.py  --pastebin=all  # 全部
    py.test test_class.py  --pastebin=failed  # 只有失败
    ```

## 测试函数

```python
#coding=utf-8
import pytest

# 功能函数
def multiply(a,b):
    return a * b

# =====fixtures========
def setup_module(module):
    print ("\n")
    print ("setup_module================>")

def teardown_module(module):
    print ("teardown_module=============>")

def setup_function(function):
    print ("setup_function------>")

def teardown_function(function):
    print ("teardown_function--->")

# =====测试用例========
def test_numbers_3_4():
    print 'test_numbers_3_4'
    assert multiply(3,4) == 12 


def test_strings_a_3():
    print 'test_strings_a_3'
    assert multiply('a',3) == 'aaa' 

if __name__ == '__main__':
    pytest.main("-s test_fixtures.py")
```

## 测试类

```python
#coding=utf-8
import pytest

# 功能函数
def multiply(a,b):
    return a * b

class TestUM:

    # =====fixtures========

    def setup(self):
        print ("setup----->在每个测试方法开始执行")

    def teardown(self):
        print ("teardown-->在每个测试方法结束执行")

    def setup_class(cls):
        print ("setup_class=========>当前测试类开始执行")

    def teardown_class(cls):
        print ("teardown_class=========>当前测试类结束执行")

    def setup_method(self, method):
        print ("setup_method----->> 在每个测试方法开始执行，与setup级别相同")

    def teardown_method(self, method):
        print ("teardown_method-->> 在每个测试方法结束执行，与treadown级别相同")

    # =====测试用例========

    def test_numbers_5_6(self):
        print 'test_numbers_5_6'
        assert multiply(5,6) == 30 

    def test_strings_b_2(self):
        print 'test_strings_b_2'
        assert multiply('b',2) == 'bb'

if __name__ == '__main__':
    pytest.main("-s test_fixtures.py")
```

## 断言

1. 比较大小与是否相等

    ```python
    #coding=utf-8
    import pytest

    # 功能
    def add(a,b):
        return a + b

    # 测试相等
    def test_add():
        assert add(3,4) == 7 

    # 测试不相等
    def test_add2():
        assert add(17,22) != 50

    # 测试大于
    def test_add3():
        assert add(17,22) <= 50

    # 测试小于
    def test_add4():
        assert add(17,22) >= 50

    if __name__ == '__main__':
        pytest.main("test_assert.py")
    ```
2. 测试包含或不包含

    ```python
    #coding=utf-8
    import pytest

    # 测试相等
    def test_in():
        a = "hello"
        b = "he"
        assert b in a 

    # 测试不相等
    def test_not_in():
        a = "hello"
        b = "hi"
        assert b not in a

    if __name__ == '__main__':
        pytest.main("test_assert2.py")
    ```

3. 测试true或false

    ```python
    #coding=utf-8
    import pytest

    #用于判断素数
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
            return True

    # 判断是否为素数
    def test_true():
        assert is_prime(13)

    # 判断是否不为素数
    def test_true():
        assert not is_prime(7)

    if __name__ == '__main__':
        pytest.main("test_assert3.py")
    ```

## 如何获取帮助信息

```dos
py.test --version # shows where pytest was imported from
py.test --fixtures # show available builtin function arguments
py.test -h | --help # show help on command line and config file options
```

## 实践

[实践](../../03.Project/Pytest/README.md)