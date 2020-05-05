# -*- coding: utf-8 -*-
"""
Created on Tue May  5 01:05:14 2020

@author: legomate
"""


import requests


response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")

print(response)

data = response.json()
print(data)
print(type(data))