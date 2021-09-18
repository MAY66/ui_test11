import time
import unittest
import yagmail
from HTMLTestRunner import HTMLTestRunner
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


if __name__ == '__main__':
    # 定义测试用例的目录为当前目录
    BASEPATH = os.path.dirname(os.getcwd())
    test_dir = os.path.join(BASEPATH, "test_case")
    print(test_dir)
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    # 获取当前日期和时间
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    html_report_dir = os.path.join(BASEPATH, "report")
    html_report_name = f"{now_time}_result.html"
    html_report_path = os.path.join(html_report_dir, html_report_name)
    html_report = 'D:\\uitest\\test_case\\report' + now_time + 'result.html'
    fp = open(html_report_path, 'wb+')

    # 调用HTMLTestRunner，运行测试用例
    runner = HTMLTestRunner(stream=fp,
                            title="测试报告",
                            description="运行环境: Windows 10, Chrome浏览器")
    runner.run(suit)
    fp.close()

