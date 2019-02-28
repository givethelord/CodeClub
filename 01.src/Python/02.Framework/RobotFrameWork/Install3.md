# 安装指导


## **1.需要使用到的环境和工具**

- [Python3](https://www.python.org/)
- [wxPython](https://www.wxpython.org/pages/downloads/)
  
    一个著名的Python GUI库，用于支持后面的RIDE图形化操作工具。

- [Robot framework](https://pypi.python.org/pypi/robotframework/2.8.5)
  
    Robot framework框架本身。

- [Robot framework-ride](https://github.com/HelioGuilherme66/RIDE/releases)

    Robot framework IDE 缩写为RIDE，一个拥有图形化界面的用于创建、组织、运行测试的工具。后续章节的示例操作都是基于RIDE来进行的。

- [Robot framework-selenium2library](https://pypi.python.org/pypi/robotframework-selenium2library/1.5.0)

    Robot framework版的selenium库,里面封装了核心的系统操作和需要使用到的关键字。需要：进行[浏览器驱动选择](浏览器驱动选择.md)和[下载](https://www.seleniumhq.org/download/)

- requests(Robot framework-requests库包，基于urllib编写的，采用的是Apache2 Licensed开源协议的HTTP库)
- Robot framework-requests(HTTP请求库)
- [AutoItLibrary](https://code.google.com/archive/p/robotframework-autoitlibrary/downloads)（Autoit库包，用于进行Windows GUI的自动化操作）
- [pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/)（Autoit的运行环境）
- [Autoit](https://www.autoitscript.com/site/autoit/downloads/)（对于操作系统是32位的朋友，就不需要安装autoit了。 AutoIt没有64位的版本，直接下载并安装AutoIt Full Installation可执行文件。）


## **2.安装方法**

- windows

    1) 传统方法是分别到各个网站下载相应的安装包，顺序完成安装。这边是按照python3，然后通过pip安装。
    注意完成Python安装后，需要先手动配置环境变量，默认安装路径即C:\Python37，另外需要配置上C:\Python37\Scripts。

    2) 使用pip安装
        ```dos
        pip install -U wxPython
        pip install -U robotframework
        pip install -U -r https://raw.githubusercontent.com/HelioGuilherme66/RIDE/v1.7.2/requirements.txt
        pip install -U https://github.com/HelioGuilherme66/RIDE/archive/v1.7.2.tar.gz
        pip install -U robotframework-selenium2library
        pip install -U Requests
        pip install -U RequestsLibrary
        ```

## **3.使用建议**  

* 使用pycharm+Robot Framework support plugin