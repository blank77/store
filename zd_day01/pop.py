from selenium import webdriver
import time

driver = webdriver.Chrome()
#打开
driver.get(r"F:\python自动化测试\python\python自动化\day01\练习的html\练习的html\跳转页面\pop.html")
#最大化
driver.maximize_window()
#定义按钮
driver.find_element_by_id("goo").click()

time.sleep(3)
driver.quit()
