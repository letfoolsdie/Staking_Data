# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:46:12 2015

@author: Nikolay_Semyachkin
"""

import pandas as pd

df = pd.read_csv('wtf.csv')

#df = df[(df.status != 'On sale') & (df.status != 'Sold out')]
#df.drop_duplicates(subset=['link', 'usr_name', 'start_date', 'BI', 'tournaments', 'coef',\
# 'stakeback', 'player_part', 'sell_left', 'status'], inplace=True)
# 
#df.status = df.status.astype(float)


#df = df[df.coef.notnull()]
vv = df.columns.values
vv[15]='cashes'
df.columns=vv

df['ABI'] = df.BI / df.tournaments
df['stakersProfit'] = (df.cashes - df.BI_actual*df.coef)* \
((100-df.player_part-df.sell_left)/100)

df['playersProfit'] = (df.cashes-df.BI_actual*(2-df.coef))* \
((df.player_part+df.sell_left)/100)
