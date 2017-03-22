#! /usr/bin/env python
# _*_ coding: utf-8 _*_

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header(u'自动化测试报告','utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("liurongo910@163.com",'livia646588')
    smtp.sendmail('liurongo910@163.com','798817612@qq.com',msg.as_string())
    smtp.quit()
    print "email has send out!"

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key = lambda fn:os.path.getmtime(testreport+'/'+fn))
    file_new = os.path.join(testreport,lists[-1])
    print file_new
    return file_new

if __name__ == '__main__':
    test_dir = './test_case'
    test_report = './test_report'

    discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test_*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream = fp, title = u'测试报告', description = u'用例执行情况')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)

    print '=======AutoTest Over========='
