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

# # 用户名
# driver.find_element_by_id('fm-login-id').send_keys('白染天空')
#
# # 密码
# driver.find_element_by_id('fm-login-password').send_keys('')
driver.find_element_by_xpath("//*[@id='login']/div[1]/i").click()
time.sleep(10)



# 输入框搜索
driver.find_element_by_id('q').send_keys('华为P50pro')

# 点击搜索
driver.find_element_by_xpath("//*[@id='J_TSearchForm']/div[1]/button").click()

data = driver.window_handles
driver.switch_to.window(data[1])
time.sleep(2)
driver.find_element_by_xpath("//*[@id='J_Itemlist_PLink_630673675853']").click()

data = driver.window_handles
driver.switch_to.window(data[2])
time.sleep(2)
driver.find_element_by_link_text("4G全网通").click()

driver.find_element_by_link_text("亮黑色").click()

driver.find_element_by_link_text("8+256GB").click()
driver.find_element_by_xpath("//*[@id='J_LinkBasket']").click()
time.sleep(3)

driver.find_element_by_xpath("//*[@id='mc-menu-hd']").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='J_SelectAll1']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='J_FloatBar']/div[2]/div[3]/div[5]").click()
# 关闭
time.sleep(4)
driver.close()
driver.quit()









