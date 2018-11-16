# Selenium2Library元素定位方法


Strategy |Example |Description
---------|--------|-------------------
identifier      |Click Element  identifier=my_element           |Matches by @id or @name attribute
id              |Click Element  id=my_element                   |Matches by @id attribute
name            |Click Element  name=my_element                 |Matches by @name attribute
[xpath](#xpath) |Click Element   xpath=//div[@id='my_element']  |Matches with arbitrary XPath expression
dom             |Click Element  dom=document.images[56]         |Matches with arbitrary DOM express
link            |Click Element  link=My Link                    |Matches anchor elements by their link text
partial link    |Click Element  partial link=y Lin              |Matches anchor elements by their partial link text
[css](#css)     |Click Element  css=div.my_class                |Matches by CSS selector
jquery          |Click Element  jquery=div.my_class             |Matches by jQuery/sizzle selector
sizzle          |Click Element  sizzle=div.my_class             |Matches by jQuery/sizzle selector
tag             |Click Element  tag=div                         |Matches by HTML tag name
default*        |Click Link     default=page?a=b                |Matches key attributes with value after first '='


## xpath

1. xpath的绝对路径：
    ```
    xpath = /html/body/div[1]/div[4]/div[2]/div/form/span[1]/input
    ```

2. xpath的相对路径

    * 元素本身
        ```
        Xpath = //*[@id='kw1']
        //表示某个层级下，*表示某个标签名。@id=kw1 表示这个元素有个 id 等于 kw1 。
        ```

    * 找上级
        ```
        xpath = //span[@class='bg s_ipt_w']/input
        如果爸爸没有唯一的属性，可以找爷爷：
        xpath = //form[@id='form1']/span/input
        ```
    
    * 布尔值写法
        ```
        Xpath = //input[@id='kw1' and @name='wd']
        Xpath = //input[@id='kw1' or @name='wd']
        ```

## css

* 通过class属性定位：
    ```
    css=.s_ipt
    点号（.）表示通过 class 属性来定位元素。
    ```

* 通过id：
    ```
    css=#kw
    井号（#）表示通过 id 属性来定位元素。
    ``` 

* 通过标签名定位：
    ```
    css=input
    ```

* 通过父子关系定位：
    ```
    css=span>input
    上面的写法表示有父亲元素，它的标签名叫 span，查找它的所有标签名叫 input 的子元素。
    ```

* 通过属性定位：
    ```
    css=input[autocomplete='off']
    ```

* 组合定位：
    ```
    css=span.bg s_ipt_wr>input.s_ipt
    有一个父元素，它的标签名叫 span，它有一个 class 属性值叫 bg s_ipt_wr，它有一个子元素，标签名
    叫 input，并且这个子元素的 class 属性值叫 s_ipt
    ```