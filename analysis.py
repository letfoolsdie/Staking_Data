# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:46:12 2015

@author: Nikolay_Semyachkin
"""

import pandas as pd

df = pd.read_csv('staking_nodp.csv')

#df = df[(df.status != 'On sale') & (df.status != 'Sold out')]
#df.drop_duplicates(subset=['link', 'usr_name', 'start_date', 'BI', 'tournaments', 'coef',\
# 'stakeback', 'player_part', 'sell_left', 'status'], inplace=True)
# 
#df.status = df.status.astype(float)


df = df[df.coef.notnull()]

df['ABI'] = df.BI / df.tournaments
df['stakers_profit'] = (df.status - (df.BI * (df.coef - 1))) * ((100 - df.player_part - df.sell_left)/100)
