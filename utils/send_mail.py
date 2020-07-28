#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import smtplib
from config import CF
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart


def get_new_report():
    """获取最新的报告"""
    report_file = os.path.join(CF.BASE_DIR, 'report', 'report.html')
    with open(report_file, encoding='utf-8') as f:
        return f.read()


def _format_addr(s):
    """格式化邮件地址"""
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_report_mail():
    """发送最新的测试报告"""
    # email地址和口令：
    user = CF.EMAIL_INFO['username']
    pwd = CF.EMAIL_INFO['password']
    # 收件人地址
    to_addr = CF.ADDRESSEE
    # SMTP服务器地址
    smtp_server = CF.EMAIL_INFO['smtp_host']
    smtp_port = CF.EMAIL_INFO['smtp_port']
    try:
        # 初始化邮件对象
        msg = MIMEMultipart()
        msg['From'] = _format_addr("selenium爱好者<%s>" % user)
        msg['To'] = _format_addr('管理员 <%s>' % ','.join(to_addr))
        msg['Subject'] = Header("unittest演示测试最新的测试报告", 'utf-8').encode()

        # 发送HTML文件
        msg.attach(MIMEText(get_new_report(), 'html', 'utf-8'))

        # 发件人邮箱中的SMTP服务器，端口
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            # 括号中对应的是发件人邮箱账号、邮箱密码
            server.login(user, pwd)
            # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件内容
            server.sendmail(user, to_addr, msg.as_string())
        print("测试结果邮件发送成功！")
    except smtplib.SMTPException as e:
        print(u"Error: 无法发送邮件", format(e))


if __name__ == '__main__':
    print(get_new_report())
    send_report_mail()
