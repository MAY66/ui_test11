import unittest
from time import sleep
from commonFile.getPicture import get_picture
from commonFile.commonlogin import user_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

#个人中心case
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

    def test_check_personal_info(self):
        try:
            sleep(10)
            # 点击资源按钮
            element1 = self.browser.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/section/aside/div/div/ul/li[3]/a/img')
            self.browser.execute_script("arguments[0].click();", element1)

            # 点击个人中心按钮
            WebDriverWait(self.browser, 10, 0.3).until(ec.element_to_be_clickable((By.XPATH,
                    '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div/div/span[2]'))).click()

            WebDriverWait(self.browser, 10, 0.3).until(ec.element_to_be_clickable((By.XPATH,
                    '/html/body/div[3]/div/div/div/div[1]/div[1]/img'))).click()

            # 断言名字是否正确
            name_tup = (By.XPATH, '//*[@id="root"]/div/div[2]/section/main/div/div/div/div/div[1]/p[1]')
            name_info = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(name_tup)).text
            self.assertEqual(name_info, "周婷")

            # 断言公司是否正确
            company_tup = (By.XPATH, '//*[@id="root"]/div/div[2]/section/main/div/div/div/div/div[1]/p[2]/span[2]')
            company_info = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(company_tup)).text
            self.assertEqual(company_info, "上海汉得信息技术股份有限公司")

            # 断言默认租户是否正确
            user_tup = (By.XPATH,
                        '//*[@id="root"]/div/div[2]/section/main/div/div/div/div/div[2]/section[1]/main/div/div[3]/div/div[2]')
            user_info = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(user_tup)).text
            self.assertEqual(user_info, "汉得")

            # 断言默认角色是否正确
            user_role_tup = (By.XPATH,
                             '//*[@id="root"]/div/div[2]/section/main/div/div/div/div/div[2]/section[1]/main/div/div[5]/div/div[2]')
            user_role_info = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(user_role_tup)).text
            self.assertEqual(user_role_info, "汉得角色")


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
