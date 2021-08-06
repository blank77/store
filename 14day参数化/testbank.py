from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from day8 import Bank_addUser
from day8 import Bank_store
from day8 import Bank_drawCash
from day8 import Bank_transferMoney
from day8 import Bank_query

'''
    DDT:data driver test
        ddt
        data
        unpack
    1.测试类必须用@ddt修饰
    2.测试方法使用@data引入数据源
    任务：
        将工行系统的核心业务进行测试？
        bank_addUser()

'''
# 数据源
Add = [
    ["11223344", "李四", 123456, "中国", "河北", "光明街", "S001", "2000", "2021-08-06"]
]
Sore = [
    ["11223344"]
]
Cash = [
    ["11223344",123456,"100"]
]
Transfer = [
    ["43222117","11223344",123456,"400"]
]
Query = [
    ["11223344",123456]
]

# A.addUser()
# A = Bank_addUser()
# B.store_money()
# B = Bank_store()
# C.drawCash()
# C = Bank_drawCash()
# D.transferMoney()
# D = Bank_transferMoney()
# E.query()
# E = Bank_query()

@ddt  # 注解，注释这个类是参数化类
class TestCalc(TestCase):
    # 测试开户
    @data(*Add)  # 引入数据源
    @unpack
    def testAdd(self, account, username, password, country, province, street, gate, money, regiaterDate):
        # 2.调用被测方法
        test_adduser = Bank_addUser().bank_addUser(account, username, password, country, province, street, gate, money,
                                                   regiaterDate)

        # 3.断言
        self.assertEqual(test_adduser, 1)

    # 测试存钱
    @data(*Sore)  # 引入数据源
    @unpack
    def testSore(self, account):
        # 2.调用被测方法
        test_sore = Bank_store().bank_store(account)

        # 3.断言
        self.assertEqual(test_sore, 0)

    # 测试取钱
    @data(*Cash)  # 引入数据源
    @unpack
    def testCash(self, account, password, cash):
        # 2.调用被测方法
        test_Cash = Bank_drawCash().bank_drawCash(account, password, cash)

        # 3.断言
        self.assertEqual(test_Cash, 0)

    # 测试转账
    @data(*Transfer)  # 引入数据源
    @unpack
    def testTeansfer(self, cardNum, collection, in_password, amount):
        # 2.调用被测方法
        test_Teansfer = Bank_transferMoney().bank_transferMoney(cardNum, collection, in_password, amount)

        # 3.断言
        self.assertEqual(test_Teansfer, 0)

    # 测试查询
    @data(*Query)  # 引入数据源
    @unpack
    def testQurey(self, account, password):
        # 2.调用被测方法
        test_Qurey = Bank_query().bank_query(account, password)

        # 3.断言
        self.assertEqual(test_Qurey, 0)
