#!/usr/bin/python
# _*_ coding: utf-8 _*_

import unittest
from selenium import webdriver
from time import sleep


class BaiDuSearch(unittest.TestCase):
    def setUp( self ):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"

    def test_baidu_search( self ):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        sleep(3)

    def tearDown( self ):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
