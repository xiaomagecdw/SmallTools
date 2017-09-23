# coding:utf-8
'''
Created on 2017年9月23日

@author: chendaiwu
'''

from selenium import webdriver
import xlwt
import time
import re

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(2)
pages = driver.page_source

workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('xxx', cell_overwrite_ok=True)

n = 0
url_list = re.findall('href=\"(.*?)\"', pages, re.S)

for url in url_list:
    if "http" in url:
        print url
        sheet1.write(n, 0, url)
        n = n + 1
workbook.save("getUrl.xls")







