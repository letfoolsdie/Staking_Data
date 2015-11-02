# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:53:13 2015

@author: Nikolay_Semyachkin
"""
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import time


def getrooms(page,user):
    soup = BeautifulSoup(page)
#    if page.find('Total') < 0:
#        return 0
    rooms = soup.find('ul', attrs={'class': 'b-profile__sidebar__list'})
    rows = rooms.findAll('li')
#    data = []
    r = []
    result = [None]*10
    for n in rows:
        
        text = n.findAll(text=True)
        text = user +text[2]+text[0]
        r.append(text)
    if len(r) > 0:
        result[:len(r)-1]=r
        return result
    return 0

driver = webdriver.Chrome('D:\Data Science\Poker staking data\chromedriver.exe')
#driver.get("https://mttmarket.com/users/55dc7e4f61ccb6107dc36ba1/info")
df = pd.read_csv('data15102015/pusers_it1-11_DONE_id.csv',encoding='utf8')
data_pd = df[['link','usr_name']]
#s = getrooms(driver.page_source,'shonix')
#cols = ['mttmarket', 'r1','r2','r3','r4','r5','r6','r7','r8','r9','r10']
#d = pd.DataFrame(s,columns=cols)
#print(s)
#
#df = pd.read_csv('pusers_.csv',encoding='utf8')
users = []

for i in range(311,len(data_pd)):
    url = data_pd['link'][i]
    driver.get(url)
    time.sleep(0.5)
    soup = BeautifulSoup(driver.page_source)
    rooms = soup.find('ul', attrs={'class': 'b-profile__sidebar__list'})
    rows = rooms.findAll('li')
    r = []
    for n in rows:
        text = n.findAll(text=True)
        text = [data_pd['usr_name'][i],text[2],text[0]]
        users.append(text)
#    users.append(r)
cols = ['mttmarket','roomNick','room']
dd = pd.DataFrame(users,columns=cols)
#dd.to_csv('roomnames.csv')
#dd.to_csv('roomnames1.csv',encoding='utf8')

