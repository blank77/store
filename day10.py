class Cup():
    __height = 0
    __volume = 0
    __color = ""
    __material = ""
    __deposit = ""

    def height(self, height):
        self.__height = height

    def volume(self, volume):
        self.__volume = volume

    def color(self, color):
        self.__color = color

    def material(self, material):
        self.__material = material

    def deposit(self, deposit):
        self.__deposit = deposit

    def describe(self):
        print("这个水杯高：", self.__height, "cm,容量是", self.__volume, "ml,颜色是", self.__color, "材质是", self.__material, "可以用来装",
              self.__deposit)


a = Cup()
a.height(30)
a.volume(1000)
a.color("蓝色")
a.material("聚乙烯")
a.deposit("水，牛奶，碳酸饮料等。。")
a.describe()


class Computer():
    __c_name = ""
    __screen = 0
    __price = 0
    __cpu = ""
    __memory = ""
    __standby_time = 0

    def computer_name(self, computer_name):
        self.__c_name = computer_name

    def screen(self, screen):
        if screen > 0:
            self.__screen = screen
        else:
            print("输入非法")

    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("输入非法")

    def cpu(self, cpu):
        self.__cpu = cpu

    def memory(self, memory):
        self.__memory = memory

    def standby_time(self, standby_time):
        if standby_time > 0:
            self.__standby_time = standby_time
        else:
            print("输入非法")

    def model(self):
        print("这台电脑电脑的显示器尺寸是", self.__screen, "英寸，价格是", self.__price, "cpu是", self.__cpu, "内存是", self.__memory, "待机时长",
              self.__standby_time, "秒")

    def type(self):
        print("我正在用", self.__c_name, "打字")

    def play(self, game):
        print("我正在用", self.__c_name, "玩", game)

    def watch(self, watching):
        print("我正在用", self.__c_name, "看", watching)


c = Computer()
c.computer_name("玩家国度rog枪神5puls")
c.screen(17.3)
c.price(18000)
c.cpu("AMD5900X")
c.standby_time(60)
c.model()
c.type()
c.play("英雄联盟")
c.watch("盗墓笔记")

