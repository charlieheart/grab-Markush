# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 07:36:26 2017

@author: Александр
"""
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

entries = 25 #sets the number of entries to be extracted

driver = webdriver.Firefox()
driver.get('https://patentscope.wipo.int/search/en/search.jsf')
search = driver.find_element_by_name('simpleSearchSearchForm:fpSearch')
search.clear()
search.send_keys('Formula (I)')
search.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.ID, 'resultTable:0:resultListTableColumnLink')))

open('urls.txt', 'w').close()

def grablinks(n):
    for i in range (n):
        
        linkElement = driver.find_element_by_id(
                'resultTable:' + str(i) + ':resultListTableColumnLink')
        url = linkElement.get_attribute('outerHTML')
        Expression = re.compile('detail\.jsf\?docId=\w*&amp')
        SearchObject = Expression.search(str(url))
        FoundString = SearchObject.group()
        FoundString = FoundString.replace('&amp', '')
        url = 'https://patentscope.wipo.int/search/en/' + FoundString
        with open ('urls.txt', mode = 'a') as file:
            file.write (url + '\n') 

def nextpage():
    nextElement = driver.find_element_by_xpath(
            "//*[contains(text(), 'next')]")
    nextElement.click()       

while entries > 10:
    grablinks(10)
    nextpage()
    entries -=10
else:
    grablinks(entries)
    

time.sleep(5)
driver.quit()
