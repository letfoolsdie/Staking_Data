# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:33:26 2015

@author: Nikolay_Semyachkin
"""
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import time

###CREATE FUNCTION TO EVALUATE STAKER'S PROFIT AT STAKEBACK DEALS:
#df.stakersProfit[np.isnan(df.coef)]   

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


data_pd = pd.read_csv("data15102015\it1-11_DONE_id.csv", encoding="utf8")

#driver = webdriver.Chrome('D:\Data Science\Poker staking data\chromedriver.exe')

#for i in range(len(data_pd)):
#    if (np.isnan(data_pd['BI_actual'][i]) & (np.isnan(data_pd['cashes'][i]))):
#        url = data_pd['item_info'][i]
#        driver.get(url)
#        time.sleep(0.5)
#        info = extract_data(driver.page_source)
#        if type(info) == list:
#            data_pd['BI_actual'][i] = info[2]
#            data_pd['cashes'][i] = info[3]
#
#
#
#data_pd.to_csv("data15102015\it1-11_DONE_id.csv", encoding="utf8", index=False)

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
#users = data_pd
#users.drop_duplicates(subset='usr_name',inplace=True)
#users.to_csv("data15102015\pusers_it1-11_DONE_id.csv", encoding="utf8")