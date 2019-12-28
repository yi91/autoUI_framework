# coding:utf-8

from appium import webdriver
import unittest


class SearchTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {'automationName': 'UiAutomator2',
                        'deviceName': '127.0.0.1:21503',
                        'platformName': 'Android',
                        'platformVersion': '5.1.1',
                        'noReset': True,
                        "appPackage": "com.cnblogs.xamarinandroid",
                        "appActivity": "md5229da715b9c96f11b174fd813ff81663.SplashScreenActivity"
                        }
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver = webdriver.Remote(desired_capabilities=desired_caps)
        self.driver.implicitly_wait(20)

    def test_case(self):
        driver = self.driver
        # 点击搜索按钮
        driver.find_element_by_accessibility_id("搜索").click()

        # 搜索框
        search_src_text = driver.find_element_by_id("com.cnblogs.xamarinandroid:id/search_src_text")
        search_src_text.click()

        # 输入搜索关键字“appium”
        driver.keyevent(29)  # a
        driver.keyevent(44)  # p
        driver.keyevent(44)  # p
        driver.keyevent(37)  # i
        driver.keyevent(49)  # u
        driver.keyevent(41)  # m

        # 回车搜索
        driver.keyevent(66)
        driver.keyevent(66)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
