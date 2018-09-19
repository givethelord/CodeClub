# 爬虫

## 一.爬虫是什么？
　　如果我们把互联网比作一张大的蜘蛛网，数据便是存放于蜘蛛网的各个节点，而爬虫就是一只小蜘蛛，

　　沿着网络抓取自己的猎物（数据）爬虫指的是：向网站发起请求，获取资源后分析并提取有用数据的程序；

　　从技术层面来说就是 通过程序模拟浏览器请求站点的行为，把站点返回的HTML代码/JSON数据/二进制数据（图片、视频） 爬到本地，进而提取自己需要的数据，存放起来使用；



## 二.爬虫的基本流程：

用户获取网络数据的方式：
* 方式1：浏览器提交请求--->下载网页代码--->解析成页面
* 方式2：模拟浏览器发送请求(获取网页代码)->提取有用的数据->存放于数据库或文件中

爬虫要做的就是方式2

    发送请求--->获取响应内容--->解析内容--->保存数据

1. 发起请求
    ```
    使用http库向目标站点发起请求，即发送一个Request
    Request包含：请求头、请求体等
    Request模块缺陷：不能执行JS 和CSS 代码
    ```

2. 获取响应内容
    ```
    如果服务器能正常响应，则会得到一个Response
    Response包含：html，json，图片，视频等
    ```


3. 解析内容
    ```
    解析html数据：正则表达式（RE模块），第三方解析库如Beautifulsoup，pyquery等
    解析json数据：json模块
    解析二进制数据:以wb的方式写入文件
    ```

4. 保存数据
    ```
    数据库（MySQL，Mongdb、Redis）
    文件
    ```



## 三.过程：通过http协议去请求与响应

http协议可以点击[这个](../../../../02.docs/ComputerScienceAndTechnology/Network/Protocol/HTTP/README.md)了解

Request：用户将自己的信息通过浏览器（socket client）发送给服务器（socket server）

Response：服务器接收请求，分析用户发来的请求信息，然后返回数据（返回的数据中可能包含其他链接，如：图片，js，css等）

ps：浏览器在接收Response后，会解析其内容来显示给用户，而爬虫程序在模拟浏览器发送请求然后接收Response后，是要提取其中的有用数据。



## 四.请求配置：request

1. 请求方式：

    常见的请求方式：GET / POST


2. 请求的URL

url全球统一资源定位符，用来定义互联网上一个唯一的资源 例如：一张图片、一个文件、一段视频都可以用url唯一确定
    ```
    url编码

    https://www.baidu.com/s?wd=图片

    图片会被编码（看示例代码）

    
    网页的加载过程是：

    加载一个网页，通常都是先加载document文档，

    在解析document文档的时候，遇到链接，则针对超链接发起下载图片的请求
    ```

3. 请求头

* User-agent：请求头中如果没有user-agent客户端配置，服务端可能将你当做一个非法用户host；

* cookies：cookie用来保存登录信息

**注意： 一般做爬虫都会加上请求头**

![](image/00001.png)

![](image/00002.png)

![](image/00003.png)

**请求头需要注意的参数：**

（1）Referrer：访问源至哪里来（一些大型网站，会通过Referrer 做防盗链策略；所有爬虫也要注意模拟）

（2）User-Agent:访问的浏览器（要加上否则会被当成爬虫程序）

（3）cookie：请求头注意携带

4. 请求体

如果是get方式，请求体没有内容 （get请求的请求体放在 url后面参数中，直接能看到）

如果是post方式，请求体是format data

ps：
1. 登录窗口，文件上传等，信息都会被附加到请求体内
2. 登录，输入错误的用户名密码，然后提交，就可以看到post，正确登录后页面通常会跳转，无法捕捉到post



## 五.响应:Response

1. 响应状态码
    * 200：代表成功
    * 301：代表跳转
    * 404：文件不存在
    * 403：无权限访问
    * 502：服务器错误


2. respone header

* 响应头需要注意的参数：

    * （1）Set-Cookie:BDSVRTM=0; path=/：可能有多个，是来告诉浏览器，把cookie保存下来
    * （2）Content-Location：服务端响应头中包含Location返回浏览器之后，浏览器就会重新访问另一个页面


3. preview就是网页源代码

    * JSO数据
    * 如网页html，图片
    * 二进制数据等

## 六.原则:Robots协议

Robots协议（也称为爬虫协议、机器人协议等）的全称是“网络爬虫排除标准”（Robots Exclusion Protocol），网站通过Robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取。通过几个小例子来解读一下robots.txt中的内容，robots.txt默认放置于网站的根目录小，对于一个没有robots.txt文件的网站，默认是允许所有爬虫获取其网站内容的。

![](image/00004.jpg)

我们对于robots协议的理解，如果是商业利益我们是必须要遵守robots协议内容，否则会承担相应的法律责任。当只是个人玩转网页、练习则是建议遵守，提高自己编写爬虫的友好程度。

3. 网页解析

## 七.网页解析

BeautifulSoup尝试化平淡为神奇，通过定位HTML标签来格式化和组织复杂的网络信息，用简单易用的Python对象为我们展示XML结构信息。

BeautifulSoup是解析、遍历、维护“标签树”的功能库。

1. BeautifulSoup的解析器

    |解析器|使用方法|优势|劣势|
    ------|--- |--- | ---
    |python标准库|BeautifulSoup(markup,"html.parser")|python内置标准库 执行速度适中 文档容错能力强|Python 2.7.3 or 3.2.2前的版本中文文档容错能力差|
    |lxml HTML解析器|BeautifulSoup(markup,"lxml")|速度快 文档容错能力强|需要安装C语言库|
    |lxml XML解析器|BeautifulSoup(markup,["lxml","xml"]) BeautifulSoup(markup,"xml")|速度快 唯一支持XML的解析器|需要安装C语言库|
    |html5lib|BeautifulSoup(markup,"html5lib")|最好的容错性 以浏览器的方式解析文档生成HTML5格式的文档|需要安装C语言库|

    * BeautifulSoup通过以上四种解析器来对我们获取的网页内容进行解析。使用官网的例子来看一下解析结果：
    
        ![](image/00005.jpg)
    
    * 首先获取以上的一段HTML内容，我们通过BeautifulSoup解析之后，并且输出解析后的结果来对比一下：
    
        ![](image/00006.jpg)
    
    * 通过解析的网页内容，我们就可以使用BeautifulSoup中的方法来轻而易举的获得网页中的主要信息：
    
        ![](image/00007.jpg)
    
2. 
    
## .总结

1. 总结爬虫流程：

     爬取--->解析--->存储


2. 爬虫所需工具：

     * 请求库：requests,selenium（可以驱动浏览器解析渲染CSS和JS，但有性能劣势（有用没用的网页都会加载）；）
     * 解析库：正则，beautifulsoup，pyquery
     * 存储库：文件，MySQL，Mongodb，Redis

3. 实践
    * [爬获校花网](xiaohua.py)