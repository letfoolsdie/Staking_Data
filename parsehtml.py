# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:18:22 2015

@author: Nikolay_Semyachkin
"""
import pandas as pd
from bs4 import BeautifulSoup

def get_num(x):
    return float(''.join(ele for ele in x if ele.isdigit() or ele == '.'))

soup = BeautifulSoup(open("MttMarket.html", encoding="utf8"))
table = soup.find('table', attrs={'class': 'b-exchange-table'})
rows = table.findAll('tr')
data = []
for tr in rows[1:]:
    r = []
    cols = tr.findAll('td')
    for td in cols:
        if 'player' in td['class']:
            r.append(td.find('a', href=True)['href'])
        if 'link' in td['class']:
            r.append(td.find('a', href=True)['href'])
        text = td.find(text=True)
        r.append(text)
    data.append(r)

cols = ['link', 'usr_name', 'start_date', 'BI', 'tournaments', 'coef', 'stakeback', 'player_part', 'sell_left', 'status', 'item_info','shit']
#data.insert(0,cols)

for i in data:
    if 'Loss' in i[-3] or 'Profit' in i[-3]:
        kef = 1 if 'Profit' in i[-3] else -1
        i[-3] = get_num(i[-3])*kef



data_pd = pd.DataFrame(data, columns=cols)
#del data_pd['shit']

data_pd.drop_duplicates(subset=cols, inplace=True)
data_pd.to_csv('staking_small_w_links.csv', encoding="utf8")




