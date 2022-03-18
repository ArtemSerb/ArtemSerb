# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 20:06:17 2022

@author: artem
"""

print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
percent=int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people=int(input("How many people to split the bill?"))
allOf=(bill/people)*(1+percent/100)
final=round(allOf, 2)
print(final)