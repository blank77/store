from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="test_ss.py")
'''
'''

runner = HTMLTestRunner.HTMLTestRunner(
    title="这是一份抖音的测试报告",   #标题
    description="这是一份详细的抖音的测试报告",    #备注
    verbosity=1,
    stream= open(file="抖音测试报告.html",mode="w+",encoding="utf-8")

)
'''
verbosity是一个选项,表示测试结果的信息复杂度，有0、1、2 三个值
0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共10个 失败2 成功8
1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
并且 你在命令行里加入不同的参数可以起到一样的效果
加入 --quiet 参数 等效于 verbosity=0
加入--verbose参数等效于 verbosity=2
'''
runner.run(tests)









