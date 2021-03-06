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
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


    # 获取当前日期和时间
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    html_report_dir = os.path.join(BASEPATH, "report")
    html_report_name = f"{now_time}_result.html"
    html_report_path = os.path.join(html_report_dir, html_report_name)
    html_report = r'D:\uitest\test_case\report' + now_time + 'result.html'
    fp = open(html_report_path, 'wb+')

    # 调用HTMLTestRunner，运行测试用例
    runner = HTMLTestRunner(stream=fp,
                            title="测试报告",
                            description="运行环境: Windows 10, Chrome浏览器")
    runner.run(suit)
    fp.close()


    # 构造邮件
    smtp_server = "smtp.163.com"
    sender = "z15291505356@163.com"
    receivers = ['z15291505356@163.com']
    password = "OXQBIWAMOOAYOHNV"

    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.runoob.com">这是一个链接</a></p>
    """
    message = MIMEMultipart()
    message['From'] = Header("ting.zhou", 'utf-8')  # 发送者
    message['To'] = Header("tester", 'utf-8')  # 接收者

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    #message.attach(MIMEText(open(html_report_path, 'rb').read(), 'plain', 'utf-8'))   #将测试报告放到正文中
    message.attach(MIMEText('测试报告见附件.', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 html_report_path 文件
    att1 = MIMEText(open(html_report_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = f'attachment; filename=report.html'
    message.attach(att1)

    # 构造附件2
    att2 = MIMEText(open(r'D:\ui_test\requiredFile\test.txt', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = f'attachment; filename="test.txt"'
    message.attach(att2)


    try:
        # for i in smtp_server:
        #     if i=="smtp.163.com":
        #         smtp_server = "smtp.163.com"
        #     elif i == "Smtphm.qiye.163.com":
        #         smtp_server = "Smtphm.qiye.163.com"
        #
        #     smtpObj = smtplib.SMTP(smtp_server, 25)
        #     smtpObj.set_debuglevel(1)
        #     smtpObj.login(sender, password)
        #     smtpObj.sendmail(sender, receivers, message.as_string())
        #     print("邮件发送成功")
        #     smtpObj.quit()
        smtpObj = smtplib.SMTP(smtp_server, 25)
        smtpObj.set_debuglevel(1)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
        smtpObj.quit()
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

