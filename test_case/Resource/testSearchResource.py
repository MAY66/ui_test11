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

    def test_search_resource(self):
        try:
            #登录Hzero
            user_login('http://localhost:8000/', 'dmin', 'Admin@123!')
            # # 点击虹珊瑚图标
            # self.browser.implicitly_wait(5)
            # # driver.find_element_by_xpath('//*[@class="sc-jrQzUz bqHIPx"]/img').click()
            # self.browser.find_element_by_xpath('//*[@id="@@coral-bubble-wrapper"]/div/div[1]/div[1]/img').click()
            # sleep(5)
            # #登录虹珊瑚
            # self.browser.switch_to.frame('umi-ui-bubble')
            # WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "username"))).send_keys(
            #     "31199")
            # WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
            #    "Zm402402")
            # WebDriverWait(self.browser, 10, 0.3).until(
            #     ec.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/section/main/div/div/div/div/form/div[3]/div/div/div/button'))).click()
            # #点击资源按钮
            # self.browser.find_element_by_xpath(
            #     '//*[@id="root"]/div/div[2]/section/aside/div/div/ul/li[3]/a/p').click()
            # # 在搜索框输入全部查询名称
            # sleep(5)
            # self.browser.find_element_by_xpath(
            #     '//*[@id="root"]/div/div[2]/section/main/div[1]/div/span/input').send_keys('会议室资源查询')
            # # 在搜索框输入部分查询名称
            # self.browser.find_element_by_xpath(
            #     '//*[@id="root"]/div/div[2]/section/main/div[1]/div/span/input').send_keys('资源')
            # # 删除搜索框的内容
            # self.browser.find_element_by_xpath(
            #     '//*[@id="root"]/div/div[2]/section/main/div[1]/div/span/span[2]/span/svg/path').click()

        except Exception as e:
            raise e

    def tearDown(self):
        self.browser.quit()


