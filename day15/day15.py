import pymysql


class Sql:
    def __init__(self):
        self.con = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='bank',
                                   charset='utf8')

    def update(self, sql, param):
        cursor = self.con.cursor()
        self.con.ping(reconnect=True)
        cursor.execute(sql, param)
        self.con.commit()
        cursor.close()
        self.con.close()

    def all(self, sql, mode="all", size=1):
        cursor = self.con.cursor()
        self.con.ping(reconnect=True)
        cursor.execute(sql)
        if mode == "all":
            return cursor.fetchall()
        elif mode == "one":
            return cursor.fetchone()
        elif mode == "many":
            return cursor.fetchmany(size)

    def select(self, sql, param, mode="all", size=1):
        cursor = self.con.cursor()
        self.con.ping(reconnect=True)
        cursor.execute(sql, param)
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


# 百度面试题
# if __name__ == '__main__':
#     name = "baidu_x_system.log"
#     with open(file=name,mode="r",encoding="utf-8") as f:
#         lines = f.readlines()#获取所有行
#         sum = 0
#         list = []
#         list1 = []
#         for line in lines:#第i行
#             #找到第一个空格
#             for j in range(len(line)):
#                 if line[j].isspace() == True:
#                     a = line[:j]
#                     list1.append(a)
#                     if a not in list:
#                         list.append(a)
#                         sum += 1
#                     break
#         print(list1)
#         print(list)
# list = set(list1)  #list是另外一个列表，里面的内容是list1里面的无重复项
# for item in list:
#   print("the %s has found %s" %(item,list1.count(item)))
#     f.close()

# 写入数据库
# if __name__ == '__main__':
#     name = "用户数据.txt"
#     sum = 0
#     with open(file=name, mode="r", encoding="utf-8") as f:
#         lines = f.readlines()  # 获取所有行
#         s = [x.strip() for x in lines if x.strip() != '']
#         S = Sql()
#         for i in s:
#             y = i.split(",")
#             sql = "insert into wages values(%s,%s,%s)"
#             S.update(sql, y)
#             sum = sum + int(y[2])
#     print(sum)
#     f.close()


# #复制图片
# if __name__ == "__main__":
#     name = "大美女.jpg"
#     with open(file=name,mode="rb") as f:
#         with open(file="d:\python\大美女.jpg",mode="wb") as f1:
#             data = f.read()
#
#             f1.write(data)
#
#             f1.flush()
#             f1.close()
#             f.close()


# #模拟图片上传
# if __name__ == "__main__":
#     name = input("请输入您要上传证件的路径")
#     with open(file=name,mode="rb") as f:
#         with open(file="d:\python\大美女.jpg",mode="wb") as f1:
#             data = f.read()
#
#             f1.write(data)
#
#             f1.flush()
#             f1.close()
#             f.close()


class Record:
    def adduser(self):
        while True:
            username = input("请输入您的用户名：")
            if username == "q":
                print("谢谢使用")
                break
            password = input("请输入您的开户密码：")
            sex = input("请输入您的性别：")
            age = input("请输入您的年龄：")
            site = input("请输入您的地址：")
            route = input("请输入您的头像路径：")
            with open(file="name.txt", mode="r+", encoding="utf-8")as r:
                # 读取文件内容
                t = r.readlines()
                r.close()
                lines = []
                # 去除\n符号
                s = [x.strip() for x in t if x.strip() != '']
                # 把列表进行切片以,分割开
                for i in s:
                    y = i.split(",")
                    lines.append(y)
                for j in lines:
                    if j[0] == username:
                        print("用户名已存在请重新输入！")
                    else:
                        with open(file=route, mode="rb") as f:
                            with open(file="d:\python\{}的头像.jpg".format(username), mode="wb") as f1:
                                data = f.read()
                                f1.write(data)
                                # 刷新
                                f1.flush()
                                # 关闭资源
                                f1.close()
                                f.close()

                        with open(file="name.txt", mode="a+", encoding="utf-8") as w:
                            w.write("\r{},{},{},{},{},{}".format(username, password, sex, age, site, route))
                            w.flush()
                            w.close()
                        print("添加用户成功")

    def log(self):
        while True:
            username = input("请输入您的用户名：")
            if username == "q":
                print("谢谢使用")
                break
            password = input("请输入您的密码：")
            with open(file="name.txt", mode="r+", encoding="utf-8")as r:
                t = r.readlines()
                lines = []
                user = ""
                s = [x.strip() for x in t if x.strip() != '']
                for i in s:
                    y = i.split(",")
                    lines.append(y)
                for j in lines:
                    if j[0] == username:
                        user = j[0]
                        if j[1] == password:
                            print("登录成功")
                            r.close()
                            break
                # 根据输入内容，选择打印结果
                if user == username:
                    print("请输入正确的密码")
                else:
                    print("输入错误，没有该用户！")

    def alter(self):
        while True:
            username = input("请输入您的用户名：")
            if username == "q":
                print("谢谢使用")
                break
            password = input("请输入您的密码：")
            with open(file="name.txt", mode="r+", encoding="utf-8")as r:
                t = r.readlines()
                lines = []
                user = ""
                s = [x.strip() for x in t if x.strip() != '']
                for i in s:
                    y = i.split(",")
                    lines.append(y)
                for j in lines:
                    if j[0] == username:
                        user = j[0]
                        pass_word = j[1]
                        if j[1] == password:
                            while True:
                                user_p = input("请输入您的新密码：")
                                user_r = input("请再次输入密码：")
                                if user_p == user_r:
                                    with open(file="name.txt", mode="w", encoding="utf-8")as w:
                                        j[1] = user_p
                                        for j in lines:
                                            w.write("{},{},{},{},{},{}\n".format(j[0], j[1], j[2], j[3], j[4], j[5]))
                                    break
                                else:
                                    print("两次密码输入不一致请重新输入")

                # 根据输入内容，选择打印结果
                if user == username and pass_word == password:
                    print("修改密码成功！")
                    r.close()
                    w.close()
                elif user == username:
                    print("请输入正确的密码")
                else:
                    print("输入错误，没有该用户！")

# if __name__ == "__main__":
#     Z = Record()
#
#
#     def interface():
#         print("****************************************************")
#         print("*         开户（1）            登录（2）              *")
#         print("*                   修改密码（3）                    *")
#         print("*                    退出（q）                       *")
#         print("****************************************************")
#
#
#     while True:
#         interface()
#         behavior = input("请选择您要办理的业务")
#         chose = input("请输入您的业务：")
#         if chose == "1":
#             Z.adduser()
#         elif chose == "2":
#             Z.log()
#         elif chose == "3":
#             Z.alter()
#         elif chose == "6":
#             print("欢迎下次光临！")
#             break
#         else:
#             print("输入错误！请重新输入！")

# 魔法成绩求和
# with open(file="scores.txt", mode="r+",encoding="utf-8")as r:
#     t = r.readlines()
#     lines = []
#     Q = ""
#     s = [x.strip() for x in t if x.strip() != '']
#     for i in s:
#         y = i.split(" ")
#         lines.append(y)
#     with open(file="d:\python\success.text", mode="w", encoding="utf-8")as w:
#         total = 0
#         for j in lines:
#             for l in range(1,len(j)):
#                 total += int(j[l])
#             w.write("{}的魔法作业总成绩:{}\n".format(j[0],total))
#             total = 0
#         w.flush()
#         w.close()
#     r.close()
