# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 17:11:38 2015

@author: Nikolay_Semyachkin
"""
from bs4 import BeautifulSoup

data = open("MttMarket.html", encoding='utf8')
soup = BeautifulSoup(data)

hhh = soup.find_all('tr')
print(hhh[1].td.get_text())
