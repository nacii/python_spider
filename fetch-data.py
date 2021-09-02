import re
import requests
from bs4 import BeautifulSoup
import pandas

# 读取excel表格
filepath = 'C:/Users/xia.yan/Desktop/Chemical/k01.xlsx'
sheet1 = "Sheet1"
data = pandas.read_excel(filepath,sheet_name = sheet1)
#print(data)

#需要爬取的网页
url = "https://quote.21cp.com/basic_centre/detail/158863415916396544--.html?quotedPriceDateStart=2018-08-31&quotedPriceDateEnd=2021-08-31&isList=1"
#获取的cookie
cookie = "_uab_collina=163029100278744888442666; quoteCentreIndex=36c3fff5; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22150911600444833792%22%2C%22first_id%22%3A%2217b94ea836b327-0dd575580351b2-7068776a-672195-17b94ea836c971%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217b94ea836b327-0dd575580351b2-7068776a-672195-17b94ea836c971%22%7D; ZSREM=MTYzMDk5Nzg2OHxsb25nfDYwNDgwMHxzdW1pdG9tb3wxNDQ3MjU1MTI2ODQ1ODA4NjR85Lit5aGR6buE6YeR5Lya5ZGYfDE1NTA5MTU5Mjg3NTYxODMwNHzkuK3loZHpu4Tph5HkvJrlkZh8MTUwOTExNjAwNDQ0ODMzNzkyfHhpYW9mZW5nLmRlbmd86YKT5bCP5Yek; ZSREM_LEGACY=MTYzMDk5Nzg2OHxsb25nfDYwNDgwMHxzdW1pdG9tb3wxNDQ3MjU1MTI2ODQ1ODA4NjR85Lit5aGR6buE6YeR5Lya5ZGYfDE1NTA5MTU5Mjg3NTYxODMwNHzkuK3loZHpu4Tph5HkvJrlkZh8MTUwOTExNjAwNDQ0ODMzNzkyfHhpYW9mZW5nLmRlbmd86YKT5bCP5Yek; zsArea=%7B%22areaCode%22%3A%22310000%22%2C%22areaName%22%3A%22%E4%B8%8A%E6%B5%B7%E5%B8%82%22%2C%22longitude%22%3A%22121.472644%22%2C%22latitude%22%3A%2231.231706%22%7D; Hm_lvt_5f657133fe3a739c5dfcc2e306267320=1630291003,1630373243,1630393001; Hm_lpvt_5f657133fe3a739c5dfcc2e306267320=1630393001; ssxmod_itna=iqfx2DyDRD9AqY5GHqwn0DuDGoqgkkQkqb3HDlOiYxA5D8D6DQeGTb2qDBjOUEi7wteA4Ig4hQec27GfxY7A3mu7QLfAhooDU4i8DCduo1bDeW=D5xGoDPxDeDADYo0DAqiOD7qDdXLvvz2xGWDmRkDWPDYxDrXpKDRxi7DDydzx07DQyktj2kQSPmBhE1O0AxKlKD9EoDsrGLsbgL2UhsQz8f2AD4DB+4kBLxhBLtSi0DP+b8DlFuDCIzBZ577SLCDUHhIBnqbnw4ppx3+vhtZfu5QirfkiDR=GiMOiDqeG0DrCxBlkDDiOhz7DxD==; ssxmod_itna2=iqfx2DyDRD9AqY5GHqwn0DuDGoqgkkQkqb3D618DEGGD0v2I+x03q8cL6YvDw6gPGcDY9KxD"

#伪装成浏览器
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
# }
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'}

#爬虫[Requests设置请求头Headers],伪造浏览器

#cookie切片
cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}
#获取网页
params = {"show_ram":1}
response = requests.get(url=url, params=params, headers=headers, cookies=cookie_dict)
#content.decode("utf-8")
print(response.status_code)
#response = requests.get(url,params=params, headers=headers)#访问url

soup = BeautifulSoup(response.text, 'html.parser')#获取网页源代码
print(type(soup))
#tr = soup.find('tr',class_='table-tbody-item')
table = soup.find('table',class_ = 'db-table-content')
print(table)
tr = table.find('tr', class_ = 'table-tbody-item')
print(tr)
td = tr.find('td',class_ = 'tbody1')
print(td.get_text().strip())
#.find_all('td')
#.find定位到所需数据位置  .find_all查找所有的tr（表格）




# 去除标签栏
# listData = [] #定义数组
# for column in td[0:]:        #tr2[1:]遍历第1列到最后一列，表头为第0列
#     td = column.find_all('td')#td表格
#     day = td[0].get_text().strip()           #遍历日期
#     price = td[1].get_text().strip()  #遍历城市
#     listData.append([day,price])
# print (listData)#打印
