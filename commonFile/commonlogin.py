# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from commonFile.getPicture import get_picture

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
