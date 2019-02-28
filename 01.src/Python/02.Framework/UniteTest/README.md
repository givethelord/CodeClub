# Unittest

　　unittest是xUnit系列框架中的一员.

## 样例

1. 被测文件
    ```python
    def plus_function(a, b):
        return a + b
    ```
2. 测试用例文件(默认匹配为test开头的测试文件)
    ```python
    import unittest
    from testfile import *

    class MyTest(unittest.TestCase):  # 继承unittest.TestCase为一个测试用例集合
        def tearDown(self):
            print('可选:每个测试用例执行之后做操作')

        def setUp(self):
            print('可选:每个测试用例执行之前做操作')

        @classmethod
        def tearDownClass(self):
            print('可选:必须使用 @ classmethod装饰器, 所有test运行完后运行一次')

        @classmethod
        def setUpClass(self):
            print('可选:必须使用@classmethod 装饰器,所有test运行前运行一次')

        def test_a_run(self):
            print('测试用例:test为开头的方法,使用self.assert的断言')
            self.assertEqual(plus_function(1,2), 3)

        def test_b_run(self):
            print('测试用例:test为开头的方法,使用self.assert的断言')
            self.assertNotEqual(plus_function(1,2), 3)
    ```

3. 执行用例
    ```python
    if __name__ == '__main__':
    unittest.main()#运行所有的测试用例
    ```


## unittest核心工作原理

1. test case(class继承了unittest.TestCase为一个测试集合,测试用例文件必须为test开头，如：testxxx.py)
    1. testxxx方法:单个测试用例
    2. skip装饰器
        1. unittest.skip(reason) 无条件跳过
        2. unittest.skipIf(condition,reason) 当condition为True时跳过
        3. unittest.skipUnless(condition,reason) 当condition为False时跳过
2. test suite:组织测试用例的实例，支持测试用例的添加和删除，最终将传递给  testRunner进行测试执行，TestSuite也可以嵌套TestSuite
    1. addTest() 添加单个TestCase到测试组中
    2. addTests() 将测试用例列表添加到测试组中
3. test loader:用来加载TestCase到TestSuite中,从各个地方寻找TestCase，创建它们的实例，然后add到TestSuite中，再返回一个TestSuite实例。
    1. loadTestsFromName 添加单个测试集合到测试组中 模块名.TestCase名
    2. loadTestsFromNames 添加测试集合列表到测试组中 [模块名.TestCase名,.....]
    3. loadTestsFromTestCase 添加单个测试集合到测试组中 TestCase名
4. test runner:进行测试用例执行的实例,verbosity控制输出的错误报告的详细程度，默认是 1，如果设为 0，则不输出每一用例的执行结果。如果参数为2则表示输出详细结果。
    1. run(suite)
5. test fixture:一个测试用例环境的搭建和销毁
    1. setUp:测试前准备环境的搭建
        1. setUpClass()所有测试用例前的设置工作
        2. setUp()该测试用例执行前的设置工作
    2. tearDown:测试后环境的还原
        1. tearDown()该测试用例执行后的清理工作
        2. tearDownClass()所有测试用例执行后的清洗工作

## 流程

写好TestCase----->创建TestSuite----->由TestLoader加载TestCase到TestSuite----->TextTestRunner来运行TestSuite----->运行的结果保存在TextTestResult中

## 执行测试用例方法

1. 通过unittest.main()来启动所需测试的测试模块:只会执行当前文件定义或者引入模块的测试用例，加载到testsuite里面的也会去执行
2. 添加到testsuite集合中再加载所有的被测试对象，而testsuit里存放的就是所需测试的用例
3. 通过defaultTestLoader.discover查找指定目录所有用例,放入run执行

## 用例执行的顺序

unittest 框架默认根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0~9，A~Z,a~z

如果要让某个测试用例先执行，不能使用默认的main()方法，需要通过TestSuite类的addTest()方法按照一定的顺序来加载

## 跳过

```python
import unittest
from TestContent.mathfunc import *

class test_00_00_checkskip(unittest.TestCase):
    """测试skip"""

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

if __name__ == "__main__":
    unittest.main()

```

## 断言

```python
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

```

## 参数化

```pyhton
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

```

## 实践

[实践](../../03.Project/UnitTest/README.md)