# coding=utf-8

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage


class BaiduSearch(BrowserEngine):

    # 这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里
    def test_baidu_search(self):
        """
        测试搜索内容不为空
        """
        homepage = HomePage(self.driver)
        # 调用页面对象中的方法
        homepage.baidu_search('selenium')
        try:
            # 调用页面对象继承基类中的获取页面标题方法
            self.assertIn('selenium', homepage.search_success())
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))
        # 调用基类截图方法
        homepage.get_windows_img('test_baidu_search')

    def btest_baidu_search2(self):
        """
        测试搜索内容为空
        """
        homepage = HomePage(self.driver)
        # 调用页面对象中的方法
        homepage.baidu_search('')
        try:
            # 调用页面对象继承基类中的获取页面标题方法
            self.assertIn('百度一下', homepage.search_success())
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))
        # 调用基类截图方法
        homepage.get_windows_img('test_baidu_search')

    def atest_baidu_news(self):
        """ 测试打开百度新闻 """
        homepage = HomePage(self.driver)
        homepage.baidu_news()  # 调用页面对象中的方法
        homepage.get_windows_img('test_search2')  # 调用基类截图方法


if __name__ == '__main__':
    unittest.main()
