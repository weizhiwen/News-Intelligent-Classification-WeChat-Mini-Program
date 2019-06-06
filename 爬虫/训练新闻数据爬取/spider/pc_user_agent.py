# 电脑端浏览器标识处理类

import json
import random


# chrome 浏览器的标识头
chrome = []
# opera 浏览器的标识头
opera = []
# firefox 浏览器的标志头
firefox = []
# ie 浏览器的标志头
ie = []
# safari 浏览器的标志头
safari = []
# 所有浏览器的标识头
all_browser = []

# json文件读取
f = open("pc_user_agent.json")
pc_user_agent = json.load(f)
browsers = pc_user_agent["browsers"]

for key, value in browsers.items():
    # all_browser 在列表中追加所有浏览器的标识头
    all_browser.extend(value)
    # 特殊浏览器只追加属于自己的那部分浏览器标识头
    if key == "chrome":
        chrome = value
    elif key == "opera":
        opera = value
    elif key == "firefox":
        firefox = value
    elif key == "internetexplorer":
        ie = value
    elif key == "safari":
        safari = value

# 得到所有浏览器的随机 User-Agent
def get_random():
    return random.choice(all_browser)

# 得到chrome浏览器的随机 User-Agent
def get_chrome_random():
    return random.choice(chrome)

# 得到opera浏览器的随机 User-Agent
def get_opera_random():
    return random.choice(opera)

# 得到firefox浏览器的随机 User-Agent
def get_firefox_random():
    return random.choice(firefox)

# 得到ie浏览器的随机 User-Agent
def get_ie_random():
    return random.choice(ie)

# 得到safari浏览器的随机 User-Agent
def get_safari_random():
    return random.choice(safari)

if __name__ == '__main__':
    # print("所有浏览器的标识头：", len(all), all)
    # print("chrome浏览器的标识头：", len(chrome), chrome)
    # print("opera浏览器的标识头：", len(opera), opera)
    # print("firefox浏览器的标识头：", len(firefox), firefox)
    # print("ie浏览器的标识头：", len(ie), ie)
    # print("safari浏览器的标识头：", len(safari), safari)
    print(get_random())

