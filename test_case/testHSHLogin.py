import unittest
from selenium import webdriver
from commonFile.getPicture import get_picture
from commonFile.commonlogin import user_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class Login(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_hsh_UserLogIn(self):
        try:
            user_login('http://localhost:8000/', 'admin', 'Admin@123!')
            # 点击虹珊瑚图标
            # self.browser.implicitly_wait(5)
            # self.browser.find_element_by_xpath('//*[@id="@@coral-bubble-wrapper"]/div/div[1]/div[1]/img').click()
            # sleep(5)
            # # 登录虹珊瑚
            # self.browser.switch_to.frame('umi-ui-bubble')
            # # 点击未登录按钮
            # self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[3]/div/span/span[2]').click()
            # sleep(5)
            # WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "username"))).send_keys(
            #     "31199")
            # WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
            #    "Zm402402")
            # WebDriverWait(self.browser, 10, 0.3).until(
            #     ec.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/section/main/div/div/div/div/form/div[3]/div/div/div/button'))).click()
        except Exception as e:
            get_picture(self.browser)
            raise e

    def tearDown(self):
        self.browser.quit()
