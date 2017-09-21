# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:50:08 2017

@author: Александр
"""
import time
import os
import re
import urllib.request
from selenium import webdriver

driver = webdriver.Firefox()
with open ('urls.txt', mode = 'r') as file:
    lines = file.readlines()

for line in lines:
    
    driver.get(line)
    
    images = driver.find_elements_by_tag_name('img')
    
    for image in images:
        src = image.get_attribute('src')
        if 'fpimage' in src:
            imgUrl = src
    
    imgUrl = imgUrl.replace("true", "false")
    Expression = re.compile('/\w*@')
    SearchObject = Expression.search(imgUrl)
    FoundString = SearchObject.group()
    FoundString = FoundString.replace('/', '')
    PN = FoundString.replace('@', '')
    
    driver.get(imgUrl)
    
    image = driver.find_element_by_tag_name('img')
    src = image.get_attribute('src')
    fullfilename = os.path.join('E:\Smal Molecules\Pics', PN + '.png')
    urllib.request.urlretrieve(src, fullfilename)

        
time.sleep(5)
driver.quit()
