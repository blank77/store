'''
    excel表格的数据统计和分析：
    1.联网安装 xlrd(读取) xlwt(写入)
    xlrd(1.2)
        cmd  -->  python  -m pip  install   xlrd==0.9.3
    2.写代码
        2.1 导入这个工具
            import  xlrd
        2.2 打开工作簿
        2.3 打开选项卡
        2.4 读取数据
任务：
    每个月的销售总金额：
    全年的销售总额：
    每种衣服的销售总额：
    每个季度销售总额占比：
    全年每种销售数量占比：

'''
import xlrd


# 1. 打开工作簿
wd = xlrd.open_workbook("2020年每个月的销售情况.xlsx",encoding_override=True)
sum = 0
down = 0
leather = 0
Jeans = 0
Windbreaker = 0
shirt = 0
cotta = 0
spring = 0
summer = 0
autumn = 0
winter = 0
y_total = 0
# 2.打开您要操作的选项卡
for j in range(0,12):
    st = wd.sheet_by_index(j)
    rows = st.nrows  # 获取行数  # 4
    cols = st.ncols  # 获取列数
    for i in range(1, rows):
        data = st.row_values(i)
        total = data[2] * data[4]
        if data[1] == "羽绒服":
            down = down + data[2] * data[4]
        elif data[1] == "皮草":
            leather = leather + data[2] * data[4]
        elif data[1] == "牛仔裤":
            Jeans = Jeans + data[2] * data[4]
        elif data[1] == "风衣":
            Windbreaker = Windbreaker + data[2] * data[4]
        elif data[1] == "衬衫":
            shirt = shirt + data[2] * data[4]
        elif data[1] == "T血":
            cotta = cotta + data[2] * data[4]
        if j == 0 or j == 1 or j == 2:
            spring = spring + total
        elif j == 3 or j == 4 or j == 5:
            summer = summer + total
        elif j == 6 or j == 7 or j == 8:
            autumn = autumn + total
        elif j == 9 or j == 10 or j == 11:
            winter = winter + total
        sum = sum + total
    print("-----------------------")
    print(j+1,"月销售总额",round(sum,1))
    y_total = y_total +sum
    sum = 0
print("-----------------------")
print("年销售总额",round(y_total,1))
print("-----------------------")
print("羽绒服年销售总额:",round(down,1),"\n","皮草年销售总额:",round(leather,1),"\n","牛仔裤年销售总额:",round(Jeans,1),"\n","风衣年销售总额:",round(Windbreaker,1),"\n","衬衫年销售总额:",round(shirt,1),"\n","T血年销售总额:",round(cotta,1))
print("-----------------------")
print(" 春季总销售占比{:.2%}".format(spring/y_total),"\n","夏季总销售占比{:.2%}".format(summer/y_total),"\n","秋季总销售占比{:.2%}".format(autumn/y_total),"\n","冬季总销售占比{:.2%}".format(winter/y_total))
print("-----------------------")
print(" 羽绒服年销售占比{:.2%}".format(down/y_total),"\n","皮草年销售占比{:.2%}".format(leather/y_total),"\n","牛仔裤年销售占比{:.2%}".format(Jeans/y_total),"\n","风衣年销售占比{:.2%}".format(Windbreaker/y_total),"\n","衬衫年销售占比{:.2%}".format(shirt/y_total),"\n","T血年销售占比{:.2%}".format(cotta/y_total))















