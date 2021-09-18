import unittest
from time import sleep
from selenium import webdriver
from commonFile.getPicture import get_picture
from commonFile.commonlogin import user_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import requests


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
        sleep(15)
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


    #def test_search_resource(self, child_module, page_name):
    def test_search_resource(self):
        try:
            # 点击任务按钮
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '//*[@id="root"]/div/div[2]/section/aside/div/div/ul/li[2]/a/p'))).click()

            #创建子模块
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
               '//*[@id="two-column-panel-right"]/div/div[1]/div[2]/button[1]/span'))).click()

            #输入子模块名
            #self.child_module = child_module
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '//*[@id="two-column-panel-right"]/div/div[1]/div[2]/button[1]/span'))).send_keys('test_hsh_child_module')

           #点击取消按钮
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '/html/body/div[8]/div/div[2]/div/div[2]/div[3]/button[1]/span'))).click()

           #点击确定按钮
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '//*[@id="two-column-panel-right"]/div/div[1]/div[2]/button[1]/span'))).click()

            # 输入子模块名
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '//*[@id="two-column-panel-right"]/div/div[1]/div[2]/button[1]/span'))).send_keys('test_hsh_child_module')

            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '/html/body/div[8]/div/div[2]/div/div[2]/div[3]/button[2]/span'))).click()

           #创建页面
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '//*[@id="two-column-panel-right"]/div/div[1]/div[2]/button[2]/span'))).click()

           #选择子模块
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '//*[@id="pageForm_package"]'))).click()

            #输入页面名称
            #self.page_name = page_name
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '//*[@id="pageForm_name"]'))).send_keys('test_hsh_page')


            # 至底部
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '//*[@id="two-column-panel-right"]/div/div[3]/div/div[1]/div[2]/span[2]/img'))).click()

            # 复制
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                 '//*[@id="two-column-panel-right"]/div/div[3]/div/div[1]/div[2]/span[3]/span/svg'))).click()

            #删除
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '//*[@id="two-column-panel-right"]/div/div[3]/div/div[1]/div[2]/span[1]/img'))).click()
            #取消删除
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '/html/body/div[4]/div/div/div/div[2]/div/div[2]/button[1]/span'))).click()
            #确定删除
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '//*[@id="two-column-panel-right"]/div/div[3]/div/div[1]/div[2]/span[1]/img'))).click()
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '/html/body/div[4]/div/div/div/div[2]/div/div[2]/button[2]/span'))).click()


        except Exception as e:
            get_picture(self.browser)
            raise e

    def tearDown(self):
        self.browser.find_element_by_css_selector(
            '#root > div > div.-layouts-header_header > div.-layouts-header_content > div.-layouts-header_actions > div:nth-child(3) > div > span > span.anticon.anticon-user > svg').click()
        self.browser.find_element_by_xpath(
            '/html/body/div[3]/div/div/div/div[2]/div[2]').click()
        self.browser.quit()

if  __name__ == "__main__":
    #test1 = TestDemo()
    #test1.test_search_resource('test_hsh_child_module', 'test_hsh_page')
    TestDemo().test_search_resource()
