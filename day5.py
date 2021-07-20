# author:jason
'''
    任务1：
        将导航系统与商城系统结合一起。
'''
# 准备商品

#景点字典
data = {
    "北京": {
        "昌平": {
            "十三陵": ["十三陵水库", "沙河水库"],
            "高校": ["北京邮电大学", "中央戏剧学院", "北京师范大学", "华北电力大学", "北京航空航天大学"],
            "天通苑": ["海底捞", "呷哺呷哺"]
        },
        "海淀": {
            "公主坟": ["军事博物馆", "中华世纪园"],
            "科普场馆": ["中国科技馆", "北京天文馆"],
            "高校": ["北京大学", "清华大学"],
            "景区": ["北京植物园", "香山公园", "玉渊潭公园"]
        },
        "朝阳": {
            "龙城": ["鸟化石国家地质公园", "朝阳南北塔"],
            "双塔": ["朝阳凌河公园", "朝阳凤凰山"]
        },
        "延庆": {
            "龙庆峡": ["龙庆峡景区"]
        }
    },
    "天津": {
        "武清区": {
            "下朱庄街": ["南湖景区"],
            "雍和道": ["凯旋王国主题乐园"],
            "开发区": ["天鹅湖温泉度假村"]
        },
        "西青区": {
            "现代农业核心区": ["水高庄园"],
            "精武镇小南河村": ["精武门"],
            "大寺镇王村": ["峰山药王庙"]
        }
    }
}


# 打印城市
def print_place(choice):
    for i in choice:
        print(i)


# 攻略
for i in data:
    print(i)

while True:
    city1 = input("请输入您要去的城市：")
    if city1 in data:
        print_place(data[city1])
        city2 = input("请输入二级城市：")
        if city2 in data[city1]:
            print_place(data[city1][city2])
            city3 = input("请输入三级地区：")
            if city3 in data[city1][city2]:
                print_place(data[city1][city2][city3])
                # 商城系统
                shop = [
                    ["劳力士手表", 200000],
                    ["Iphone 12X plus", 12000],
                    ["lenovo PC", 6000],
                    ["HUA WEI WATCH", 1200],
                    ["Mac PC", 15000],
                    ["辣条", 2.5],
                    ["老干妈", 20]
                ]
                # 初始化钱包
                while True:
                    money = input("请输入您的余额：")
                    if money.isdigit():
                        money = int(money)  # "200000" --> 200000
                        break
                    else:
                        print("金额只能为数字，请重新输入！")
                # 空的购物车
                mycart = []

                # 优惠券

                # 定义联想电脑优惠券
                import random

                a = [
                    ["lenovo PC", "联想电脑1折优惠券", 0.1]
                ]
                # 定义老干妈优惠券
                b = [
                    ["老干妈", "老干妈7折优惠券", 0.7]
                ]
                # 定义优惠券数量
                coupon = a * 20 + b * 10
                # 定义优惠券随机
                coupon_sel = random.choice(coupon)
                # 判断是否需要优惠券
                while True:
                    favour = input("是否需要优惠券 y/n")
                    if favour == "y":
                        print("恭喜你获得了", coupon_sel[1])
                        # 改掉商场价格
                        for index, value in enumerate(shop):
                            if value[0] == coupon_sel[0]:
                                value[1] = value[1] * coupon_sel[2]
                        break
                    elif favour == "n":
                        print("很遗憾您放弃了本次优惠券，祝您购物愉快")
                        break
                    else:
                        print("输入错误，请重新选择")
                # 购物
                while True:
                    print("-----------------------------------------")
                    print("-编号\t名称\t\t原价\t\t现价-")
                    print("-----------------------------------------")
                    for index, value in enumerate(shop):
                        # 判断是否是打折商品
                        if value[0] == coupon_sel[0]:
                            # 打印打折商品现价和原价
                            print("|", index, "\t", value[0], "\t", (value[1] / coupon_sel[2]), "\t", (value[1]))
                        else:
                            # 打印未打折商品
                            print("|", index, "\t", value[0], "\t", value[1], "\t", value[1])
                    print("------------------------------------------")
                    # 请输入商品编号
                    chose = input("请输入您要的商品：")
                    # 判断是否是商品编号
                    if chose.isdigit():
                        chose = int(chose)
                        if chose > len(shop) - 1:
                            print("没有该商品编号")
                        else:
                            # 判断钱是否够
                            if money > shop[chose][1]:
                                mycart.append(shop[chose])
                                # 钱减去
                                money = money - shop[chose][1]
                                print("恭喜，成功添加购物车，您的余额还剩：￥", money)
                            else:
                                print("对不起，穷鬼，余额不足，请到商城去购买！")
                    elif chose == "q" or chose == "Q":
                        print("谢谢惠顾，欢迎下次光临")
                        break
                    else:
                        print("输入错误，请输入商品编号")
                # 打印小票
                print("下面是您的购物小条，请拿好：")
                for index, value in enumerate(mycart):
                    print(index, "   ", value)
                print("您的钱包还剩：￥", money)
                #退出整个系统
                break
            elif city3 == 'q' or city3 == "Q":
                print("------------------欢迎下次光临Jason旅行社！------------------")
                break
            else:
                print("当前三级地区不存在，别瞎弄！")
        elif city2 == 'q' or city2 == "Q":
            print("------------------欢迎下次光临Jason旅行社！------------------")
            break
        else:
            print("当前二级城市不存在，别瞎弄！")
    elif city1 == 'q' or city1 == "Q":
        print("------------------欢迎下次光临Jason旅行社！------------------")
        break
    else:
        print("当前城市不存在，别瞎弄！")
