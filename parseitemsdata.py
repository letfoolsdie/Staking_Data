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
data_pd = pd.read_csv("wtf.csv", encoding="utf8")
#data_pd['BI_actual'] = 0
##data_pd['Cashes'] = 0
#data_pd = data_pd[(data_pd.status != 'On sale') & (data_pd.status != 'Sold out')]
#data_pd = data_pd[data_pd.coef.notnull()]

#toWorkWith = data_pd.loc[(data_pd['BI_actual']==0) & (data_pd['Cashes']==0)]
driver = webdriver.Firefox()
#driver.implicitly_wait(1)


for i in range(2500):
    if (data_pd['BI_actual'][i] == 0) & (data_pd['Cashes'][i] == 0):
        url = data_pd['item_info'][i]
        driver.get(url)
        info = extract_data(driver.page_source)
        if type(info) == list:
            data_pd['BI_actual'][i] = info[2]
            data_pd['Cashes'][i] = info[3]

#urls = list(data_pd.item_info)
#driver = webdriver.Firefox()
#driver.implicitly_wait(2)
#    
#info = []
#for url in urls:
#    driver.get(url)
#    info.append(extract_data(driver.page_source))
#    
#    driver.close()
    

data_pd.to_csv("wtf.csv", encoding="utf8", index=False)

