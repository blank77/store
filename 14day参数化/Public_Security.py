import pymysql
import time
import random
class Sql:
    def __init__(self):
        self.con = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='police',
                               charset='utf8')
        self.cursor = self.con.cursor()

    def update(self,sql):
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()
        cursor.close()
        self.con.close()

    def select(self,sql, mode="all", size=1):
        cursor = self.con.cursor()
        cursor.execute(sql)
        if mode == "all":
            return cursor.fetchall()
        elif mode == "one":
            return cursor.fetchone()
        elif mode == "many":
            return cursor.fetchmany(size)
        #
        self.con.commit()
        cursor.close()
        self.con.close()



class User:
    def __init__(self,ID,name,sex,age,password,state,country,province,street,door,registration_time,immigrant_time,honor,culture,learn):
        self.__ID = ID
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__password = password
        self.__state = state
        self.__country = country
        self.__province = province
        self.__street = street
        self.__door = door
        self.__registration_time = registration_time
        self.__immigrant_time = immigrant_time
        self.__honor = honor
        self.__culture = culture
        self.__learn = learn




class R_public_security:
    def __init__(self,l_name):
        self.__l_name = l_name

class L_country:
    def __init__(self,c_name):
       self.__c_name = c_name


class Admin(object):

    def printSysFunctionView(self):
        print("****************************************************")
        print("*         注册（1）            查询（2）            *")
        print("*         移民（3）            删除（4）            *")
        print("*         学习（5）            退出（q）            *")
        print("****************************************************")

class System:
    # 生成唯一的银行卡号
    str = ""
    def randomCardId(self,province):
        global str
        if province == "河北":
            self.str = "130"
        elif province == "山西":
            self.str = "144"
        while True:
            for i in range(29):
                ch = chr(random.randrange(ord("0"), ord("9") + 1))
                self.str += ch
            # 判断是否重复
            sql = "select ID from province"
            S = Sql()
            data = S.select(sql,"all")
            if self.str not in data:
                # 这里是通过找一下原来的字典中是否有这个key，如果没有的话那么这个卡号就合法，前面要有个not，没有找到这个卡号那么我们创建这个卡号
                return self.str

    def register(self):
        name = input("请输入您的姓名：")
        sex = input("请输入您的性别")
        age = input("请输入您的年龄")
        password = input("请输入您的密码：")
        state = "true"
        country = input("请输入您的国籍：")
        province = input("请输入您的居住省份：")
        street = input("请输入您的街道：")
        door = input("请输入您的门牌号：")
        print("********************************************************")
        print("*         0：没有教育历史（包括幼儿园）     1：小学文化      *")
        print("*         2：初中文化                    3：高中文化      *")
        print("*         4：大学文化（硕士生）            5：研究生       *")
        print("*         6：博士生                      7：教授         *")
        print("********************************************************")
        culture = input("您的文化程度是：")
        immigrant_time = ""
        registration_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if culture == 4 or culture == 5 or culture == 6:
            honor = 0
        elif culture == 7:
            honor = 1
        else:
            honor = 2
        # 随机产生32为数字
        ID = self.randomCardId(province)
        learn = 0
        sql = "insert into bank values({},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(ID,name,sex,age,password,state,country,province,street,door,registration_time,immigrant_time,honor,culture,learn)
        print(sql)


main = System()
main.register()
