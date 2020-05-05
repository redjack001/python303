# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:22:00 2020

@author: redjack001
"""


import requests
import webbrowser  


response = requests.get("https://api.nasa.gov/planetary/apod?api_key=IHdzZJerwjQZTQhBpexoXoKBcsyLG9q49PmeXzs6",
  headers={
    "date": "2020-05-05",
    "hd": "False",
    "api_key": "DEMO_KEY"
  }
)

print(response)

# convert json to Python object 
data = response.json()

print(data)


txt = 'url'

if txt in data:
    print("Element Found in Dict")
    pos = list(data)
    print(data[txt])
    webbrowser.open(data[txt], new=0, autoraise=True)    
    
else:
    print("Element not Found in Dict")    