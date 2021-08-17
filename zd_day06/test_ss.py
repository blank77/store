from unittest import TestCase
from appium import webdriver
from ddt import ddt
from ddt import data
from method import Method
from Initregister import initregister
import time

@ddt
class Test_hkr(TestCase):

    def setUp(self) -> None:
        server = r'http://localhost:4723/wd/hub'  # Appium Server, 端口默认为4723
        desired_capabilities = {
            'platformName': 'Android',  # 平台
            # 需替换成你的driverName，如果不知 道自己的设备名，用adb命令去查看一下
            'deviceName': '127.0.0.1:62001',
            'platformVersion': '7.1.2',  # 安卓版本
            'appPackage': 'com.ss.android.ugc.aweme',  # APP包名
            'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity',  # APP启动名
            'unicodeKeyboard': True,  # 这句和下面那句是避免中文问题的
            'resetKeyboard': True
        }

        self.driver = webdriver.Remote(server, desired_capabilities)  # 连接手机和APP

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()

    # @data(*initregister.register_success_data)
    def test_register_success(self):
        login = Method(self.driver)
        login.register()


