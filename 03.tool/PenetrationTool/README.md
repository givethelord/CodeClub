# 渗透工具

* 1.Web渗透
    * 1.PentestDB

        * [官网](https://www.ultraedit.com/)
        * [文档](https://bbs.ichunqiu.com/thread-9519-1-1.html)

        > 提供轻量级的易扩展的工具,可以快速编写exploit、添加漏洞验证/扫描规则、添加指纹规则、爆破规则

* 2.Metasploit 渗透测试环境
    * [官网](https://www.metasploit.com/)
    > 　　Metasploit Framework是一个编写、测试和使用exploit代码的完善环境。
      　　这个环境为渗透测试、shellcode编写和漏洞研究 提供了一个可靠的平台，这个框架主要是由面向对象的Perl编程语言编写的，并带有由C语言，汇编程序和Python编写的可选组件。
      　　Metasploit Framework 作为一个缓冲区溢出测试使用的辅助工具，也可以说是一个漏洞利用和测试平台。它集成了各平台上常见的溢出漏洞和流行的shellcode，并且不断更新，使得缓冲区溢出测试变得方便和简单。（PS：缓冲区溢出测试下次讲解）
       　　使用Metasploit安全测试工具在渗透测试中可以做很多事情，你可以保存你的操作日志、甚至定义每个有效负载在运行完成之后是 如何将其自身清除的。
         　值得一提的是这个强大的工具是免费的，它的开发团队由两个全职成员和少数兼职的投稿者组 成，Metasploit Framework由最初的1.0版发展到现在的3.0版的漏洞自动化探测，成绩骄人，精神可嘉！


* 3.Nmap 网络安全审计工具
    * [官网](https://nmap.org/)
    > 　　nmap是一个网络连接端扫描软件，用来扫描网上电脑开放的网络连接端。确定哪服务运行在那些连接端，并且推断哪个操作系统计算机运行（这是亦称 fingerprinting）。
        它是网络管理员必用的软件之一，以及用以评估网络系统保安。
      　　正如大多数工具被用于网络安全的工具，nmap 也是不少黑客及骇客（又称脚本小孩）爱用的工具 。
     　　系统管理员可以利用nmap来探测工作环境中未经批准使用的服务器，但是黑客会利用nmap来搜集目标电脑的网络设定，从而计划攻击的方法。
    　　Nmap 常被跟评估系统漏洞软件Nessus 混为一谈。Nmap 以隐秘的手法，避开闯入检测系统的监视，并尽可能不影响目标系统的日常操作。
    　　Nmap 在黑客帝国(The Matrix)中，连同SSH1的32位元循环冗余校验漏洞，被崔妮蒂用以入侵发电站的能源管理系统。

![](http://p3.pstatp.com/large/pgc-image/15227433917811eba4d042f)


* 4.Hashcat 高级密码恢复工具
    * [官网](https://hashcat.net/hashcat/)
    > 　　Hashcat 的 oclHashcat 是一个用来破解哈希值的工具，支持 MD5 和 SHA1。
     　　oclHashcat 是世界上最快，最先进的，基于 GPGPU 的密码恢复工具，支持 5 种独特攻击模式，超过 170 个高优化哈希算法。
     　　oclHashcat 当前支持 AMD (OpenCL) 和 Nvidia (CUDA)    图形处理器，支持 GNU/Linux 和 Windows 7/8/10 平台。

![](http://p3.pstatp.com/large/pgc-image/1522743391838afbb01b94e)


* 5.Maltego 互联网情报局和工具
    * [官网](https://www.paterva.com/web7/buy/maltego-clients/maltego-ce.php)
    > 　　有时候你可曾想过，从一个Email，或者Twitter，或是网站，甚至姓名等等，能找到一个人千丝万缕的联系，并把这些联系整合，利用起来？
      　　 Maltego就是这样一款优秀而强大的工具。Maltego允许从服务器中更新，整合数据，并允许用户很大程度上的自定义，从而实现整合出最适合用 户的“情报拓扑”。

![](http://p3.pstatp.com/large/pgc-image/1522743391778640a80e630)

* 6.Netsparker web应用安全扫描工具
    * [官网](https://www.netsparker.com/web-vulnerability-scanner/)
    > 　　Netsparker是一款综合型的web应用安全漏洞扫描工具，它分为专业版和免费版，免费版的功能也比较强大
        Netsparker与其他综合性的 web应用安全扫描工具相比的一个特点是它能够更好的检测SQL Injection和 Cross-site Scripting类型的安全漏洞。
![](http://p3.pstatp.com/large/pgc-image/15227433917977a259e7853)


* 7.W3af web应用程序攻击和检查框架
    * [官网](http://w3af.org/)
    > 　　W3af是一个Web应用程序攻击和检查框架。该项目已超过130个插件，其中检查SQL注入，跨站点脚本（XSS），本地和远程文件等。
     　　该项目的目标是要建立一个框架，以寻找和开发Web应用安全漏洞，很容易使用和扩展。
     　　功能和特点
     　　支持代理
     　　代理身份验证（基本和摘要）
     　　网站身份验证（基本和摘要）
     　　超时处理
     　　伪造用户代理
     　　新增自订标题的请求
     　　cookie处理
     　　本地缓存GET和头部
     　　本地DNS缓存
     　　保持和支持http和https连接
     　　使用多POS请求文件上传
     　　支持SSL证书
![](http://p3.pstatp.com/large/pgc-image/1522743391808d0acc03e143)


* 8.Burp Suite 攻击web 应用程序
    * [官网](https://portswigger.net/burp/)
    * [指导](https://legacy.gitbook.com/book/t0data/burpsuite/details)
    > 　　Burp Suite 是用于攻击web 应用程序的集成平台。它包含了许多工具，并为这些工具设计了许多接口，以促进加快攻击应用程序的过程。
     　　所有的工具都共享一个能处理并显示HTTP 消息，持久性，认证，代理，日志，警报的一个强大的可扩展的框架。


* 9.Sqlmap 开源的自动化SQL注入工具
    * [官网](http://sqlmap.org/)
    * [指导](https://blog.csdn.net/wn314/article/details/78872828)
    > 　　Sqlmap是开源的自动化SQL注入工具，由Python写成，具有如下特点：
      　　完全支持MySQL、Oracle、PostgreSQL、Microsoft SQL Server、Microsoft Access、IBM DB2、SQLite、Firebird、Sybase、SAP MaxDB、HSQLDB和Informix等多种数据库管理系统。
      　　完全支持布尔型盲注、时间型盲注、基于错误信息的注入、联合查询注入和堆查询注入。
      　　在数据库证书、IP地址、端口和数据库名等条件允许的情况下支持不通过SQL注入点而直接连接数据库。
      　　支持枚举用户、密码、哈希、权限、角色、数据库、数据表和列。
      　　支持自动识别密码哈希格式并通过字典破解密码哈希。
      　　支持完全地下载某个数据库中的某个表，也可以只下载某个表中的某几列，甚至只下载某一列中的部分数据，这完全取决于用户的选择。
     　　 支持在数据库管理系统中搜索指定的数据库名、表名或列名
     　　 当数据库管理系统是MySQL、PostgreSQL或Microsoft SQL Server时支持下载或上传文件。
     　　 当数据库管理系统是MySQL、PostgreSQL或Microsoft SQL Server时支持执行任意命令并回现标准输出。

