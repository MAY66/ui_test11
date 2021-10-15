import unittest
from time import sleep
from commonFile.getPicture import get_picture
from commonFile.commonlogin import user_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

#创建子模块case
class TestDemo(unittest.TestCase):
    def setUp(self):
        sleep(5)
        # 登录Hzero
        self.browser = user_login('http://localhost:8000/', 'admin', 'Admin@123!','31199','Zm402402')

    def test_search_resource(self):
        try:
            # 点击任务按钮
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[2]/section/aside/div/div/ul/li[2]/a/p'))).click()
            #创建子模块
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
               '//*[@id="two-column-panel-right"]/div/div[1]/div[2]/button[1]/span'))).click()
            #输入子模块名
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '//*[@id="two-column-panel-right"]/div/div[1]/div[2]/button[1]/span'))).send_keys('test_hsh_child_module')
           #点击取消按钮
            WebDriverWait(self.browser, 10, 0.3).until(ec.presence_of_element_located((By.XPATH,
                '/html/body/div[8]/div/div[2]/div/div[2]/div[3]/button[1]/span'))).click()
            #添加断言

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
        # 退出虹珊瑚登录
        WebDriverWait(self.browser, 10, 0.3).until(ec.element_to_be_clickable((By.XPATH,
               '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div/div'))).click()
        WebDriverWait(self.browser, 10, 0.3).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                'body > div:nth-child(8) > div > div > div > div:nth-child(2) > div.-layouts-header_icon-wrapper > img'))).click()
        # 关闭浏览器
        self.browser.quit()


