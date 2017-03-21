#!/usr/bin/python
# _*_ coding: utf-8 _*_

import unittest
from selenium import webdriver
from time import sleep


class BaiDuSet(unittest.TestCase):
    def setUp( self ):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"

    def test_baidu_set(self):
        driver = self.driver
        driver.get((self.base_url+"/gaoji/preferences.html"))

        m = driver.find_element_by_name("NR")
        m.find_element_by_xpath("//option[@value='20']").click()
        sleep(2)

        driver.find_element_by_xpath("//input[@value='保存设置']").click()
        sleep(2)
        driver.switch_to_alert().accept()

    def tearDown( self ):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
