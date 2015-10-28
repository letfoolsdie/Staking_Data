# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:46:12 2015

@author: Nikolay_Semyachkin
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

def splitData(df, percForTest):
    test = df.sample(frac = percForTest)
    train = df.drop(df.index[test.index])
    return train,test


def simulateStrategy(df, starting_bankroll):
#    bank = starting_bankroll
#    df = df[['start_date','stakersProfit','tournaments_x','player_part','BI']]
    df.start_date = pd.to_datetime(df.start_date, format="%d.%m.%Y")
    dol_per_tourn = 1
    df['st_share'] = df.tournaments_x*dol_per_tourn / df.BI
    df['st_share'][df.st_share*100 > 100 - df.player_part] = (100 - df.player_part)/100
    df['bets'] = df.stakersProfit*df.st_share
#    df['iss'] = 1
#    df = df[['bets','start_date']]
    df = df.groupby(['start_date']).sum()
    df.bets = df.bets.cumsum()
    df.bets.plot()
#    df.iss.plot()
    return df
    
    


df = pd.read_csv('data15102015/it1-11_DONE_id.csv', parse_dates=True, dayfirst=True)
#df = pd.read_csv('wtf.csv', parse_dates=True, dayfirst=True)
dfUsers = pd.read_csv('data15102015/pusers_it1-11_DONE_id.csv',encoding='utf8')
#df = df[(df.status != 'On sale') & (df.status != 'Sold out')]
#df.drop_duplicates(subset=['link', 'usr_name', 'start_date', 'BI', 'tournaments', 'coef',\
# 'stakeback', 'player_part', 'sell_left', 'status'], inplace=True)
# 
#df.status = df.status.astype(float)


#df = df[df.coef.notnull()]
#df = df[300:]
#vv = df.columns.values
#vv[15]='cashes'
#df.columns=vv
#
df['ABI'] = df.BI / df.tournaments
#df['coef'] = 1.0
df['addPrice'] = df.BI_actual * (df.coef-1)

df['stakersProfit'] = (df.cashes - df.BI_actual - df.addPrice)*((100-df.player_part-df.sell_left)/100)

df['playersProfit'] = (df.cashes - df.BI_actual)*((df.player_part+df.sell_left)/100)+ \
    df.addPrice*((100-df.player_part-df.sell_left)/100)

##stakers profit for stakeback deals:
#df.stakersProfit[np.isnan(df.coef)] = (df.status - df.status*df.plShare) * ((100-df.player_part-df.sell_left)/100)


#df['newpr'] = df.status - df.addPrice

###BUILD GRAPH WITH TOTAL PROFIT OVER TIME:
#ts = df[['start_date', 'status', 'playersProfit','stakersProfit']]
#ts.start_date = pd.to_datetime(ts.start_date, format="%d.%m.%Y")
#ts = ts.groupby(['start_date']).sum()
##ts = ts.sort(columns='start_date')
#ts.status = ts.status.cumsum()
#ts.playersProfit = ts.playersProfit.cumsum()
#ts.stakersProfit = ts.stakersProfit.cumsum()
###ts.newpr = ts.newpr.cumsum()
###ts.plot(x='start_date',y='status')
#ts.plot()

#BUILD BAR GRAPH FOR 'ABI' vs. 'coef'
#check for coef.value_counts()(!!) for representative numbers
#abiCoef = df[['ABI','coef']]
#abiCoef.groupby(['coef']).mean().plot(kind='bar')


##BUILD TABLE FOR TOP 5 PLAYERS BY CASHES, PLAYER'S PROFIT AND STAKER'S PROFIT
#plSum = df[['usr_name','playersProfit','stakersProfit', 'status','cashes']].groupby('usr_name').sum()
#topCashes = plSum.sort(columns='cashes', ascending=False).head(5)
#topPlProfit = plSum.sort(columns='playersProfit', ascending=False).head(5)
#topStProfit = plSum.sort(columns='stakersProfit', ascending=False).head(10)
#topStatus = plSum.sort(columns='status', ascending=False).head(10)

##PLAYERS WHO WERE PROFITABLE TO STAKER:
#plSum[plSum.stakersProfit>0].sort(columns='stakersProfit')
#
##AVERAGE PROFIT PER DEAL FOR EACH COEFFICIENT:
#x = df[['coef','status']].groupby('coef').sum()
#x['nums'] = df.coef.value_counts()
#x['avrgForCoef']=x.status/x.nums
#x['avrgForCoef'].plot(kind='bar')
#
##COMPARE ROI FOR STAKED TOURNAMENTS AND GENERAL ROI FOR A PLAYER 
#dist = 500
#haveDist = dfUsers[dfUsers.tournaments > dist]
#x = haveDist[haveDist.roi>haveDist.tot_totROI]
#playedBetter = len(x)/len(haveDist)


#PERCENT OF PROFITABLE DEALS:
#Profitable to staker:
#print(len(df[df.stakersProfit>0])/len(df))
##Profitable players (to staker): roi > av.coef:
plSum = df[['usr_name','stakersProfit','coef']].groupby('usr_name')
plSum = plSum.agg({'stakersProfit':np.sum,'coef':np.mean})
#du = pd.merge(dfUsers,plSum,right_index=True, left_on='usr_name')
#du['coef_penalty'] = (du.coef-1)*100
#du = pd.merge(df,plSum,right_index=True, left_on='usr_name')
#s = du[du.roi>du.coef_penalty]
#print(len(s)/len(du))


###Some manual analysis to filter profitable deals
du = pd.merge(df,dfUsers,on='usr_name')
du['coef_penalty'] = (du.coef-1)*100
#sum(du[du.tot_totROI>du.coef_penalty].stakersProfit)
#sum(du[du.tot_totROI>du.coef_penalty+10].stakersProfit)
#sum(du[du.ly_totROI>du.coef_penalty].stakersProfit)
#sum(du[du.ly_totROI>du.coef_penalty+10].stakersProfit)
#sum(du[(du.ly_totROI>du.coef_penalty)&(du.ly_avBI*1.3>du.ABI)].stakersProfit)
#sum(du[(du.ly_totROI>du.coef_penalty)&(du.ly_tournaments>500)].stakersProfit)
#sum(du[(du.ly_totROI>du.coef_penalty)&(du.ly_tournaments>500)&(du.ly_avBI*1.7>du.ABI)].stakersProfit)
#sum(du[(du.ly_totROI>du.coef_penalty)&(du.ly_avBI*1.7>du.ABI)&(du.roi>du.coef_penalty)].stakersProfit)
#

###Build graph for stakers profit based on deals selected by strategy:
x = du[(du.ly_totROI>du.coef_penalty)&(du.ly_tournaments>500)\
&(du.ly_avBI*1.7>du.ABI)&(du.tot_totROI > du.coef_penalty+10)]

#x = du[(du.ly_totROI>du.coef_penalty)\
#&(du.ly_avBI*1.7>du.ABI)&(du.roi > 0)]

#x = du[(du.roi>du.coef_penalty)&(du.abi*1.2>du.ABI)]

df = simulateStrategy(x,500)
train,test = splitData(du,0.2)
#s = x[['start_date','stakersProfit']]
#s.start_date = pd.to_datetime(s.start_date, format="%d.%m.%Y")
#s = s.groupby(['start_date']).sum()
#s.stakersProfit = s.stakersProfit.cumsum()
#s.plot()