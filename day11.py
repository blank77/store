import time


class OldPhone:
    __brand = ""
    __number = ""
    __voice = ""

    def getnumber(self, phonenumber):
        self.__number = phonenumber

    def setnumber(self):
        return self.__number

    def getbrand(self, phonebrand):
        self.__brand = phonebrand

    def setbrand(self):
        return self.__brand

    def getvoice(self, phonevoice):
        self.__voice = phonevoice

    def call(self, number):
        print(self.__number, "正在给", number, "打电话，正在响铃", self.__voice)
        for i in range(8):
            print(".", end="")
            time.sleep(1)
        print("已接通")


class NewPhone(OldPhone):
    __address = ""
    __background = ""

    def __init__(self, address, background):
        self.__address = address
        self.__background = background

    def call(self, number):
        print("语音拨通中")
        super().call(number)
        print("来电号码归属于", self.__address, "显示背景为：", self.__background)

    def describe(self):
        print("品牌为:", super().setbrand(), "的手机真好用")


class Test_phone():
    phone = NewPhone("北京","奥特曼")
    phone.getnumber("15576223264")
    phone.getvoice("十年")
    phone.getbrand("华为")
    phone.call("15076227534")
    phone.describe()







class ChefClass:
    __uesrname = ""
    __age = 0

    def getusername(self, username):
        self.__username = username

    def setusername(self):
        return self.__username

    def getage(self, cookage):
        self.__age = cookage

    def setage(self):
        return self.__age

    def Steamedrice(self):
        print("厨师",self.__username,"正在蒸饭")

class Cook(ChefClass):
    def Stir(self):
        print("厨师",self.setusername(),"正在炒菜")

class Stir_try(Cook):
    def Steamedrice(self):
        print("厨师", self.setusername(), "正在蒸饭")

    def Stir(self):
        print("厨师", self.setusername(), "正在炒菜")

class Test_cook:
    cook = Stir_try()
    cook.getusername("张三")
    cook.getage(39)
    print("厨师",cook.setusername(),"今年",cook.setage())
    cook.Steamedrice()
    cook.Stir()









class Person:
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def Setname(self):
        return self.__name

    def Setsex(self):
        return self.__sex

    def Setage(self):
        return self.__age


class Worker(Person):
    def profession_news(self):
        print("工人信息为：姓名",self.Setname(),"性别",self.Setsex(),"年龄",self.Setage())
    def Work(self):
        print("工人",self.Setname(),"正在工作")


class Student(Person):
    def __init__(self, name, sex, age, sno):
        super().__init__(name, sex, age)
        self.__sno = sno

    def student(self):
        print("我是学生",self.Setname(),"性别",self.Setsex(),"年龄",self.Setage())\

    def study(self):
        print("学生",self.Setname(),"正在学习")
    def sing(self):
        print("学生",self.Setname(),"正在唱歌")

class Test_work:
    worker = Worker("李四", "男", 30)
    worker.profession_news()
    worker.Work()
    people = Student("王五", "男", 19, "161324")
    people.student()
    people.study()
    people.sing()