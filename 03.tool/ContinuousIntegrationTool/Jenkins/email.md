# 配置邮件通知

## 邮件发送配置(自带发送邮件功能)

1. 点击左边的菜单(系统管理)---系统设置---邮件通知
2. 填写系统管理员邮件地址(smtp.126.com)
3. 填写SMTP服务器(smtp.126.com)。如果是qq，需要开启smtp服务。

    邮件服务器名称	|服务器地址| 	端口号
    --------------|-----------|---------
    POP3服务器	|pop.126.com	| 110
    SMTP服务器	|smtp.126.com	| 25
    IMAP服务器	|imap.126.com	| 143

4. 勾选smtp认证,填入发送邮箱的用户名、密码和端口号。(**注意:不要勾选使用SSL协议**)
5. 勾选发送邮件测试，填入接受邮件的邮箱，进行测试。

## 安装插件

系统管理→插件管理→可选插件，搜索找到 Email Extension Plugin安装。


## 发送邮件模板配置

1. 全局配置：系统设置---Extended E-mail Notification,插件的邮件发送配置同自带的配置,还需要配置下列参数:(**注意:不要勾选使用SSL协议**)

    * Default Content Type:填入默认发送邮件内容格式(HTML)
    * Default Recipients:填入默认需要接受邮件的人
    * Reply To List:填入默认接受到邮件中可以回复的人
    * Default Subject:填入默认发送邮件的标题
    * Default Content: 填入默认发送邮件内容
    * Default Triggers:填入默认触发器的触发条件

2. 项目配置:添加构建后操作->Editable Email Notification,配置参数同上,只不过默认参数值都是读取全局的
    * 在Advanced Settings -> Triggers -> Failure - Any -> Send To 加上Recipient List