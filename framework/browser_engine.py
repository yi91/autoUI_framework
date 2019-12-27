# -*- coding:utf-8 -*-
import configparser as ConfigParser
import os.path
from selenium import webdriver
from framework.logger import Logger
import unittest

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(unittest.TestCase):
    """
    定义一个引擎类，负责 setUp和tearDown 并提供driver
    """
    pro_dir = os.path.dirname(os.path.dirname(__file__)).replace('\\', '/')
    chrome_driver_path = pro_dir + '/tools/chromedriver.exe'

    driver = webdriver.Chrome(chrome_driver_path)
    logger.info("Starting Chrome browser.")

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        cls.driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        cls.driver.maximize_window()
        logger.info("Maximize the current window.")

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    # read the browser type from config.ini file, return the driver
