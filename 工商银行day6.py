'''
    中国工商银行账户管理系统：
        ICBC:
'''
import random
# 1.准备一个数据库 和 银行名称
bank = {
    "12345678":{        "username":"张三",
                        "password":"123456",
                        "country":"中国",
                        "province":"北京市",
                        "street":"沙河镇",
                        "gate":"s001",
                        "money":5000,
                        "bank_name":"中国工商银行回龙观支行"
                        },
    "22345678":{        "username":"张三",
                        "password":123456,
                        "country":"中国",
                        "province":"北京市",
                        "street":"沙河镇",
                        "gate":"s002",
                        "money":9000,
                        "bank_name":"中国工商银行回龙观支行"
                        }
}  # 空的数据库
'''
    {
        "张三":{
            account:s001,
            country:"中国"
        }，
        "李四":{
            
        }
    
    
    }

'''
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的



# 2.入口程序
def welcome():
    print("*************************************")
    print("*      中国工商银行昌平支行           *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")


# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,gate,money):
    # 1.判断数据库是否已满
    if len(bank) >= 100:
        return 3
    # 3.正常开户
    bank[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "gate":gate,
        "money":money,
        "bank_name":bank_name
    }
    return 1
#生成唯一的银行卡号
def randomCardId():
    while True:
        str = ""
        for i in range(8):
            ch = chr(random.randrange(ord("0"), ord("9") + 1))
            str += ch
        #判断是否重复
        if not bank.get(str):
            # 这里是通过找一下原来的字典中是否有这个key，如果没有的话那么这个卡号就合法，前面要有个not，没有找到这个卡号那么我们创建这个卡号
            return str
# 用户的开户的操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password  = input("请输入您的开户密码：")
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street =  input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = int(input("请输入您的开户初始余额："))  # 将输入金额转换成int类型
    # 随机产生8为数字
    account = randomCardId()

    status = bank_addUser(account,username,password,country,province,street,gate,money)

    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            ----------个人信息------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            ------------------------
        '''
        print(info % (username,password,account,country,province,street,gate,money,bank_name))

# 定义存钱的函数
def bank_store(accout_one):
    accout_two = bank.get(accout_one)
    if not accout_two:
        return 1
    return 0


# 用户存钱的操作
def store_money():
    accout_one = input("请输入您的账号：")
    money_one = input("请输入您要存入的金额：")
    money_one = int(money_one)
    digit = bank_store(accout_one)
    if digit == 1:
        print("您的账号不存在！")
    elif digit == 0:
        bank[accout_one]["money"] = bank[accout_one]["money"] + money_one
        print("存入成功！您的账户余额为：", bank[accout_one]["money"])

# 银行的取钱逻辑

def bank_drawCash(account,password,cash):
    # 验证是否存在该卡号
    user = bank.get(account)
    # 用get 方法判定卡号是否存在,如果不存在返回none,if not 就返回true
    if not user:
        return 1
    # 验证密码
    if password != bank[account]["password"]:
        return 2
    # 验证金额是否足够
    # 开始取钱
    # 判断转账金额账号是否充足
    if cash > bank[account]["money"]:
        return 3
    return 0

def drawCash():
    account = input("请输入您的账号：")
    password = input("请输入您的账户密码：")
    cash = int(input("请输入您的取现金额："))
    status = bank_drawCash(account,password,cash)
    if status == 1:
        print("对不起，您的账号不存在，请重新输入！")
    elif status == 2:
        print("对不起，您的密码不对，请重新输入！")
    elif status == 3:
        print("对不起，您的钱不够，请重新输入！")
    elif status == 0:
        bank[account]["money"] = bank[account]["money"] - cash
        acc_balance = bank[account]["money"]
        print("取款成功，请拿好您的小票！")
        info = '''
        ---------取款信息---------
        账号：%s
        取款金额：%s
        账户余额：%s
        ------------------------
        '''
        print(info % (account,cash,acc_balance))

#转账
#定义转账函数
def bank_transferMoney(cardNum,collection,in_password,amount):
    # 验证是否存在该卡号
    user = bank.get(cardNum)
    user_z = bank.get(collection)
    # 用git 方法判定卡号是否存在,如果不存在返回none,if not 就返回true
    if not user or not user_z:
        return 1
    # 判断两次输入是否是同一账号
    if bank[cardNum] == bank[collection]:
        return 4
    # 验证密码
    if in_password != bank[cardNum]["password"]:
        return 2
    #验证金额是否足够
    # 开始转账
    # 判断转账金额账号是否充足
    if amount > bank[cardNum]["money"]:
        return 3
    return 0

def transferMoney():
    cardNum = input("请输入您的卡号：")
    collection = input("请输入您要转入的卡号")
    in_password = input("请输入密码")
    amount = int(input("验证成功！请输入转账金额："))
    status = bank_transferMoney(cardNum,collection,in_password,amount)
    if status == 4:
        print("操作违法，转账失败")
    if status == 3:
        print("金额有误，转账失败！")
    elif status == 2:
        print("密码输入有误")
    elif status == 1:
        print("没有该账号，转账失败")
    elif status == 0:
        #判定通过，将账号里的金额进行转账
        bank[cardNum]["money"] = bank[cardNum]["money"] - amount
        bank[collection]["money"] = bank[collection]["money"] + amount
        #将账户的金额赋予变量
        balance = bank[cardNum]["money"]
        payee = bank[collection]["money"]
        print("转账成功！以下是您的转账信息：")
        info1 = '''
                    ----------个人信息------
                    转出账号：%s
                    转入账号：%s
                    转出金额：%s
                    您的账号余额：%s
                    您转入账号余额：%s
                    ------------------------
                '''
        print(info1 % (cardNum,collection,amount,balance,payee))

#查询
def bank_query(amount,password):
    # 验证是否存在该卡号
    user = bank.get(amount)
    # 用git 方法判定卡号是否存在,如果存在返回none,if not 就返回true
    if not user:
        return 1
    # 验证密码
    if password != bank[amount]["password"]:
        return 2
    return 0

def query():
    amount = input("请输入您的卡号：")
    password = input("请输入密码:")
    status = bank_query(amount,password)
    if status == 1:
        print("没有该账号")
    elif status == 2:
        print("密码输入有误")
    elif status == 0:
        print("查询成功！以下是您的账户信息：")
        info = '''
                   ----------个人信息------
                   用户名：%s
                   密码：%s
                   账号：%s
                   地址信息
                       国家：%s
                       省份：%s
                       街道：%s
                       门牌号: %s
                   余额：%s
                   开户行地址：%s
                   ------------------------
               '''
        print(info % (bank[amount]["username"], bank[amount]["password"], amount, bank[amount]["country"], bank[amount]["province"], bank[amount]["street"], bank[amount]["gate"], bank[amount]["money"], bank_name))







while True:
    # 打印欢迎程序
    welcome()
    chose  = input("请输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        store_money()
    elif chose == "3":
        drawCash()
    elif chose == "4":
        transferMoney()
    elif chose == "5":
        query()
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")








