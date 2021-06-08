from datetime import datetime


# 定义获取时间戳函数
def get_shijianchuo():
    # datetime模块下，now()可以获取当前系统时间
    now_time = datetime.now()
    # 将当前系统时间格式化为一个字符串
    # 使用datetime模块下的strftime（)将系统时间格式化为字符串
    str_time = datetime.strftime(now_time, '%Y%m%d%H%M%S')
    return str_time
# 定义截图函数
def get_picture(browser):
    picture_file = "D:\\uitest\\uitest_pic" + get_shijianchuo() + ".png"
    browser.get_screenshot_as_file(picture_file)
