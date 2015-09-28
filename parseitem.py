# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:35:19 2015

@author: Nikolay_Semyachkin
"""
import pandas as pd
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("item_details.html", encoding="utf8"))
table = soup.find('table', attrs={'class': 'b-exchange-table'})
rows = table.findAll('tr')
data = []
for tr in rows[1:]:
    r = []
    cols = tr.findAll('td')
    for td in cols:
        if ('right' in td['class']) & ('i' in td['class']): 
            text = td.find(text=True)
            r.append(text)
    if len(r) > 0:
        data.append(r)