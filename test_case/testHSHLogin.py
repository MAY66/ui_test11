import unittest
from selenium import webdriver
from commonFile.getPicture import get_picture
from commonFile.commonlogin import user_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

#登录case
class Login(unittest.TestCase):

    def setUp(self):
        print('测试开始')

    def test_g_login_by_correct_username_and_password(self):
        self.browser = webdriver.Chrome()
        # 登录Hzero
        self.browser = user_login('http://localhost:8000/', 'admin', 'Admin@123!')
        self.browser.maximize_window()
        # 点击虹珊瑚图标
        sleep(5)
        self.browser.find_element_by_xpath('//*[@id="@@coral-bubble-wrapper"]/div/div[1]/div[1]/img').click()
        sleep(5)
        # 进入虹珊瑚
        self.browser.switch_to.frame('umi-ui-bubble')
        sleep(5)
        # self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div/span/span[1]/svg').click()
        self.browser.find_element_by_css_selector(
            '#root > div > div.-layouts-header_header > div.-layouts-header_content > div.-layouts-header_actions > div:nth-child(3) > div > span > span.anticon.anticon-user > svg').click()

        sleep(5)
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "username"))).send_keys(
            "31199")
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
            "Zm402402")
        WebDriverWait(self.browser, 10, 0.3).until(
            ec.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/section/main/div/div/div/div/form/div[3]/div/div/div/button'))).click()

        # 断言：通过登录页面“请输入密码”进行断言，如果登录失败，则页面不会进行跳转，页面仍在登录页面
        text_tup = (By.XPATH, '//*[@id="root"]/div/div[2]/section/main/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div')
        text_info = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(text_tup)).text
        self.assertEqual(text_info, "请输入密码")

        # 退出虹珊瑚登录
        WebDriverWait(self.browser, 10, 0.3).until(ec.element_to_be_clickable((By.XPATH,
             '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div/div/span[3]/svg/path'))).click()

        WebDriverWait(self.browser, 10, 0.3).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
            'body > div:nth-child(8) > div > div > div > div:nth-child(2) > div.-layouts-header_icon-wrapper > img'))).click()
        # 关闭浏览器
        self.browser.quit()

    def test_a_login_by_errored_username(self):
        self.browser = webdriver.Chrome()
        # 登录Hzero
        self.browser = user_login('http://localhost:8000/', 'admin', 'Admin@123!')
        self.browser.maximize_window()
        # 点击虹珊瑚图标
        sleep(5)
        self.browser.find_element_by_xpath('//*[@id="@@coral-bubble-wrapper"]/div/div[1]/div[1]/img').click()
        sleep(5)
        # 进入虹珊瑚
        self.browser.switch_to.frame('umi-ui-bubble')
        sleep(5)
        # self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div/span/span[1]/svg').click()
        self.browser.find_element_by_css_selector(
            '#root > div > div.-layouts-header_header > div.-layouts-header_content > div.-layouts-header_actions > div:nth-child(3) > div > span > span.anticon.anticon-user > svg').click()
        sleep(5)
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "username"))).send_keys(
            "311")
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
            "Zm402402")
        WebDriverWait(self.browser, 10, 0.3).until(
            ec.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/section/main/div/div/div/div/form/div[3]/div/div/div/button'))).click()

        # 断言：通过登录页面“请输入密码”进行断言，如果登录失败，则页面不会进行跳转，页面仍在登录页面
        password_tup = (By.ID,'password')
        password_info = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(password_tup)).text
        self.assertEqual(password_info, "请输入密码")


    def test_b_login_by_errored_password(self):
        self.browser = webdriver.Chrome()
        # 登录Hzero
        self.browser = user_login('http://localhost:8000/', 'admin', 'Admin@123!')
        self.browser.maximize_window()
        # 点击虹珊瑚图标
        sleep(5)
        self.browser.find_element_by_xpath('//*[@id="@@coral-bubble-wrapper"]/div/div[1]/div[1]/img').click()
        sleep(5)
        # 进入虹珊瑚
        self.browser.switch_to.frame('umi-ui-bubble')
        sleep(5)
        # self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div/span/span[1]/svg').click()
        self.browser.find_element_by_css_selector(
            '#root > div > div.-layouts-header_header > div.-layouts-header_content > div.-layouts-header_actions > div:nth-child(3) > div > span > span.anticon.anticon-user > svg').click()

        sleep(5)
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "username"))).send_keys(
            "31199")
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
            "Zm4024")
        WebDriverWait(self.browser, 10, 0.3).until(
            ec.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/section/main/div/div/div/div/form/div[3]/div/div/div/button'))).click()

        # 断言：通过登录页面“请输入密码”进行断言，如果登录失败，则页面不会进行跳转，页面仍在登录页面
        password_tup = (By.ID, 'password')
        password_info = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(password_tup)).text
        self.assertEqual(password_info, "请输入密码")

    def test_c_login_by_errored_username_and_password(self):
        self.browser = webdriver.Chrome()
        # 登录Hzero
        self.browser = user_login('http://localhost:8000/', 'admin', 'Admin@123!')
        self.browser.maximize_window()
        # 点击虹珊瑚图标
        sleep(5)
        self.browser.find_element_by_xpath('//*[@id="@@coral-bubble-wrapper"]/div/div[1]/div[1]/img').click()
        sleep(5)
        # 进入虹珊瑚
        self.browser.switch_to.frame('umi-ui-bubble')
        sleep(5)
        # self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div/span/span[1]/svg').click()
        self.browser.find_element_by_css_selector(
            '#root > div > div.-layouts-header_header > div.-layouts-header_content > div.-layouts-header_actions > div:nth-child(3) > div > span > span.anticon.anticon-user > svg').click()

        sleep(5)
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "username"))).send_keys(
            "311")
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
            "Zm4024")
        WebDriverWait(self.browser, 10, 0.3).until(
            ec.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/section/main/div/div/div/div/form/div[3]/div/div/div/button'))).click()

        # 断言：通过登录页面“请输入密码”进行断言，如果登录失败，则页面不会进行跳转，页面仍在登录页面
        password_tup = (By.ID, 'password')
        password_info = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(password_tup)).text
        self.assertEqual(password_info, "请输入密码")

    def test_d_login_by_username_is_null(self):
        self.browser = webdriver.Chrome()
        # 登录Hzero
        self.browser = user_login('http://localhost:8000/', 'admin', 'Admin@123!')
        self.browser.maximize_window()
        # 点击虹珊瑚图标
        sleep(5)
        self.browser.find_element_by_xpath('//*[@id="@@coral-bubble-wrapper"]/div/div[1]/div[1]/img').click()
        sleep(5)
        # 进入虹珊瑚
        self.browser.switch_to.frame('umi-ui-bubble')
        sleep(5)
        # self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div/span/span[1]/svg').click()
        self.browser.find_element_by_css_selector(
            '#root > div > div.-layouts-header_header > div.-layouts-header_content > div.-layouts-header_actions > div:nth-child(3) > div > span > span.anticon.anticon-user > svg').click()

        sleep(5)
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "username"))).send_keys(
            "")
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
            "Zm4024")
        WebDriverWait(self.browser, 10, 0.3).until(
            ec.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/section/main/div/div/div/div/form/div[3]/div/div/div/button'))).click()

        # 断言：通过登录页面“请输入密码”进行断言，如果登录失败，则页面不会进行跳转，页面仍在登录页面
        password_tup = (By.ID, 'password')
        password_info = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(password_tup)).text
        self.assertEqual(password_info, "请输入密码")

    def test_e_login_by_password_is_null(self):
        self.browser = webdriver.Chrome()
        # 登录Hzero
        self.browser = user_login('http://localhost:8000/', 'admin', 'Admin@123!')
        self.browser.maximize_window()
        # 点击虹珊瑚图标
        sleep(5)
        self.browser.find_element_by_xpath('//*[@id="@@coral-bubble-wrapper"]/div/div[1]/div[1]/img').click()
        sleep(5)
        # 进入虹珊瑚
        self.browser.switch_to.frame('umi-ui-bubble')
        sleep(5)
        # self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div/span/span[1]/svg').click()
        self.browser.find_element_by_css_selector(
            '#root > div > div.-layouts-header_header > div.-layouts-header_content > div.-layouts-header_actions > div:nth-child(3) > div > span > span.anticon.anticon-user > svg').click()

        sleep(5)
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "username"))).send_keys(
            "31199")
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
            "")
        WebDriverWait(self.browser, 10, 0.3).until(
            ec.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/section/main/div/div/div/div/form/div[3]/div/div/div/button'))).click()

        # 断言：通过登录页面“请输入密码”进行断言，如果登录失败，则页面不会进行跳转，页面仍在登录页面
        password_tup = (By.ID, 'password')
        password_info = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(password_tup)).text
        self.assertEqual(password_info, "请输入密码")

    def test_f_login_by_username_and_password_is_null(self):
        self.browser = webdriver.Chrome()
        # 登录Hzero
        self.browser = user_login('http://localhost:8000/', 'admin', 'Admin@123!')
        self.browser.maximize_window()
        # 点击虹珊瑚图标
        sleep(5)
        self.browser.find_element_by_xpath('//*[@id="@@coral-bubble-wrapper"]/div/div[1]/div[1]/img').click()
        sleep(5)
        # 进入虹珊瑚
        self.browser.switch_to.frame('umi-ui-bubble')
        sleep(5)
        # self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div/span/span[1]/svg').click()
        self.browser.find_element_by_css_selector(
            '#root > div > div.-layouts-header_header > div.-layouts-header_content > div.-layouts-header_actions > div:nth-child(3) > div > span > span.anticon.anticon-user > svg').click()

        sleep(5)
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "username"))).send_keys(
            "")
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
            "")
        WebDriverWait(self.browser, 10, 0.3).until(
            ec.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/section/main/div/div/div/div/form/div[3]/div/div/div/button'))).click()

        # 断言：通过登录页面“请输入密码”进行断言，如果登录失败，则页面不会进行跳转，页面仍在登录页面
        password_tup = (By.ID, 'password')
        password_info = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(password_tup)).text
        self.assertEqual(password_info, "请输入密码")


    def tearDown(self):
        print('测试结束')
