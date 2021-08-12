from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

# 创建谷歌浏览器对象
driver = webdriver.Chrome(options=chrome_options)

# 打开网址
driver.get("https://www.suning.com/")

# 窗口最大化
driver.maximize_window()
time.sleep(2)

# # 登录
# driver.find_element_by_link_text('登录').click()
#
# # 点击账户登录
# driver.find_element_by_link_text('账户登录').click()
#
# # 账户
# driver.find_element_by_id('userName').send_keys('1231232')
#
# # 密码
# driver.find_element_by_id('password').send_keys('213123')
# time.sleep(3)
# driver.find_element_by_id('iar1_sncaptcha_button').click()
# # 点击登录
# driver.find_element_by_id('submit').click()

# 搜索框
driver.find_element_by_id("searchKeywords").send_keys("华为P50pro")
# 点击搜索
driver.find_element_by_id("searchSubmit").click()

# 选择一个商品
time.sleep(3)
# chromeDriver.find_element_by_name('ssdsn_search_pro_name02-1_0_0_12156210854_0070094634').click()
driver.find_element_by_xpath("//*[@id='ssdsn_search_pro_baoguang-1-0-1_1_02:0070094634_12308467927']/img").click()

# 切换窗口
data = driver.window_handles
driver.switch_to.window(data[1])

# 添加购物车
driver.find_element_by_id("addCart").click()
time.sleep(3)
# 结算
driver.find_element_by_name('cart1_go').click()

# 去结算
driver.find_element_by_name('icart1_ope_buy01').click()
time.sleep(3)
driver.close()
driver.quit()