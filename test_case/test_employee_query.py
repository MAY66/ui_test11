from TestRunner import HTMLTestRunner
from TestRunner import SMTP
import unittest
from selenium import webdriver
from commonFile.getPicture import get_picture
from commonFile.commonlogin import user_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo(unittest.TestCase):
    """测试用例说明"""

    # 定义setUp(),实现浏览器驱动
    def setUp(self):
        # 驱动浏览器
        self.browser = webdriver.Chrome()

    # 输入“张”查询员工信息
    def test_employ_query(self):
        try:
            user_login('https://login.hand-china.com/','31199','Zm402402')
            self.browser.find_element_by_xpath('//*[@id="menucontainer"]/div[1]/div[1]/span')
            frame_name = self.find_element_by_id('container')
            self.swtich_to.frame(frame_name)
            self.find_elements_by_name('name').send_keys('张')
            self.browser.find_element_by_xpath('//*[@id="employee-filters"]/div[4]/div[3]/div/button').click()

        except Exception as e:
            get_picture(self.browser)
            raise e

    # 定义tearDown(),关闭浏览器
    def tearDown(self):
        self.browser.quit()





