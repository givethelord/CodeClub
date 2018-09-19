# 接口测试工具

* 1.Jmeter

    * [目录](Jmeter)
    * [官网](https://jmeter.apache.org/)

　　Apache JMeter是**Apache**组织开发的基于**Java**的压力测试工具。用于对软件做**压力测试**，它最初被设计用于Web应用测试，但后来扩展到其他测试领域。 它可以用于测试静态和动态资源，例如静态文件、Java 小服务程序、CGI 脚本、Java 对象、数据库、FTP 服务器， 等等。JMeter 可以用于对服务器、网络或对象模拟巨大的负载，来自不同压力类别下测试它们的强度和分析整体性能。另外，JMeter能够对应用程序做功能/回归测试，通过创建带有断言的脚本来验证你的程序返回了你期望的结果。为了最大限度的灵活性，JMeter允许使用正则表达式创建断言。

　　Apache jmeter 可以用于对静态的和动态的资源（文件，Servlet，Perl脚本，java 对象，数据库和查询，FTP服务器等等）的性能进行测试。它可以用于对服务器、网络或对象模拟繁重的负载来测试它们的强度或分析不同压力类型下的整体性能。你可以使用它做性能的图形分析或在大并发负载测试你的服务器/脚本/对象。


* 2.Postman

    * [目录](Postman)
    * [官网](https://www.getpostman.com/)
    * [Google商城](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?utm_source=chrome-ntp-icon)

　　用户在开发或者调试网络程序或者是网页B/S模式的程序的时候是需要一些方法来跟踪网页请求的，用户可以使用一些网络的监视工具比如著名的Firebug等网页调试工具。今天给大家介绍的这款网页调试工具不仅可以调试简单的css、html、脚本等简单的网页基本信息，它还可以发送几乎所有类型的HTTP请求！Postman在发送网络HTTP请求方面可以说是Chrome插件类产品中的代表产品之一。


* 3.Wrk

    * [目录](Wrk)
    * [Github地址](https://github.com/wg/wrk )


　　基于事件机制的高性能http压力测试工具，除了能针对单个url进行测试外，最重要的就是能够构造不同的url，不同的参数进行测试。或者发送携带body的POST请求，在有些场景下不要太帅。


* 4.ab

    * [目录](ApacheBench)
    * [官网](http://httpd.apache.org/download.cgi)
    * [参数文档](http://httpd.apache.org/docs/2.0/programs/ab.html)

　　ApacheBench 是一个指令列程式，专门用来执行网站服务器的运行效能，特别是针对Apache 网站服务器。这原本是用来检测 Apache 网站服务器能够提供的效能，特别是可以看出Apache能提供每秒能送出多少网页。

　　ab工具小巧简单，上手学习较快，可以提供需要的基本性能指标，但是没有图形化结果，不能监控。因此ab工具可以用作临时紧急任务和简单测试。


* 5.SoapUI

    * [目录](SoapUI)
    * [官网](https://www.soapui.org/downloads/latest-release.html)
    * [参数文档](https://www.soapui.org/docs/preferences-and-settings.html)

　　WebService通过Http协议发送请求和接收结果时，发送的请求内容和结果内容都采用XML格式封装，并增加了一些特定的HTTP消息头，以说明HTTP消息头的内容格式，这些特定的HTTP消息头和XML内容格式就是SOAP协议。SOAP提供了标准的RPC方法来调用WebService。
