# encoding=utf-8
import time
import time
from appium import webdriver

server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',    # 平台
    # 需替换成你的driverName，如果不知 道自己的设备名，用adb命令去查看一下
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '7.1.2',      # 安卓版本
    'appPackage': 'com.ss.android.ugc.aweme',      #APP包名
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity',      # APP启动名
    'unicodeKeyboard': True,       # 这句和下面那句是避免中文问题的
    'resetKeyboard': True
    }

driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
time.sleep(12)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb").click()

time.sleep(2)
for i in range(4):
    driver.swipe(500,1200,500,300)
    time.sleep(10)


driver.quit()  # 退出driver
