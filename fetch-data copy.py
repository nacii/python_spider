# -*-coding:utf-8 -*-
import re
import urllib
from urllib import request as urllib2
import requests
from bs4 import BeautifulSoup
import pandas
from unidecode import unidecode

# 读取excel表格
filepath = 'C:/Users/xia.yan/Desktop/Chemical/k02.xlsx'
sheet1 = "Sheet1"
data = pandas.read_excel(filepath,sheet_name = sheet1)
#print(data)

#需要爬取的网页
url = "http://www.safe.gov.cn/safe/rmbhlzjj/index.html"

#伪装成浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'}

#获取网页
# params = {"show_ram":1}
# response = requests.get(url=url, params=params, headers=headers)
#content.decode("utf-8")

request1 = urllib2.Request(url, headers=headers)
source_code = urllib2.urlopen(request1).read()
str_utf8 = str(source_code)
# byte_utf8 = str_utf8.encode('unicode_escape')
byte_utf8 = str_utf8.encode('utf-8')
decode_utf8 = byte_utf8.decode('utf-8').replace('\\x', '%')
plain_text = urllib.parse.unquote(decode_utf8)
print(plain_text)
# print(response.text)
#response = requests.get(url,params=params, headers=headers)#访问url
# 获取网页源代码
soup = BeautifulSoup(plain_text)
print(type(soup))
#tr = soup.find('tr',class_='table-tbody-item')
#table = soup.find('table',class_ = 'list')
# list_soup = soup.find('div', {'class': 'mod book-list'})
table = soup.find('table',{'class': 'list'})
print(table)

# try_times += 1;
# if table==None and try_times<200:
#     continue



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
