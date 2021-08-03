import threading
import time

breads = 0


class Cook(threading.Thread):
    username = ""
    bread = 0

    def __init__(self, *args, **kwargs):
        super(Cook, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    def run(self) -> None:
        global breads
        while self.__running.isSet():
            if breads == 600:
                self.__flag.clear()
                time.sleep(0.5)
            elif breads < 600:
                self.__flag.set()
                time.sleep(0.5)
                self.bread += 1
                breads += 1
                print("厨师{}已做了{}个面包".format(self.username, self.bread))
                print("销售柜台总共有{}个面包".format(breads))


class Customer(threading.Thread):
    username = ""
    money = 0
    count = 0

    def run(self) -> None:
        global breads
        while True:
            if self.money > 0:
                if breads > 0:
                    breads -= 1
                    self.money -= 2
                    self.count += 1
                    print("顾客{}已买了{}".format(self.username, self.count))
                elif breads == 0:
                    time.sleep(1)
            elif self.money == 0:
                print("顾客{}已消费完".format(self.username))
                break


cook1 = Cook()
cook2 = Cook()
cook3 = Cook()
cook1.username = "张三"
cook2.username = "李四"
cook3.username = "王五"
shopper1 = Customer()
shopper2 = Customer()
shopper3 = Customer()
shopper4 = Customer()
shopper5 = Customer()
shopper6 = Customer()
shopper1.username = "1"
shopper2.username = "2"
shopper3.username = "3"
shopper4.username = "4"
shopper5.username = "5"
shopper6.username = "6"
cook1.start()
cook2.start()
cook3.start()
shopper1.start()
shopper2.start()
shopper3.start()
shopper4.start()
shopper5.start()
shopper6.start()
