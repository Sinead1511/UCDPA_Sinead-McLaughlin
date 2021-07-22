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

FB = pd.read_csv("facebook_data.csv")
Twit = pd.read_csv("twtr_data.csv")

Merge = Twit.append(FB, sort=False)

Merge.sort_values(by='adj_close', ascending=False, inplace=True)

Merge.dropna(subset=['date'], inplace=True)

result = []
for value in Merge["adj_close"]:

    if value >= 50:
        result.append("$50+")
    else:
        result.append("<$50")

Merge["Result"] = result

Merge['adj_high'] = Merge['adj_high'].round(1)
Merge['adj_low'] = Merge['adj_low'].round(1)
Merge['adj_open'] = Merge['adj_open'].round(1)
Merge['adj_close'] = Merge['adj_close'].round(1)
print(Merge)

List = ['Twitter', 'Facebook']
print("\nList with the use of Mixed Values: ")
print("The companies used in this project are: ", end="")
print(List)

import numpy as np

list_1 = [69.08, 348.64]
array_1 = np.array(list_1)
print("Twitter & Facebook SP on 22nd July 21 are: ", end="")
print(array_1)

Merge.drop_duplicates(subset=['adj_close', 'adj_open'])
print(Merge)

OverUnder = Merge['adj_close'].groupby(Merge['Result'])
print(OverUnder)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 10))

Mergefilt = Merge[(Merge.Result == '<$50')]

sns.set(style="darkgrid")
plots = sns.barplot(x="symbol", y="adj_close", data=Mergefilt)

for bar in plots.patches:
    plots.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=20, xytext=(0, 20),
                   textcoords='offset points')

plt.xlabel("Company", size=11)
plt.ylabel("Closing Share Price", size=11)
plt.title("Average Stock Price of <$50 cohort")
plt.show()

plt.figure(figsize=(10, 10))

Mergefilt1 = Merge[(Merge.Result == '$50+')]

sns.set(style="darkgrid")
plots = sns.barplot(x="symbol", y="adj_close", data=Mergefilt1)

for bar in plots.patches:
    plots.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=20, xytext=(0, 20),
                   textcoords='offset points')

plt.xlabel("Company", size=11)
plt.ylabel("Closing Share Price", size=11)
plt.title("Average Stock Price of $50+ cohort")
plt.show()

FB['adj_close'] = FB['adj_close'].round(1)
print("Facebook max SP is: $", end="")
FBSPmax = FB['adj_close'].max()
print(FBSPmax)

Twit['adj_close'] = Twit['adj_close'].round(1)
print("Twitter max SP is: $", end="")
TwitSPmax = Twit['adj_close'].max()
print(TwitSPmax)

FB['adj_close'] = FB['adj_close'].round(1)
print("Facebook min SP is: $", end="")
FBSPmin = FB['adj_close'].min()
print(FBSPmin)

Twit['adj_close'] = Twit['adj_close'].round(1)
print("Twitter min SP is: $", end="")
TwitSPmin = Twit['adj_close'].min()
print(TwitSPmin)

print("Facebook max SP is higher than Twitter max SP by: $", end="")
TwitSPdiff = FBSPmax - TwitSPmax
TwitSPdiffRD = TwitSPdiff.round(1)
print(TwitSPdiffRD)