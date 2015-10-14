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


def extract_general_data(page):
    soup = BeautifulSoup(page)
    allData = []
    totTournaments = []
    lyTournamentsNoTurbo = []
    
    if page.find('Profit') < 0:
        return None,None
    divs = soup.findAll('div', attrs={'class': 'b-profile__column'})
    for d in divs:

        if ('Profit All time' in d.text)&('During his career' in d.text):
            dts = d.findAll('dt')
            for val in dts:
                values = val.find(text=True)
                totTournaments.append(values)
#            break
        if ('excluding large field' in d.text):
            dts = d.findAll('dt')
            for val in dts:
                values = val.find(text=True)
                lyTournamentsNoTurbo.append(values)
#            break
#        allData.append(totTournaments)
#        allData.append(lyTournamentsNoTurbo)
        
    return totTournaments, lyTournamentsNoTurbo
    
    
data_pd = pd.read_csv('data13102015\\pusers14102015.csv', encoding="utf8")

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

driver = webdriver.Firefox()
#driver.get(user)
usersInfo = []
for i in range(len(data_pd)):
#    print('started cycle')
    if (np.isnan(data_pd['tournaments'][i])):
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
  
    if np.isnan(data_pd['tot_tournaments'][i]):     
#        print('find with None values')
        url = data_pd['link'][i]+'/stats'
        driver.get(url)
        
        infoT, infoLY = extract_general_data(driver.page_source)
        
        if (type(infoT) == list):
            data_pd['tot_tournaments'][i]=int(infoT[0])
            data_pd['tot_avFieldSize'][i]=float(infoT[1])
            data_pd['tot_avBI'][i]=float(infoT[2])
            data_pd['tot_profit'][i]=float(infoT[3])
            data_pd['tot_avROI'][i]=float(infoT[4])
            data_pd['tot_totROI'][i]=float(infoT[5])
        if (type(infoLY) == list):#&(len(infoLY)>0)
            data_pd['ly_tournaments'][i]=int(infoLY[0])
            data_pd['ly_avFieldSize'][i]=float(infoLY[1])
            data_pd['ly_avBI'][i]=float(infoLY[2])
            data_pd['ly_profit'][i]=float(infoLY[3])
            data_pd['ly_avROI'][i]=float(infoLY[4])
            data_pd['ly_totROI'][i]=float(infoLY[5])
#    usersInfo.append([infoT,infoLY])
#    
data_pd.to_csv("data13102015\\pusers14102015.csv", encoding='utf8', index=False)

