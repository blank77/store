from DBUtils import *

'''
    任务1：工商系统改造
    任务2：excel与数据库转换工具
        excel_to_db()
        db_to_excel()
'''
# sql = "update  person set salary = salary + %s"
# param = [2000]
#
# update(sql,param)
#
# sql = "select * from person where age > %s"
# param = [30]
# data = select(sql,param,mode="many",size=3)
# print(data)
import pymysql
import xlwt
import xlrd
#连接数据库
def getConn(database):
    args = dict(
        host='localhost',
        user='root',
        passwd='root',
        db=database,
        charset='utf8'
    )
    #**arges把关键参数送入字典里
    conn = pymysql.connect(**args)
    #返回conn
    return conn

#定义mysql数据库数据转换为execl格式文件
def db_to_excel(database='bank', table='bank', excelResult=''):
    #连接数据库
    conn = getConn(database)
    cursor = conn.cursor()
    #格式化
    cursor.execute("select * from {}".format(table))
    data_list = cursor.fetchall()
    # 创建一个workbook 设置编码
    excel = xlwt.Workbook(encoding = 'utf-8')
    #创建一个execl表
    sheet = excel.add_sheet("sheet1")
    #获取数据库行长度
    row_number = len(data_list)
    #得到列的长度
    column_number = len(cursor.description)
    #通过for遍历写入数据
    for i in range(column_number):
        sheet.write(0, i, cursor.description[i][0])
    for i in range(row_number):
        for j in range(column_number):
            sheet.write(i + 1, j, data_list[i][j])
    #规定excel名称
    excelName = "mysql_{}_{}.xls".format(database, table)
    if excelResult != '':
        excelName = excelResult
    #保存
    excel.save(excelName)

#代码入口
# if __name__ == "__main__":
#     db_to_excel("bank", "bank")




def excel_to_db(excelName, database='bank', table='ICBC'):
    #获取到excel中的字段和数据
    excel = xlrd.open_workbook(excelName,encoding_override=True)
    # 打开您要操作的选项卡
    sheet = excel.sheet_by_index(0)
    # 获取行数
    row_number = sheet.nrows
    # 获取列数
    column_number = sheet.ncols
    #获取行的数据
    field_list = sheet.row_values(0)
    data_list = []
    #把excel的值添加给data_list
    for i in range(1, row_number):
        data_list.append(sheet.row_values(i))
    #连接数据库
    conn = getConn(database)
    cursor = conn.cursor()
    # 格式化数据库
    #删除原有同名数据库表
    drop_sql = "drop table if exists {}".format(table)
    cursor.execute(drop_sql)
    create_sql = "create table {}(".format(table)
    #:-1除了最后一个取全部，-1取最后一个元素
    #根据字段创建表，根据数据执行插入语句
    for field in field_list[:-1]:
        create_sql += "{} varchar(50),".format(field)
    create_sql += "{} varchar(50))".format(field_list[-1])
    # 创建数据库表
    cursor.execute(create_sql)
    for data in data_list:
        new_data = ["'{}'".format(i) for i in data]
        insert_sql = "insert into {} values({})".format(table, ','.join(new_data))
        #添加数据到表
        cursor.execute(insert_sql)
    # 提交数据到数据库
    conn.commit()
    # 关闭资源
    cursor.close()
    conn.close()

#代码入口
# if __name__ == '__main__':
#     excel_to_db("mysql_bank_bank.xls")

