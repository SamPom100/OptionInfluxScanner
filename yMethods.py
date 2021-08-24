import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = yf.Ticker("MSFT")

#get options
#print(ticker.options)
#print(ticker.option_chain("2021-09-17"))

#TODO get 10 most active options
data = yf.download(['MSFT210917C00260000'])
data1 = data.drop(["Open","High","Low","Adj Close", "Volume"], axis=1)
data2 = data.drop(["Open","High","Low","Adj Close", "Close"], axis=1)

#TODO overlay both graphs
data1.plot()
data2.plot()

plt.show()
print("done")