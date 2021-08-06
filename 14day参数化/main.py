
from HTMLTestRunner import HTMLTestRunner  # 运行器
import unittest


# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"F:\python自动化测试\python\day10【面向对象】",pattern="testbank.py")

# 2.使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是一份银行的测试报告",
    description="工商银行的测试报告",
    verbosity=1,
    stream= open("银行.html",mode="w+",encoding="utf-8")
)

# 3.运行所有用例
runner.run(tests)


# 4.实现邮件发送






