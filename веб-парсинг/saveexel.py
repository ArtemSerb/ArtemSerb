# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:46:42 2022

@author: artem
"""

from bs4 import BeautifulSoup
import requests
import lxml
import csv

data_list = []
def get_response(num_category: int, num_page: int) -> str:
    '''
    This is a function for get response.
    The input is two integers (category number, page number).
    The get_response function returns the text code of the page.
    '''
    response = requests.get(f'https://parsinger.ru/html/index{num_category}_page_{num_page}.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

def create_dataframe(soup: str):
    '''This is a procedure which parsing data'''
    #list names
    names = [name.text.strip() for name in soup.find_all('a', class_='name_item')]
    # list discriptions
    discriptions = [[item.text.split(':')[1].strip() for item in disc.find_all('li')] \
                    for disc in soup.find_all('div', class_='description')]
    # list prices
    prices = [price.text.strip() for price in soup.find_all('p', class_='price')]
    # create data rows and add push it into data_list
    for n, d, p in zip(names, discriptions, prices):
        data_list.append([n] + d + [p])

#Проходим в циклах по всем страницам всех категорий товаров
for i in range(1, 6):
    for j in range(1, 5):
        create_dataframe(get_response(i, j))

#Создаём файл и загружаем данные в него
with open('price_list_all.csv', 'w', encoding='utf-8-sig', newline='') as new_file:
    writer = csv.writer(new_file, delimiter=';')
    for row in data_list:
        writer.writerow(row)