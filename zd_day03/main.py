from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="test_hkr.py")


runner = HTMLTestRunner.HTMLTestRunner(
    title="这是一份HRK的测试报告",    description="这是一份详细的注册测试报告",
    verbosity=1,
    stream= open(file="注册测试报告.html",mode="w+",encoding="utf-8")

)

runner.run(tests)









