# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 14:38:55 2022

@author: artem
"""
from bs4 import BeautifulSoup

with open("./index2.html") as file:
    src = file.read()
#print(src)
    
soup = BeautifulSoup(src, "lxml")

#title = soup.title
#print(title)
#print(title.text)

#page_h1 = soup.find("h1")

#user_name = soup.find("div", class_ = 'user__name')
#print(user_name.text.strip(

#social_links = soup.find(class_ = "social__networks").find("ul").find_all("a")
#for item in social_links:
  #  item_url = item.get("href")
  #  print(item_url)
  