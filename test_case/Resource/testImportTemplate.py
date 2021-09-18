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

    def test_search_resource(self):
        try:
            sleep(10)
            # 点击资源按钮
            element1 = self.browser.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/section/aside/div/div/ul/li[3]/a/img')
            self.browser.execute_script("arguments[0].click();", element1)
            sleep(10)
            #点击“本地导入”按钮
            self.browser.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/section/main/div[1]/div/button[1]/span').click()
            sleep(10)
            #点击“添加文件”按钮
            self.browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/span[3]').click()
            #选择文件
            sleep(10)
            #点击”取消“按钮
            self.browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[1]/span').click()
            sleep(10)
            #点击“确定”按钮
            self.browser.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/section/main/div[1]/div/button[1]/span').click()
            sleep(10)
            self.browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/span[3]').click()
            sleep(10)
            self.browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]').click()

        except Exception as e:
            get_picture(self.browser)
            raise e

    def tearDown(self):
        self.browser.find_element_by_css_selector(
            '#root > div > div.-layouts-header_header > div.-layouts-header_content > div.-layouts-header_actions > div:nth-child(3) > div > span > span.anticon.anticon-user > svg').click()
        self.browser.find_element_by_xpath(
            '/html/body/div[3]/div/div/div/div[2]/div[2]').click()
        self.browser.quit()

