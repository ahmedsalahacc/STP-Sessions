# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hyfgoATmrC_DXaz-aaO6KM22O6_fU6O4
"""

import requests

payload = {"entry.1971603035":"Ahmed", "entry.984349283":"Salah", "entry.1718339407":22}

def send_request():
  response = requests.post('https://docs.google.com/forms/u/0/d/e/1FAIpQLScux88fcYzqQr8nIhTy8DyAISdfL6rvHfy7OASgqMikFLcU-A/formResponse', data=payload)
  print(response)

for i in range(1000):
  send_request()

