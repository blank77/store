'''
    需求：
        购物流程。
        1.商品在货架上
        2.空的购物车
        3.自己的初始化资金
    技术选型：
        1.容器
            列表： []
        2.循环技术
            while
            for i in  enumerate(li)
        3.判断
        4.键盘输入
    任务：
    [10张老干妈：7折优惠券，20张联想电脑1折优惠券]
    开始买东西之前，提示是否要抽一张优惠券。
        若是：随机给一张，最终要进行使用优惠券的进行结算。
        若否：正常买东西
'''



#1.准备商品
shop = [
    ["劳力士手表",200000],
    ["Iphone 12X plus",12000],
    ["lenovo PC",6000],
    ["HUA WEI WATCH",1200],
    ["Mac PC",15000],
    ["辣条",2.5],
    ["老干妈",13]
]
# 2. 初始化钱包
money = input("请输入您的余额：")
money = int(money)  # "200000" --> 200000

# 3.空的购物车
mycart = []


#优惠券

#定义联想电脑优惠券
import random

a = [
    ["lenovo PC","联想电脑1折优惠券",0.1]
]
#定义老干妈优惠券
b = [
    ["老干妈","老干妈7折优惠券",0.7]
]
#定义优惠券数量
coupon = a * 20 + b * 10
#定义优惠券随机
coupon_sel = random.choice(coupon)


whether = ["y", "n"]
i = 0
l = 0
judge = input("您是否抽一张优惠券：（y/n）")
if judge in whether:  # 判断是否需要优惠券
    if judge == "n":
        # 4.买东西
        while i <= 20:
            if money == 0:
                print("你已经没有钱了穷鬼，请充值再来")
                break  # 终结循环
            else:
                # 4.1 展示商品
                for key, value in enumerate(shop):
                    print(key, value)
                # 4.2 请输入您想要的商品
                chose = input("亲输入您想要的商品编号：")  # "1"
                # 4.3
                if chose.isdigit():
                    chose = int(chose)
                    # 4.4 先判断是否存在该商品
                    if chose > 6:
                        print("您输入的商品不存在！别瞎弄！")
                    else:
                        # 4.5 判断您的余额是否足够
                        if money < shop[chose][1]:
                            print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
                        else:
                            # 4.6 将商品添加到购物车 ，余额减去对应的钱
                            mycart.append(shop[chose])
                            money = money - shop[chose][1]
                            print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                elif chose == "q" or chose == "Q":
                    print("拜拜了，您嘞！欢迎下次光临！")
                    break
                else:
                    print("对不起，您输入有误，请重新输入！")
    elif judge == "y":
        print("恭喜你抽中了", coupon_sel[1])
        # 4.买东西
        while i <= 20:
            if money == 0:
                print("你已经没有钱了穷鬼，请充值再来")
                break  # 终结循环
            else:
                # 4.1 展示商品
                for key, value in enumerate(shop):
                    print(key, value)
                # 4.2 请输入您想要的商品
                chose = input("亲输入您想要的商品编号：")  # "1"
                # 4.3
                if chose.isdigit():
                    chose = int(chose)
                    # 4.4 先判断是否存在该商品
                    if chose > 6:
                        print("您输入的商品不存在！别瞎弄！")
                    else:
                        if shop[chose][0] == coupon_sel[0]:
                            # 4.5 判断您的余额是否足够
                            if money < shop[chose][1] * coupon_sel[2]:
                                print("对不起，穷鬼，您连打折的东西都买不起吗？请到其他超市买东西去！")
                            else:
                                # 4.6 将商品添加到购物车 ，余额减去对应的钱
                                mycart.append(shop[chose])
                                money = money - shop[chose][1] * coupon_sel[2]
                                print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                        else:
                            # 4.5 判断您的余额是否足够
                            if money < shop[chose][1]:
                                print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
                            else:
                                # 4.6 将商品添加到购物车 ，余额减去对应的钱
                                mycart.append(shop[chose])
                                money = money - shop[chose][1]
                                print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                elif chose == "q" or chose == "Q":
                    print("拜拜了，您嘞！欢迎下次光临！")
                    break
                else:
                    print("对不起，您输入有误，请重新输入！")
else:
    print("因为您输入的数据错误，所以系统自动认为您放弃了")
    # 4.买东西
    while i <= 20:
        if money == 0:
            print("你已经没有钱了穷鬼，请充值再来")
            break  # 终结循环
        else:
            # 4.1 展示商品
            for key, value in enumerate(shop):
                print(key, value)
            # 4.2 请输入您想要的商品
            chose = input("亲输入您想要的商品编号：")  # "1"
            # 4.3
            if chose.isdigit():
                chose = int(chose)
                # 4.4 先判断是否存在该商品
                if chose > 6:
                    print("您输入的商品不存在！别瞎弄！")
                else:
                    # 4.5 判断您的余额是否足够
                    if money < shop[chose][1]:
                        print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
                    else:
                        # 4.6 将商品添加到购物车 ，余额减去对应的钱
                        mycart.append(shop[chose])
                        money = money - shop[chose][1]
                        print("恭喜，成功添加购物车！您的余额还剩￥：", money)
            elif chose == "q" or chose == "Q":
                print("拜拜了，您嘞！欢迎下次光临！")
                break
            else:
                print("对不起，您输入有误，请重新输入！")
# 打印购物小条
print("以下是您的购物小条，请拿好：")
for key ,value in  enumerate(mycart):
    print(key,value)
print("本次余额还剩：￥",money)














