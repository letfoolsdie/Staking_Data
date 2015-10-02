# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:42:25 2015

@author: Nikolay_Semyachkin
"""

import pandas as pd
import mumpy as np
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

user = 'https://mttmarket.com/users/55eebec761ccb65540d2383a'

