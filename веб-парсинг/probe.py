# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:06:03 2022

@author: artem
"""

from selenium import webdriver

url = 'https://stepik.org/'
browser = webdriver.Chrome()
browser.get(url)