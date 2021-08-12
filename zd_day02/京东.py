import cv2
import time
import numpy as np
from selenium import webdriver
from urllib import request
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# 打开谷歌浏览器
driver = webdriver.Chrome(options=chrome_options)

# 打开京东网址
driver.get("https://www.jd.com/")

# 窗口最大化
driver.maximize_window()

def loadpage(userid, password):
    url = "https://passport.jd.com/new/login.aspx?"
    driver.get(url)
    time.sleep(3)
    s1 = r'//div/div[@class="login-tab login-tab-r"]/a'
    userlogin = driver.find_element_by_xpath(s1)
    userlogin.click()
    # time.sleep(5)
    username = driver.find_element_by_id("loginname")
    username.send_keys(userid)
    userpswd = driver.find_element_by_id("nloginpwd")
    userpswd.send_keys(password)
    # time.sleep(5)
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(3)
    while True:
        try:
            getPic()
        except:
            print("登陆成功----")
            break
    time.sleep(5)


def getPic():
    # 用于找到登录图片的大图
    s2 = r'//div/div[@class="JDJRV-bigimg"]/img'
    # 用来找到登录图片的小滑块
    s3 = r'//div/div[@class="JDJRV-smallimg"]/img'
    bigimg = driver.find_element_by_xpath(s2).get_attribute("src")
    smallimg = driver.find_element_by_xpath(s3).get_attribute("src")
    # print(smallimg + '\n')
    # print(bigimg)
    # 背景大图命名
    backimg = "backimg.png"
    # 滑块命名
    slideimg = "slideimg.png"
    # 下载背景大图保存到本地
    request.urlretrieve(bigimg, backimg)
    # 下载滑块保存到本地
    request.urlretrieve(smallimg, slideimg)
    # 获取图片并灰度化
    block = cv2.imread(slideimg, 0)
    template = cv2.imread(backimg, 0)
    # 二值化后的图片名称
    blockName = "block.jpg"
    templateName = "template.jpg"
    # 将二值化后的图片进行保存
    cv2.imwrite(blockName, block)
    cv2.imwrite(templateName, template)
    block = cv2.imread(blockName)
    block = cv2.cvtColor(block, cv2.COLOR_RGB2GRAY)
    block = abs(255 - block)
    cv2.imwrite(blockName, block)
    block = cv2.imread(blockName)
    template = cv2.imread(templateName)
    # 获取偏移量
    result = cv2.matchTemplate(block, template, cv2.TM_CCOEFF_NORMED)  # 查找block在template中的位置，返回result是一个矩阵，是每个点的匹配结果
    x, y = np.unravel_index(result.argmax(), result.shape)
    # print("x方向的偏移", int(y * 0.4 + 18), 'x:', x, 'y:', y)
    # 获取滑块
    element = driver.find_element_by_xpath(s3)
    ActionChains(driver).click_and_hold(on_element=element).perform()
    ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=y, yoffset=0).release().perform()
    # ActionChains(driver).release(on_element=element).perform()
    time.sleep(3)


id = "**********"  # 用户账号
passwd = "*************"  # 用户密码
loadpage(id, passwd)

# 搜索
driver.find_element_by_id("key").send_keys("华为P50pro")
driver.find_element_by_class_name("button").click()


# 选择商品
time.sleep(5)
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[5]/div/div[1]/a/img").click()

# 切换窗口
data = driver.window_handles
driver.switch_to.window(data[1])

# 加入购物车
driver.find_element_by_id("InitCartUrl").click()

driver.find_element_by_link_text('我的购物车').click()

# 切换窗口
data = driver.window_handles
driver.switch_to.window(data[2])

# 去结算
driver.find_element_by_link_text('去结算').click()
# 提交
time.sleep(5)
driver.find_element_by_id('order-submit').click()
# chromeDriver.find_element_by_link_text('提交订单').click()

# 关闭
time.sleep(3)
driver.close()
driver.quit()
