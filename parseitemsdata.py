# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:33:26 2015

@author: Nikolay_Semyachkin
"""
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

def extract_data(page):
    soup = BeautifulSoup(page)
    if page.find('Total') < 0:
        return 0
    table = soup.find('table', attrs={'class': 'b-exchange-table'})
    rows = table.findAll('tr')
#    data = []
    for tr in rows[1:]:
        r = []
        cols = tr.findAll('td')
        for td in cols:
            if ('right' in td['class']) & ('i' in td['class']): 
                text = td.find(text=True)
                r.append(text)
        if len(r) > 0:
            return r
    return 0
#driver = webdriver.Chrome('D:\Data Science\Poker staking data\chromedriver.exe')
data_pd = pd.read_csv("staking_small_w_links.csv", encoding="utf8")
urls = list(data_pd.item_info)
driver = webdriver.Firefox()
driver.implicitly_wait(2)
    
info = []
for url in urls:
    driver.get(url)
    info.append(extract_data(driver.page_source))
    
#    driver.close()
    




#driver.execute_script(open("D:\Data Science\Poker staking data\item_details_files/main.859958b1a89a6bf7dab12dd0e026fd00.js").read())
#html_source = driver.page_source
#


#sleep(5)
#html = driver.execute_script('main.859958b1a89a6bf7dab12dd0e026fd00.js')
#print(html)


