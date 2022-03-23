from lxml import etree
import os
import requests
import re
import sys
from urllib.parse import urljoin
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'https://situ.tw/'
## 用來保持網路連線的
rs = requests.session()
# 用 requests 抓取網頁並存在 response
response = rs.get(url,verify = False)
print(response)
html = response.text
page = etree.HTML(html)
print(html)
print(page)
import time


url = 'https://www.sto.cx/serial/mslist.aspx'
url_book = 'https://www.sto.cx/mbookintro-177024.html'
url_book1 = 'https://www.sto.cx/book-72612-1.html'
# https://www.sto.cx/book-26886-1.html
## 用來保持網路連線的
rs = requests.session()
# 用 requests 抓取網頁並存在 response
response = rs.get(url_book1,verify = False)
print(response)
html = response.text
page = etree.HTML(html)

def get_Book(url_book,List = []):
    # url_book = 'https://www.sto.cx/book-135748-1.html'
    ## 用來保持網路連線的
    rs = requests.session()
    # 用 requests 抓取網頁並存在 response
    response = rs.get(url_book,verify = False)
    print(response)
    html = response.text
    page = etree.HTML(html)

    # print(html)
    # print(page)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # 透過指定的瀏覽器 driver 打開 Chrome
    driver = webdriver.Chrome()
    # 將瀏覽器視窗最大化
    driver.maximize_window()
    driver.get(url_book)
    a =[]
    a = (driver.find_element_by_xpath('//*[@id="Page_select"]').text).split('\n')
    page_num = int(len(a))
    for i in range(1,int(len(a))):
        content = driver.find_element_by_xpath('//*[@id="BookContent"]').text 
        time.sleep(2)
        List.append(content)
        button = driver.find_elements_by_xpath('//*[@id="webPage"]/a[11]')[0]
        button.click()
    driver.close()   
    return(List)
    
txt = []
url_book = 'https://www.sto.cx/book-73759-1.html'
get_Book(url_book,txt)

import csv 
with open("冰與火之歌-魔龍的狂舞.txt", "w",encoding = 'utf8') as file:
    file.write("\n".join(txt))