import unittest
from time import sleep
from selenium import webdriver
from commonFile.getPicture import get_picture
from commonFile.commonlogin import user_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    #输入用户名和密码进行登录
    def test_UserLogIn_by_input_username_and_password(self):
        try:
            #登录Hzero
            user_login('http://localhost:8000/', 'admin', 'Admin@123!')
            # 点击虹珊瑚图标
            self.browser.implicitly_wait(5)
            # driver.find_element_by_xpath('//*[@class="sc-jrQzUz bqHIPx"]/img').click()
            self.browser.find_element_by_xpath('//*[@id="@@coral-bubble-wrapper"]/div/div[1]/div[1]/img').click()
            sleep(5)
            #登录虹珊瑚
            self.browser.switch_to.frame('umi-ui-bubble')
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "username"))).send_keys(
                "31199")
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
               "Zm402402")
            WebDriverWait(self.browser, 10, 0.3).until(
                ec.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/section/main/div/div/div/div/form/div[3]/div/div/div/button'))).click()

    def test_add_resource_to_project(self):
            #点击资源按钮
        self.browser.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/section/aside/div/div/ul/li[3]/a/img').click()
            # 在搜索框输入全部查询名称
            # sleep(5)
            # self.browser.find_element_by_xpath(
            #     '//*[@id="root"]/div/div[2]/section/main/div[1]/div/span/input').send_keys('会议室资源查询')

            # 将”会议室资源查询“模板添加到项目中
            # 点击“添加到项目”按钮
            sleep(10)
            self.browser.find_element_by_xpath(
                '//*[@id="block-list-view"]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/button/span').click()
            # 将模板添加到项目中---校验”取消“功能是否可用
            self.browser.find_element_by_css_selector(
                'body > div:nth-child(9) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button:nth-child(1) > span').click()
            # 将模板添加到项目中---校验”确定“功能是否可用
            sleep(10)
            self.browser.find_element_by_css_selector(
                '#block-list-view > div > div > div > div:nth-child(1) > div:nth-child(2) > div.plugin-ui-blocks-ui-block-list-index_module_templateCard > div.ant-spin-nested-loading > div > div > div.plugin-ui-blocks-ui-block-list-index_module_addProject > button > span').click()
            self.browser.find_element_by_css_selector(
                'body > div:nth-child(9) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.ant-btn.ant-btn-primary > span').click()
            # 将模板添加到项目中---关闭窗口
            sleep(10)
            self.browser.find_element_by_xpath(
                '//*[@id="block-list-view"]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/button/span').click()
            self.browser.find_element_by_xpath(
                '/html/body/div[2]/div/div[2]/div/div[2]/button/span/span/svg').click()
            # 添加断言

            # 收藏”报销单详情“模板
            sleep(10)
            self.browser.find_element_by_xpath(
                '//*[@id="block-list-view"]/div/div/div/div[1]/div[3]/div[1]/div[3]/div[1]/span[2]/span/img').click()
            # 添加断言
            element_collect_template = self.browser.find_element_by_xpath(
                '//*[@id="block-list-view"]/div/div/div/div[1]/div[3]/div[1]/div[3]/div[1]/span[2]/span/img').text
            self.assertEqual(element_collect_template, "收藏成功")

            # 取消收藏”报销单详情“模块
            sleep(10)
            self.browser.find_element_by_xpath(
                '//*[@id="block-list-view"]/div/div/div/div[1]/div[4]/div[1]/div[3]/div[1]/span[2]/span/img').click()
            # 添加断言
            element_discollect_template = self.browser.find_element_by_xpath(
                '//*[@id="block-list-view"]/div/div/div/div[1]/div[3]/div[1]/div[3]/div[1]/span[2]/span/img').text
            self.assertEqual(element_discollect_template, "取消收藏成功")


        except Exception as e:
            raise e

    def tearDown(self):
        self.browser.quit()
