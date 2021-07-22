from typing import Any, Union
from unittest import result

from pandas import Series, DataFrame
from pandas.core.generic import NDFrame
from pandas.io.parsers import TextFileReader


def my_function(stockp, stockp2):
    print("The Companies used for this anaysis of Stocks are " + stockp + " & "  + stockp2 +".")
my_function(stockp="Twitter", stockp2="Facebook")

import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TWTR&interval=5min&apikey=KNW1AQQH38EIKDV3'
r = requests.get(url)
data = r.json()

print(data)

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=FB&interval=5min&apikey=KNW1AQQH38EIKDV3'
r = requests.get(url)
data = r.json()

print(data)

import pandas as pd

Twit = pd.read_csv("facebook_data.csv")
FB = pd.read_csv("twtr_data.csv")

Merge = Twit.append(FB, sort=False)
print(Merge)

Merge.sort_values(by='adj_close', ascending=False, inplace=True)
print(Merge)

Merge.dropna(subset=['date'], inplace=True)
print(Merge)

result = []
for value in Merge["adj_close"]:

    if value >= 300:
        result.append("$300+")
    else:
        result.append("<$300")

Merge["Result"] = result
print(Merge)

Merge['adj_high'] = Merge['adj_high'].round(1)
Merge['adj_low'] = Merge['adj_low'].round(1)
Merge['adj_open'] = Merge['adj_open'].round(1)
Merge['adj_close'] = Merge['adj_close'].round(1)
print(Merge)