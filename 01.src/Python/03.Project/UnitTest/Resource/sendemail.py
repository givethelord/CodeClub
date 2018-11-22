#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/11/22 21:20
# @Author  : Administrator
# @Site    :
# @File    : sendemail.py
# @Software: PyCharm

"""
-----------------------------------------------------
Function:通过smtp发送邮件


-----------------------------------------------------
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def sendmail(sender, receivers, subject, content, filePath):
    """通过smtp发送邮件

    :param sender: 发件人(字符串)
    :param receivers:收件人(列表)
    :param subject:标题(字符串)
    :param filePaht:发件附件(字符串)
    :return:
    """
    # 1.设置服务器所需信息
    smtp_server = "smtp.126.com"  # 使用的邮箱的smtp服务器地址，这里是126的smtp地址
    mail_user = sender  # 用户名
    mail_pass = "密码"  # 密码

    # 2.设置email信息
    message = MIMEMultipart()  # 创建一个带附件的实例

    message['From'] = sender  # 设置收件人
    message['To'] = ";".join(receivers)  # 将收件人列表以";"分隔
    message['Subject'] = Header(subject, 'utf-8')  # 设置标题
    message.attach(MIMEText(content, 'plain', 'utf-8'))  # 设置正文

    attach = MIMEText(
        open(
            filePath,
            'rb').read(),
        _subtype='html',
        _charset='utf-8')  # 读取附件
    attach["Content-Type"] = 'application/octet-stream'  # 设置类型
    attach["Content-Disposition"] = 'attachment; filename=' + \
        os.path.basename(filePath)  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    message.attach(attach)  # 带上附件

    # 3.登录并发送邮件
    try:
        smtp = smtplib.SMTP()
        # smtp.set_debuglevel(1) # 打开调试模式
        smtp.connect(smtp_server, 25)
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"
