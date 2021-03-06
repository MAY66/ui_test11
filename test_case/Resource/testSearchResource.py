import unittest
from time import sleep
from commonFile.getPicture import get_picture
from commonFile.commonlogin import user_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

#搜索资源模板名称case
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
            sleep(5)
            # 点击资源按钮
            element1 = self.browser.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/section/aside/div/div/ul/li[3]/a/img')
            self.browser.execute_script("arguments[0].click();", element1)

            # 在搜索框输入全部查询名称
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                        '//*[@id="root"]/div/div[2]/section/main/div[1]/div/span/input'))).send_keys(
                "会议室资源查询")
            # 添加断言
            resourcename_tips_tup = (By.XPATH,
                                     '//*[@id="block-list-view"]/div[1]/div/div/div/div[2]/div[1]/div[3]/div[1]/span[1]')
            tips_info = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(resourcename_tips_tup)).text
            self.assertEqual(tips_info, "会议室资源查询")

            # 清除查询框中的内容
            WebDriverWait(self.browser, 10, 0.3).until(ec.element_to_be_clickable((By.XPATH,
                        '//*[@id="root"]/div/div[2]/section/main/div[1]/div/span/span[2]'))).click()

            # 在搜索框输入部分查询名称
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                        '//*[@id="root"]/div/div[2]/section/main/div[1]/div/span/input'))).send_keys("资源")
            # 添加断言
            resourcename_tips_tup2 = (By.XPATH,
                                     '//*[@id="block-list-view"]/div[1]/div/div/div/div[2]/div[1]/div[3]/div[1]/span[1]')
            tips_info2 = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located(resourcename_tips_tup2)).text
            self.assertEqual(tips_info2, "会议室资源查询")

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
