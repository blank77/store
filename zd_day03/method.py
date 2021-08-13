import time
class Method:
    def __init__(self,driver):
        self.driver = driver

    def register(self,username,password,age,sex,job,mail,phone,address):
        self.driver.find_element_by_link_text("新来的童鞋来这里注册一下哦").click()
        # 用户名
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys(username)
        # 密码
        self.driver.find_element_by_xpath("//*[@id='pwd']").send_keys(password)
        self. driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys(password)
        #下一步
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()
        time.sleep(3)
        #年龄
        self.driver.find_element_by_xpath("//*[@id='valid_age']").send_keys(age)
        #性别
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/select[1]").send_keys(sex)
        #职位
        self.driver.find_element_by_xpath("//*[@id='classname']").send_keys(job)
        #下一步
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()
        time.sleep(3)
        #邮箱
        self.driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys(mail)
        #电话
        self.driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys(phone)
        #地址
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys(address)
        #注册
        self.driver.find_element_by_xpath("//*[@id='btn_reg']").click()

    def get_success_one(self):
        return self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]").text

    def get_error_two(self):
        return self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]").text
