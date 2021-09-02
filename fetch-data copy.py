# -*-coding:utf-8 -*-
import re
import urllib
from urllib import request as urllib2
import requests
from bs4 import BeautifulSoup
import pandas

# 读取excel表格
# filepath = 'C:/Users/xia.yan/Desktop/Chemical/k02.xlsx'
# sheet1 = "Sheet1"
# data = pandas.read_excel(filepath,sheet_name = sheet1)
#print(data)

#需要爬取的网页
url = "http://www.safe.gov.cn/AppStructured/hlw/RMBQuery.do"

#伪装成浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'}

#获取网页
# params = {"show_ram":1}
# response = requests.get(url=url, params=params, headers=headers)
#content.decode("utf-8")

request1 = urllib2.Request(url, headers=headers)
source_code = urllib2.urlopen(request1).read()

###utf-8字符串转码为真正的字符串
'''
str_utf8 = str(source_code)
print(str_utf8)
# byte_utf8 = str_utf8.encode('unicode_escape')
byte_utf8 = str_utf8.encode('utf-8')
decode_utf8 = byte_utf8.decode('utf-8').replace('\\x', '%')
plain_text = urllib.parse.unquote(decode_utf8)
print(plain_text)
'''
###
# print(response.text)
#response = requests.get(url,params=params, headers=headers)#访问url
# 获取网页源代码
soup = BeautifulSoup(source_code)
# print(type(soup))
#tr = soup.find('tr',class_='table-tbody-item')
#table = soup.find('table',class_ = 'list')
# list_soup = soup.find('div', {'class': 'mod book-list'})
table = soup.find('table',{'class': 'list'})
# print(table)
th_list = table.find_all('th', class_ = 'table_head')  #th_list是一个列表[]
th_text = []
for th in th_list:
    th = th.get_text().strip() #抽取文本
    th_text.append(th) #标题文本存入列表
print(*th_text,"\t") #打印列表所有内容,元素之间用制表符\t连接


tr_list = table.find_all('tr', class_ = 'first')
for tr in tr_list:
    # tr_first = table.find('tr', class_ = 'first')
    td_list = tr.find_all('td')
    td_text = []
    for td in td_list:
        td = td.get_text().strip()
        td_text.append(td)
    print(*td_text, "\t")
    
# print(tr.get_text().replace("space", "").replace("\n", "").replace("\r", "").replace("\t", ""))
# td = tr.find('td',class_ = 'tbody1')
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
