# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 17:05:35 2022

@author: artem
"""

from random import choice
import requests

url = 'http://httpbin.org/ip'

with open('proxy.txt') as file:
    proxy_file = file.read().split('\n')
    for _ in range(1000):
        try:
            ip = choice(proxy_file).strip()
            proxy = {
                'http': f'http://{ip}',
                'https': f'http://{ip}'
            }
            response = requests.get(url=url, proxies=proxy)
            print(response.json(), 'Success connection')
        except Exception as _ex:
            continue