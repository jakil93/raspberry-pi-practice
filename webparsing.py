#coding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import time
phantomPath = "C:\\Users\\it\\OneDrive\\for myself\\PhantomJS 2.1.1\\bin\\phantomjs.exe"
chromPath = "C:\\Users\\it\\OneDrive\\for myself\\ChromDriver 2.9\\chromedriver.exe"
#driver = webdriver.PhantomJS(executable_path=phantomPath)
driver = webdriver.Chrome(executable_path=chromPath)
driver.get("http://bus.busan.go.kr/busanBIMS/default.asp")
print driver.page_source

