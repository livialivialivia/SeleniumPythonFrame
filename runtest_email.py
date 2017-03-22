#! /usr/bin/env python
# _*_ coding: utf-8 _*_#! /usr/bin/env python
# _*_ coding: utf-8 _*_
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#获取最新的报告文件
def new_file(test_dir):
    lists = os.listdir(test_dir)
    lists.sort(key = lambda  fn:os.path.getmtime(test_dir+'/'+fn))
    file_path = os.path.join(test_dir,lists[-1])
    return file_path

#发送邮件
def send_mail(newfile):

    f = open(newfile,'rb')
    mail_body = f.read()
    f.close()


    smtpserver = 'smtp.163.com'
    user = 'liurongo910@163.com'
    password = 'livia646588'
    sender = 'liurongo910@163.com'
    receiver=['798817612@qq.com','liu.rong@mydreamplus.com']
    subject = '自动定时发送测试报告20170321'

    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)
    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html[ "Content-Disposition" ] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)


    msg[ 'From' ] = 'liurongo910@163.com <liurongo910@163.com>'
    msg[ 'To' ] = ";".join(receiver)
    msg[ 'Subject' ] = Header(subject, 'utf-8')


    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    print '======AutoTest Start======='

    test_dir = './test_case'
    test_report_dir = './test_report'

    discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test_*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report_dir+'/'+now+'result.html'

    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream = fp,title = u'测试报告',description = '用例执行情况')
    runner.run(discover)
    fp.close()

    new_report = new_file(test_report_dir)
    send_mail(new_report)

    print '=======AutoTest Over========='