# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 17:35:10 2022

@author: artem
"""

import requests

from random import choice

url = 'http://httpbin.org/user-agent'

while line := open('user_agent.txt').read().split('\n'):
    user_agent = {'user-agent': choice(line)}
    response = requests.get(url=url, headers=user_agent)
    print(response.text)