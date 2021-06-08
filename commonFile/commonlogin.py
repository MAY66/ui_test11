# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from commonFile.getPicture import get_picture


def user_login(url,username,password):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        # 设置动态等待10秒，每间隔0.3秒判断name属性为loginId的元素是否加载出来
        WebDriverWait(driver, 10, 0.3).until(ec.presence_of_element_located((By.NAME, "username"))).send_keys(username)
        # 设置动态等待10秒，每间隔0.3秒判断name属性为password的元素是否加载出来
        WebDriverWait(driver, 10, 0.3).until(ec.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        # 设置动态等待10秒，每间隔0.3秒判断id属性为button_submit的元素是否加载出来
        WebDriverWait(driver, 10, 0.3).until(ec.element_to_be_clickable((By.NAME, "submit"))).click()
    except Exception as e:
       get_picture(driver)
       raise e


if  __name__ == "__main__":
    user_login("https://login.hand-china.com","z15291505356","zhou123456")


