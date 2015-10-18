# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:18:22 2015

@author: Nikolay_Semyachkin
"""
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
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

data_pd = pd.read_csv('data15102015\it1-11_final.csv', parse_dates=True, dayfirst=True)
#soup = BeautifulSoup(open("data15102015\it1.htm", encoding="utf8"))


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

#rec = pd.concat([df,df1,df2,df3])
#rec.drop_duplicates(subset='item_info',inplace=True)


##ADDING FIELD FOR FINAL VERSION:

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

data_pd.to_csv('data15102015\it1-11_DONE.csv', encoding="utf8", index=False)





