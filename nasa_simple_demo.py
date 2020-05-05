# -*- coding: utf-8 -*-
"""
Created on Tue May  5 01:05:14 2020

@author: redjack001
"""


import requests
import webbrowser


response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")

print(response)

data = response.json()

txt = 'url'

if txt in data:
    print("Element Found in Dict")
    pos = list(data)
    print(data[txt])
    webbrowser.open(data[txt], new=0, autoraise=True)    
    
else:
    print("Element not Found in Dict")    