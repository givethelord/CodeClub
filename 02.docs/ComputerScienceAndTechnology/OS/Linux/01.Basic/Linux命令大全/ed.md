# Linux ed命令
[返回Linux 命令目录](11.Linux命令大全.md)

Linux ed命令是文本编辑器，用于文本编辑。

ed是Linux中功能最简单的文本编辑程序，一次仅能编辑一行而非全屏幕方式的操作。

ed命令并不是一个常用的命令，一般使用比较多的是vi 指令。但ed文本编辑器对于编辑大文件或对于在shell脚本程序中进行文本编辑很有用。

## 语法
```bash
ed [-][-Gs][-p<字符串>][--help][--version][文件] 
```

### 参数：

* -G或--traditional 提供回兼容的功能。
* -p<字符串> 指定ed在command mode的提示字符。
* -s,-,--quiet或--silent 不执行开启文件时的检查功能。
* --help 显示帮助。
* --version 显示版本信息。

## 实例

* 以下是一个 Linux ed 完整实例解析：
    ```bash
    $ ed              <- 激活 ed 命令 
    a                 <- 告诉 ed 我要编辑新文件 
    My name is Titan. <- 输入第一行内容 
    And I love Perl very much. <- 输入第二行内容 
    .                 <- 返回 ed 的命令行状态 
    i                 <- 告诉 ed 我要在最后一行之前插入内容 
    I am 24.          <- 将“I am 24.”插入“My name is Titan.”和“And I love Perl very much.”之间 
    .                 <- 返回 ed 的命令行状态 
    c                 <- 告诉 ed 我要替换最后一行输入内容 
    I am 24 years old. <- 将“I am 24.”替换成“I am 24 years old.”（注意：这里替换的是最后输的内容） 
    .                 <- 返回 ed 的命令行状态 
    w readme.text     <- 将文件命名为“readme.text”并保存（注意：如果是编辑已经存在的文件，只需要敲入 w 即可） 
    q                 <- 完全退出 ed 编辑器 
    ```

* 这是文件的内容是：
    ```bash
    $ cat readme.text 
    My name is Titan. 
    I am 24 years old. 
    And I love Perl vrey much. 
    ```