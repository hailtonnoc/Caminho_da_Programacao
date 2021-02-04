import pandas as pd
import pandas_datareader as pdr

!pip install yfinance --upgrade --no-cache-dir
import yfinance as yf
yf.pdr_override()

df = pdr.datareader('CSNA3','yahoo','2020-10-01','2020-10-15')

print(df.head(), df.tail())

