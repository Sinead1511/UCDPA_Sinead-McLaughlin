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

