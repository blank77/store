from unittest import TestCase
from selenium import webdriver
from ddt import ddt
from ddt import data
from method import Method
from Initregister import initregister
import time

@ddt
class Test_hkr(TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/HKR")
        time.sleep(2)

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()
        self.driver.close()

    @data(*initregister.register_success_data)
    def test_register_success(self, initdata):
        # 提取用户名，密码，期望结果
        username = initdata["username"]
        password = initdata["password"]
        age = initdata["age"]
        sex = initdata["sex"]
        job = initdata["job"]
        mail = initdata["mail"]
        phone = initdata["phone"]
        address = initdata["address"]
        expect = initdata["expect"]

        login = Method(self.driver)
        login.register(username, password, age, sex, job, mail, phone, address)

        #  获取实际结果
        result = login.get_success_one()

        # 断言
        self.assertEqual(expect, result)

    @data(*initregister.register_error_data)
    def test_register_error(self, initdata):
        # 提取用户名，密码，期望结果
        username = initdata["username"]
        password = initdata["password"]
        age = initdata["age"]
        sex = initdata["sex"]
        job = initdata["job"]
        mail = initdata["mail"]
        phone = initdata["phone"]
        address = initdata["address"]
        expect = initdata["expect"]

        login = Method(self.driver)
        login.register(username, password, age, sex, job, mail, phone, address)

        #  获取实际结果
        result = login.get_error_two()
        # 断言
        self.driver.save_screenshot("register.jpg")
        self.assertEqual(expect, result)