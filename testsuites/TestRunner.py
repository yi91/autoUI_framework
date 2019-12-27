# coding=utf-8
import HTMLTestRunner
import os
import unittest
import time

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '\\test_report\\'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "_report.html"
fp = open(HtmlFile, "wb")


# 构建suite
def set_suit():
    """
    set case list
    :return:
    """
    case_list = []
    with open('caselist.txt', 'r') as f:
        for value in f.readlines():
            data = str(value)
            # 过滤掉caselist文件中#注释的
            if data != '' and not data.startswith("#"):
                case_list.append(data.replace("\n", ""))
    # 定义一个new_suite
    new_suite = unittest.TestSuite()

    if len(case_list) == 0:
        print('没有用例需要测试！')
        return new_suite

    for case in case_list:
        case_name = case.split('/')[1]
        # 使用相对路径
        case_dir = case.split('/')[0]
        # discover()返回的是一个suite(case_list)，suite包含一个列表
        suite = unittest.defaultTestLoader.discover(case_dir, case_name+'.py')
        for cases in suite:
            for test_case in cases:
                new_suite.addTest(test_case)
    return new_suite


if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"某某项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(set_suit())
    fp.close()
