# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:42:25 2015

@author: Nikolay_Semyachkin
"""

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver

def extract_data(page):
    soup = BeautifulSoup(page)
    if page.find('Profit') < 0:
        return 0
    data = soup.findAll('dt')#('dl', attrs={'class': 'b-stats__item'})
    r = []
    for val in data:
        values = val.find(text=True)
        r.append(values)
    return r
#    data = []
#    for tr in rows[1:]:
#        r = []
#        cols = tr.findAll('td')
#        for td in cols:
#            if ('right' in td['class']) & ('i' in td['class']): 
#                text = td.find(text=True)
#                r.append(text)
#        if len(r) > 0:
#            return r
#    return 0
data_pd = pd.read_csv("wtf_users1.csv", encoding="utf8")

driver = webdriver.Firefox()
#driver.get(user)
usersInfo = []
for i in range(len(data_pd)):
    if (data_pd['tournaments'][i] == 0) & (data_pd['roi'][i] == 0):
        url = data_pd['link'][i]
        driver.get(url)
        info = extract_data(driver.page_source)
        if type(info) == list:
            data_pd['profit'][i]=float(info[0][:-1])
            data_pd['totBI'][i]=float(info[1][:-1])
            data_pd['totCashes'][i]=float(info[2][:-1])
            data_pd['roi'][i]=float(info[3][:-1])
            data_pd['roiBI'][i]=float(info[4][:-1])
            data_pd['tournaments'][i]=int(info[5])
            data_pd['abi'][i]=float(info[6][:-1])
            data_pd['itm'][i]=float(info[7][:-1])
#        usersInfo.append(info)
    
#    
data_pd.to_csv('wtf_users1.csv', encoding='utf8', index=False)

