# Python编码规范和覆盖率工具

## Python编码规范


Pylint 是一个 Python 代码分析工具，它分析 Python 代码中的错误，查找不符合代码风格标准（Pylint 默认使用的代码风格是 PEP 8，具体信息，请参阅参考资料）和有潜在问题的代码。目前 Pylint 的最新版本是 pylint-0.18.1。 

Pylint 是一个 Python 工具，除了平常代码分析工具的作用之外，它提供了更多的功能：如检查一行代码的长度，变量名是否符合命名标准，一个声明过的接口是否被真正实现等等。 
Pylint 的一个很大的好处是它的高可配置性，高可定制性，并且可以很容易写小插件来添加功能。 

如果运行两次 Pylint，它会同时显示出当前和上次的运行结果，从而可以看出代码质量是否得到了改进。 


## 覆盖率工具 coverage

```bash
# 安装
pip install coverage

# 想运行代码
coverage run 文件

# 生成代码覆盖率报告
coverage report -m 

# 生成html文件
coverage html
```

