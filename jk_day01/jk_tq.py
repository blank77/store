import requests,xlwt,xlrd
from bs4 import BeautifulSoup

provinces = ["hebei","beijing","shanghai","tianjin","chongqing","qinghai","shanxi","neimenggu","xinjiang","gansu","guangdong","fujian","taiwan","hainan","ningxia","henan","shandong","sanxi","anhui","hubei","heilongjiang","jilin","liaoning","hunan","jiangsu","sichuan","guizhou","yunnan","guangxi","xizang","zhejiang","jiangxi","xianggang","aomen"]
w = book = xlwt.Workbook(encoding='utf-8',style_compression=0)
k = 0
for i in provinces:
    sheet = book.add_sheet(i, cell_overwrite_ok=True)
    # 目标url
    url = 'http://flash.weather.com.cn/wmaps/xml/{}.xml'.format(i)
    # 获取网页源代码
    resp = requests.get(url)
    html = resp.content.decode('utf-8')
    # 数据提取
    soup = BeautifulSoup(html, 'html.parser')
    tr_list = soup.find_all()
    for j in tr_list:
        o = str(j)
        sheet.write(k,0,o)
        k+=1
    k = 0
w.save("天气.xls")
