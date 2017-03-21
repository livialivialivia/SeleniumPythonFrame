#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import unittest,time
from HTMLTestRunner import HTMLTestRunner

test_dir = './test_case'
report_dir = './test_report'
discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test_*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    filename = report_dir +'/' + now + '_result.html'

    fp = open(filename,'wb')

    runner = HTMLTestRunner(stream = fp, title = u'百度搜索测试报告', description = u'用例执行情况:')

    runner.run(discover)
    fp.close()