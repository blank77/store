from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver import ActionChains
import time
#开发者模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])


# 打开谷歌浏览器
driver = webdriver.Chrome(options=chrome_options)

# 打开淘宝网址
driver.get("https://www.taobao.com/")

# 窗口最大化
driver.maximize_window()

# 点击登录按钮
driver.find_element_by_link_text('登录').click()

# 切换窗口
data = driver.window_handles
driver.switch_to.window(data[1])

# 用户名
driver.find_element_by_id('fm-login-id').send_keys('白染天空')

# 密码
driver.find_element_by_id('fm-login-password').send_keys('13903254007zy.')

# 滑动验证
time.sleep(5)
ac = ActionChains(driver)
slider = driver.find_element_by_xpath("//*[@id='nc_2_n1z' and @class='nc_iconfont btn_slide']")  # 定位滑块
# slider = chromeDriver.find_element_by_id('nc_2_n1z')  # 定位滑块
ac.click_and_hold(slider).move_by_offset(300, 0).perform()

driver.find_element_by_class_name('fm-button fm-submit password-login').click()

# 输入框搜索
driver.find_element_by_id('q').send_keys('iphone12')

# 点击搜索
driver.find_element_by_link_text('搜索').click()

# 关闭
driver.quit()









