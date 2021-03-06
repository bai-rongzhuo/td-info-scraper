# -*- coding: utf-8 -*-
"""htn

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lNtUCHEtEt1fcZn5J2OzrapXoJNIlrDm
"""

import requests
import json
from flask import Flask
import datetime
#from dateutil.parser import parse
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/banana")
def banana():
    return "Hello World!"

response = requests.get('https://api.td-davinci.com/api/customers/0096e7fb-b384-4dc2-a6b0-3faf6de5686b_c18dca28-f10f-4a0a-b905-db636046bd4c/transactions',
    headers = { 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiZThmZGM2ZWQtOWVmMi0zZTViLWFjNzItYzAzZGUyNWY2ZDYzIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiIwMDk2ZTdmYi1iMzg0LTRkYzItYTZiMC0zZmFmNmRlNTY4NmIifQ.lN1DmnXacItZYY63EGTZPiXXeh7UIKx-55X6NOwlX0g'})
response_data = response.json()

#print(response_data)

transactions = []

for dic in response_data['result']:
  s = dic.items()
  inlist = []
  #print(s)
  for key, value in s:
    if key == "description":
      inlist.append(value)
    if key == "type":
      inlist.append(value)
    if key == "currencyAmount":
      inlist.append(value)
    if key == "originationDateTime":
      if len(value) > 20:
        d = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
      else:
        d = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")      
      inlist.append(d)
    if key == "categoryTags":
      inlist.append(value)
    if key == "merchantCategoryCode":
      inlist.append(value)
  transactions.append(inlist)

transactions.sort(key=lambda x: x[3])
transactions = transactions[::-1]

monthly = []



with open('data.json', 'w') as outfile:
    json.dump(response_data, outfile)

