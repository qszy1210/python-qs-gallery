#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
#from email.mime.text import MIMEText 版本不同, 需要注意
from email.MIMEText import MIMEText
from email.header import Header

mail_host = 'smtp.163.com'
# mail_host = 'localhost'
mail_username = 'asdfqs'
mail_password = 'YIKFSBCPTNUJJUXB'

sender = 'asdfqs@163.com'
receiver = ['asdfqs@163.com']

message_text = '如果收到这封邮件, 说明我三个月没有联系我媳妇了~\
    可以说什么都没有留给我媳妇, 不过总有些惊喜\
    可以查看下同方全球人寿保险公司, 你老公有投保的保险哦~\
    看下说不定有小惊喜.'

message = MIMEText(message_text, 'plain', 'utf-8')
message['From'] = Header('你亲爱的老公', 'utf-8')
message['To'] = Header('asdfqs', 'utf-8')

subject = '来自老公的重要提醒'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()

    smtpObj.connect(mail_host, 25)
    # smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(mail_username, mail_password)
    smtpObj.sendmail(sender, receiver, message.as_string())
    print 'success'
except smtplib.SMTPException, e:
    print 'Error'
    print e