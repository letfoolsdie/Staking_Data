# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:33:26 2015

@author: Nikolay_Semyachkin
"""
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

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


data_pd = pd.read_csv("data13102015\data131015_2it.csv", encoding="utf8")

#toWorkWith = data_pd.loc[(data_pd['BI_actual']==0) & (data_pd['Cashes']==0)]
driver = webdriver.Firefox()
#driver.implicitly_wait(1)


for i in range(len(data_pd)):
    if (data_pd['BI_actual'][i] == 0) & (data_pd['Cashes'][i] == 0):
        url = data_pd['item_info'][i]
        driver.get(url)
        info = extract_data(driver.page_source)
        if type(info) == list:
            data_pd['BI_actual'][i] = info[2]
            data_pd['Cashes'][i] = info[3]
#
#data_pd['profit'] = np.nan
#data_pd['totBI']= np.nan
#data_pd['totCashes']= np.nan
#data_pd['roi']= np.nan
#data_pd['roiBI']= np.nan
#data_pd['tournaments']= np.nan
#data_pd['abi']= np.nan
#data_pd['itm']= np.nan
#
#data_pd['tot_tournaments']= np.nan
#data_pd['tot_avFieldSize']= np.nan
#data_pd['tot_avBI']= np.nan
#data_pd['tot_profit']= np.nan
#data_pd['tot_avROI']= np.nan
#data_pd['tot_totROI']= np.nan
#
#data_pd['ly_tournaments']= np.nan
#data_pd['ly_avFieldSize']= np.nan
#data_pd['ly_avBI']= np.nan
#data_pd['ly_profit']= np.nan
#data_pd['ly_avROI']= np.nan
#data_pd['ly_totROI']= np.nan

data_pd.to_csv("data13102015\data131015_2it.csv", encoding="utf8", index=False)

