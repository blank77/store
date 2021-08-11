from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR")
driver.maximize_window()
#登录
driver.find_element_by_xpath("//*[@id='loginname' and @name='loginname']").send_keys("root")
driver.find_element_by_xpath("//*[@id='password' and @name='password']").send_keys("root")
driver.find_element_by_xpath("//*[@id='submit' and @value='登陆']").click()
#更换头像
driver.find_element_by_xpath("//*[@id='img']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='ul_pic']/li[3]").click()
# driver.find_element_by_xpath("//*[@id='lablefile']").click()
# time.sleep(2)
# driver.get(r"D:\python\1.jpg")
# driver.find_element_by_xpath("//*[@id='pic_btn']").click()
#跳转首页
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[1]").click()
driver.refresh()
#评价表
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]/select").send_keys("9（上晚自习）")
driver.find_element_by_xpath("//*[@id='tea_td']/select").send_keys("贾生")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[5]/td[3]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[6]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[7]/td[3]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[8]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[9]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[10]/td[3]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[11]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[12]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='textarea']").send_keys("很好")
driver.find_element_by_xpath("//*[@id='subtn']").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[7]/div[3]/a").click()
time.sleep(1)
#跳转修改信息页面
driver.find_element_by_xpath("//*[@id='_easyui_tree_8']/span[4]/a").click()
#修改信息
time.sleep(1)
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[1]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[1]/td[2]/input").send_keys("旺柴")

driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[3]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[3]/td[2]/input").send_keys("123456")

driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").clear()
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").send_keys("10")

driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[5]/td[2]/select").send_keys("女")

driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[6]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[6]/td[2]/input").send_keys("河北")

driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[8]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[8]/td[2]/input").send_keys("123456789@qq.com")

driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[9]/td[2]/textarea").send_keys("旺旺")
# driver.find_element_by_xpath("//*[@id='btn_modify']").click()

# time.sleep(3)
# driver.quit()