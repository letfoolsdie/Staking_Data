# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:18:22 2015

@author: Nikolay_Semyachkin
"""
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib
matplotlib.style.use('ggplot')

def get_num(x):
    return float(''.join(ele for ele in x if ele.isdigit() or ele == '.'))



def buildGraph(df):
    ts = df[['start_date', 'status']]
    ts.start_date = pd.to_datetime(ts.start_date, format="%d.%m.%Y")
    ts = ts.groupby(['start_date']).sum()
    #ts = ts.sort(columns='start_date')
    ts.status = ts.status.cumsum()
    ts.plot()

rec = pd.read_csv('data15102015\combined_it1-8-js.csv', parse_dates=True, dayfirst=True)
#soup = BeautifulSoup(open("data15102015\it1.htm", encoding="utf8"))
#soup1 = BeautifulSoup(open("data15102015\it2.htm", encoding="utf8"))
#soup2 = BeautifulSoup(open("data15102015\it5.htm", encoding="utf8"))
#soup3 = BeautifulSoup(open("data15102015\it_js.html", encoding="utf8"))
#soup4 = BeautifulSoup(open("data15102015\it4.htm", encoding="utf8"))
#soup5 = BeautifulSoup(open("data15102015\it5.htm", encoding="utf8"))
#soup6 = BeautifulSoup(open("data15102015\it7.html", encoding="utf8"))
#soup7 = BeautifulSoup(open("data15102015/1710-it8.html"))
soup8 = BeautifulSoup(open("data15102015/1710-it9.html"))

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
#    
#df = buildDataframe(soup)
#df1 = buildDataframe(soup1)
#df2 = buildDataframe(soup2)
#df3 = buildDataframe(soup3)
#df4 = buildDataframe(soup4)
#df5 = buildDataframe(soup5)
#df6 = buildDataframe(soup6)
#df7 = buildDataframe(soup7)
df8 = buildDataframe(soup8)

#rec = pd.concat([df,df1,df2,df3])
#rec.drop_duplicates(subset='item_info',inplace=True)


###DEBUG: BUILD GRAPH:


#df1 = df1[(df1.status!='On sale') & (df1.status!='Sold out')]

#df2 = buildDataframe(soup2)
#df2 = df2[(df2.status!='On sale') & (df2.status!='Sold out')]

#df = pd.DataFrame(data, columns=cols)
#del data_pd['shit']
#
#data_pd.drop_duplicates(subset=cols, inplace=True)
#data_pd['BI_actual'] = 0.0
#data_pd['Cashes'] = 0.0
#
#data_pd.to_csv('data13102015\data131015_1it.csv', encoding="utf8")




