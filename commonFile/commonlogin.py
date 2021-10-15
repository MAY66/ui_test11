# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from commonFile.getPicture import get_picture
from time import sleep

def user_login(url, username, password):
    try:
        browser = webdriver.Chrome()
        browser.get(url)
        WebDriverWait(browser, 10, 0.3).until(ec.presence_of_element_located((By.NAME, "username"))).send_keys(username)
        WebDriverWait(browser, 10, 0.3).until(ec.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        # 点击汉得平台登录按钮
        # WebDriverWait(browser, 10, 0.3).until(ec.element_to_be_clickable((By.NAME, "submit"))).click()
        # 点击虹珊瑚登录按钮
        WebDriverWait(browser, 19, 0.3).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="loginFormAccount"]/div[2]/span/button'))).click()
        return browser

    except Exception as e:
        raise e
def user_login1(url, username, password, username1, password1):
    try:
        browser = webdriver.Chrome()
        browser.get(url)
        WebDriverWait(browser, 10, 0.3).until(ec.presence_of_element_located((By.NAME, "username"))).send_keys(username)
        WebDriverWait(browser, 10, 0.3).until(ec.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        # 点击汉得平台登录按钮
        # WebDriverWait(browser, 10, 0.3).until(ec.element_to_be_clickable((By.NAME, "submit"))).click()
        # 点击虹珊瑚登录按钮
        WebDriverWait(browser, 19, 0.3).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="loginFormAccount"]/div[2]/span/button'))).click()
        browser.maximize_window()
         # 点击虹珊瑚图标
        WebDriverWait(browser, 10, 0.3).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="@@coral-bubble-wrapper"]/div/div[1]/div[1]/img'))).click()
        # 进入虹珊瑚
        sleep(5)
        browser.switch_to.frame('umi-ui-bubble')
        sleep(5)
        WebDriverWait(browser, 10, 0.3).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div.-layouts-header_header > div.-layouts-header_content > div.-layouts-header_actions > div:nth-child(3) > div > span > span.anticon.anticon-user > svg')))
        #输入虹珊瑚登录页面用户名
        WebDriverWait(browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "username"))).send_keys(
        username1)
        # 输入虹珊瑚登录页面密码
        WebDriverWait(browser, 10, 0.3).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
        password1)
        # 点击登录按钮
        WebDriverWait(browser, 10, 0.3).until(ec.element_to_be_clickable((By.XPATH,
        '//*[@id="root"]/div/div[2]/section/main/div/div/div/div/form/div[3]/div/div/div/button'))).click()
        return browser

    except Exception as e:
        raise e

