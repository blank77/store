# import pymysql
#
# 1.连接数据库
# con = pymysql.connect(host="localhost",user="root",password="root",database="lt")
#
# # 2.创建控制台
# cursor = con.cursor()
#
# # 3.准备一条sql语句
# sql = "insert into  person values(%s,%s,%s,%s)";
# param = ['旺财1',36,'女',5600]
# # sql = "update person set salary = salary + 2000"
# # sql = "delete from person where age > 30"
# # sql = "select * from person"
# # 4.执行sql
# cursor.execute(sql,param)  # (模板, 参数)
#
#
# # 4.1 将查询的数据提取出来
# data = cursor.fetchone()
# print(data)
#
#
#
# # 5.提交数据到数据库
# con.commit()  # 提交
#
# # 6.关闭资源
# cursor.close()
# con.close()
import time
import pymysql
import random
import itertools
# 1.连接数据库
con = pymysql.connect(host="localhost", user="root", password="root", database="bank")
# 2.创建控制台
cursor = con.cursor()

# 1.准备一个数据库 和 银行名称
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
def bank_addUser(account, username, password, country, province, street, gate, money, regiaterDate):
    # 1.判断数据库是否已满
    sql = "select count(*) from bank"
    cursor.execute(sql)
    data = cursor.fetchone()
    if data[0] >= 100:
        return 3
    # 3.正常开户
    sql = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account, username, password, country, province, street, gate, money, regiaterDate, bank_name]
    cursor.execute(sql, param)
    return 1


# 生成唯一的银行卡号
def randomCardId():
    while True:
        str = ""
        for i in range(8):
            ch = chr(random.randrange(ord("0"), ord("9") + 1))
            str += ch
        # 判断是否重复
        sql = "select account from bank"
        cursor.execute(sql)
        data = cursor.fetchall()
        if str not in data or str[0] != 0:
            # 这里是通过找一下原来的字典中是否有这个key，如果没有的话那么这个卡号就合法，前面要有个not，没有找到这个卡号那么我们创建这个卡号
            return str


# 用户的开户的操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = int(input("请输入您的开户初始余额："))  # 将输入金额转换成int类型
    regiaterDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # 随机产生8为数字
    account = randomCardId()

    status = bank_addUser(account, username, password, country, province, street, gate, money, regiaterDate)

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
        print(info % (username, password, account, country, province, street, gate, money, bank_name))


# 定义存钱的函数
def bank_store(accout_one):
    sql = "select * from bank where account = %s"
    param = [accout_one]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if  not data:
        return 1
    return 0


# 用户存钱的操作
def store_money():
    accout_one = input("请输入您的账号：")
    money_one = input("请输入您要存入的金额：")
    digit = bank_store(accout_one)
    if digit == 1:
        print("您的账号不存在！")
    elif digit == 0:
        # 用sql语句把账户存入金钱
        sql = "update bank set money = money + %s where account = %s"
        param = [money_one, accout_one]
        cursor.execute(sql, param)
        # 用sql语句查询账户金钱
        sql = "select money from bank where account= %s "
        param = [accout_one]
        cursor.execute(sql, param)
        data = cursor.fetchone()
        print("存入成功！您的账户余额为：", data[0])


# 银行的取钱逻辑

def bank_drawCash(account, password, cash):
    # 验证是否存在该卡号
    # 用sql查询所有的账号
    sql = "select * from bank where account = %s"
    param = [account]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 1
    # 验证密码
    # 用sql查询账号密码
    sql = "select * from bank where account = %s and password = %s"
    param = [account,password]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 2
    # 验证金额是否足够
    # 开始取钱
    # 判断转账金额账号是否充足
    # 用sql
    sql = "select money from bank where account = %s"
    param = [account]
    cursor.execute(sql, param)
    data = cursor.fetchone()
    if cash > data[0]:
        return 3
    return 0


def drawCash():
    account = input("请输入您的账号：")
    password = input("请输入您的账户密码：")
    cash = int(input("请输入您的取现金额："))
    status = bank_drawCash(account, password, cash)
    if status == 1:
        print("对不起，您的账号不存在，请重新输入！")
    elif status == 2:
        print("对不起，您的密码不对，请重新输入！")
    elif status == 3:
        print("对不起，您的钱不够，请重新输入！")
    elif status == 0:
        sql = "update bank set money = money - %s where account = %s"
        param = [cash, account]
        cursor.execute(sql, param)
        sql = "select money from bank where account = %s"
        param = [account]
        cursor.execute(sql, param)
        data = cursor.fetchone()
        print("取款成功，请拿好您的小票！")
        info = '''
        ---------取款信息---------
        账号：%s
        取款金额：%s
        账户余额：%s
        ------------------------
        '''
        print(info % (account, cash, data[0]))


# 转账
# 定义转账函数
def bank_transferMoney(cardNum, collection, in_password, amount):
    # 验证是否存在该卡号
    sql = "select * from bank where account = %s"
    param = [cardNum]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 1
    sql = "select * from bank where account = %s"
    param = [collection]
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    if not data1:
        return 1
    # 判断两次输入是否是同一账号
    if cardNum == collection:
        return 4
    # 验证密码
    sql = "select * from bank where account = %s and password = %s"
    param = [cardNum,in_password]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 2
    # 验证金额是否足够
    # 开始转账
    # 判断转账金额账号是否充足
    sql = "select money from bank where account = %s"
    param = [cardNum]
    cursor.execute(sql, param)
    data = cursor.fetchone()
    if amount > data[0]:
        return 3
    return 0


def transferMoney():
    cardNum = input("请输入您的卡号：")
    collection = input("请输入您要转入的卡号")
    in_password = input("请输入密码")
    amount = int(input("验证成功！请输入转账金额："))
    status = bank_transferMoney(cardNum, collection, in_password, amount)
    if status == 4:
        print("操作违法，转账失败")
    if status == 3:
        print("金额有误，转账失败！")
    elif status == 2:
        print("密码输入有误")
    elif status == 1:
        print("没有该账号，转账失败")
    elif status == 0:
        # 判定通过，将账号里的金额进行转账
        # sql语句从付款账号转出金额
        sql = "update bank set money = money - %s where account = %s"
        param = [amount, cardNum]
        cursor.execute(sql, param)
        # sql语句把钱转入收款账号
        sql = "update bank set money = money + %s where account = %s"
        param = [amount, collection]
        cursor.execute(sql, param)
        # sql语句查询付款账号余额
        sql = "select money from bank where account = %s"
        param = [cardNum]
        cursor.execute(sql, param)
        data = cursor.fetchone()
        print("转账成功！以下是您的转账信息：")
        info1 = '''
                    ----------个人信息------
                    转出账号：%s
                    转入账号：%s
                    转出金额：%s
                    您的账号余额：%s
                    ------------------------
                '''
        print(info1 % (cardNum, collection, amount, data[0]))


# 查询
def bank_query(account, password):
    # 验证是否存在该卡号
    # 用sql查询所有的账号
    sql = "select * from bank where account = %s"
    param = [account]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 1
    # 验证密码
    # 用sql查询账号密码
    sql = "select * from bank where account = %s and password = %s"
    param = [account,password]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 2
    return 0


def query():
    account = input("请输入您的卡号：")
    password = input("请输入密码:")
    status = bank_query(account, password)
    if status == 1:
        print("没有该账号")
    elif status == 2:
        print("密码输入有误")
    elif status == 0:
        # sql语句查询付款账号余额
        sql = "select * from bank where account = %s"
        param = [account]
        cursor.execute(sql, param)
        data1 = cursor.fetchall()
        data = list(data1)
        print("查询成功！以下是您的账户信息：")
        info = '''
                   ----------个人信息------
                   用户名：%s
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
        print(info % (data[0][1], data[0][0], data[0][3], data[0][4], data[0][5], data[0][6], data[0][7], data[0][9]))


#


while True:
    # 打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        addUser()
        con.commit()
    elif chose == "2":
        store_money()
        con.commit()
    elif chose == "3":
        drawCash()
        con.commit()
    elif chose == "4":
        transferMoney()
        con.commit()
    elif chose == "5":
        query()
        con.commit()
    elif chose == "6":
        print("欢迎下次光临！")
        cursor.close()
        con.close()
        break
    else:
        print("输入错误！请重新输入！")
