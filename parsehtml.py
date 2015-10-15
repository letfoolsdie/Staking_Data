# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:18:22 2015

@author: Nikolay_Semyachkin
"""
import pandas as pd
from bs4 import BeautifulSoup

def get_num(x):
    return float(''.join(ele for ele in x if ele.isdigit() or ele == '.'))

soup = BeautifulSoup(open("data15102015\MttMarket.htm", encoding="utf8"))
soup1 = BeautifulSoup(open("data13102015\MttMarket.htm", encoding="utf8"))
soup2 = BeautifulSoup(open("alldata_220915-1726\MttMarket.htm", encoding="utf8"))
def buildDataframe(soup):

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
    
    cols = ['link', 'usr_name', 'start_date', 'BI', 'tournaments', 'coef', \
    'stakeback', 'player_part', 'sell_left', 'status', 'item_info','shit']
    
    
    for i in data:
        if 'Loss' in i[-3] or 'Profit' in i[-3]:
            kef = 1 if 'Profit' in i[-3] else -1
            i[-3] = get_num(i[-3])*kef
            
    df = pd.DataFrame(data, columns=cols)
#    df = df[(df.status!='On sale') & (df.status!='Sold out')]
#    df.drop_duplicates(inplace=True)
    df.drop_duplicates(subset='item_info',inplace=True)
    return df
    
df = buildDataframe(soup)

df1 = buildDataframe(soup1)
#df1 = df1[(df1.status!='On sale') & (df1.status!='Sold out')]

df2 = buildDataframe(soup2)
df2 = df2[(df2.status!='On sale') & (df2.status!='Sold out')]

#df = pd.DataFrame(data, columns=cols)
#del data_pd['shit']
#
#data_pd.drop_duplicates(subset=cols, inplace=True)
#data_pd['BI_actual'] = 0.0
#data_pd['Cashes'] = 0.0
#
#data_pd.to_csv('data13102015\data131015_1it.csv', encoding="utf8")




