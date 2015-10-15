# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:47:15 2015

@author: Nikolay_Semyachkin
"""
import time
from selenium import webdriver

#driver = webdriver.Chrome('D:\Data Science\Poker staking data\chromedriver.exe')
driver = webdriver.Firefox()


driver.get("https://mttmarket.com/packets/list?status=complete")
driver.maximize_window()
x = driver.find_element_by_link_text('Show more')
#x = driver.find_element_by_link_text('Show more')
for i in range(1000):
    x.click()
#        time.sleep(0.5)
    


#driver.refresh()
#driver.find_element_by_class_name("b-btn b-btn__white b-btn__white__big").click()
#driver.findElement(By.cssSelector("b-btn__white__big"));
#x = driver.find_element_by_link_text('Show more')
#for i in range(100):
#    x.click()
#    time.sleep(0.3)
#driver.close()