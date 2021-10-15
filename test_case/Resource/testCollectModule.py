import unittest
from time import sleep
from selenium import webdriver
from commonFile.getPicture import get_picture
from commonFile.commonlogin import user_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

#收藏模板case
class TestDemo(unittest.TestCase):
    def setUp(self):
        # 登录Hzero
        self.browser = user_login('http://localhost:8000/', 'admin', 'Admin@123!')
        self.browser.maximize_window()
        # 点击虹珊瑚图标
        sleep(10)
        self.browser.find_element_by_xpath('//*[@id="@@coral-bubble-wrapper"]/div/div[1]/div[1]/img').click()
        sleep(10)
        # 进入虹珊瑚
        self.browser.switch_to.frame('umi-ui-bubble')
        sleep(10)
        # self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div/span/span[1]/svg').click()
        self.browser.find_element_by_css_selector(
            '#root > div > div.-layouts-header_header > div.-layouts-header_content > div.-layouts-header_actions > div:nth-child(3) > div > span > span.anticon.anticon-user > svg').click()

        sleep(10)
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "username"))).send_keys(
            "31199")
        WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
            "Zm402402")
        WebDriverWait(self.browser, 10, 0.3).until(ec.element_to_be_clickable((By.XPATH,
                '//*[@id="root"]/div/div[2]/section/main/div/div/div/div/form/div[3]/div/div/div/button'))).click()

    def test_add_resource_to_project(self):
        try:
            #点击资源按钮
            self.browser.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/section/aside/div/div/ul/li[3]/a/img').click()

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
            get_picture(self.browser)
            raise e

    def tearDown(self):
        # 退出虹珊瑚登录
        WebDriverWait(self.browser, 10, 0.3).until(ec.element_to_be_clickable((By.XPATH,
            '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div/div'))).click()

        WebDriverWait(self.browser, 10, 0.3).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
             'body > div:nth-child(8) > div > div > div > div:nth-child(2) > div.-layouts-header_icon-wrapper > img'))).click()
        # 关闭浏览器
        self.browser.quit()

