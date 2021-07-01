# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from commonFile.getPicture import get_picture


# def user_login(url,username,password):
#     try:
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         driver.get(url)
#         # 设置动态等待10秒，每间隔0.3秒判断name属性为loginId的元素是否加载出来
#         WebDriverWait(driver, 10, 0.3).until(ec.presence_of_element_located((By.NAME, "username"))).send_keys(username)
#         # 设置动态等待10秒，每间隔0.3秒判断name属性为password的元素是否加载出来
#         WebDriverWait(driver, 10, 0.3).until(ec.presence_of_element_located((By.NAME, "password"))).send_keys(password)
#         # 设置动态等待10秒，每间隔0.3秒判断id属性为button_submit的元素是否加载出来
#         #WebDriverWait(driver, 10, 0.3).until(ec.element_to_be_clickable((By.NAME, "submit"))).click()
#         # 虹珊瑚登录页面提交按钮
#         WebDriverWait(driver, 10, 0.3).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="loginFormAccount"]/div[2]/span/button'))).click()
#         return driver
#     except Exception as e:
#        get_picture(driver)
#        raise e

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
       # get_picture(browser)
       raise e

