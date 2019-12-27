# coding=utf-8
from framework.base_page import BasePage


class HomePage(BasePage):
    # 主页面
    url = '/'

    # 输入框
    input_box = "id=>kw"
    # 搜索按钮
    search_submit_btn = "xpath=>//*[@id='su']"
    # 百度新闻入口
    news_link = "xpath=>//*[@id='u1']/a[@name='tj_trnews']"

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_news(self):
        self.click(self.news_link)

    # 定义本页面的搜索功能
    def baidu_search(self, context=''):
        """
        提供一个搜索方法，测试用例只需要参入不同的参数即可
        :return:
        """
        self.open(self.url)
        self.type_search(context)
        self.send_submit_btn()

    def search_success(self):
        print("当前主题："+self.get_page_title())
        return self.get_page_title()

    def baidu_news(self):
        """ 打开百度新闻 """
        self.open(self.url)
        self.click_news()

