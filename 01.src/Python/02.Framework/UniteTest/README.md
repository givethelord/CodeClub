# Unittest

　　unittest是xUnit系列框架中的一员.

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

## unittest流程上

写好TestCase----->创建TestSuite----->由TestLoader加载TestCase到TestSuite----->TextTestRunner来运行TestSuite----->运行的结果保存在TextTestResult中

## 执行测试用例方法

1. 通过unittest.main()来启动所需测试的测试模块:只会执行当前文件定义或者引入模块的测试用例，加载到testsuite里面的也会去执行
2. 添加到testsuite集合中再加载所有的被测试对象，而testsuit里存放的就是所需测试的用例
3. 通过defaultTestLoader.discover查找指定目录所有用例,放入run执行

## 用例执行的顺序

unittest 框架默认根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0~9，A~Z,a~z

如果要让某个测试用例先执行，不能使用默认的main()方法，需要通过TestSuite类的addTest()方法按照一定的顺序来加载

## unittest实例

[UnitTest实战](../../03.Project/UnitTest/README.md)