

import yfinance as yf

price = yf.Ticker('ATCO-A')
price = price.info['regularMarketPrice']

print(price)