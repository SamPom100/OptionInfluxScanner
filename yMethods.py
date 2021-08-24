import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)

ticker = yf.Ticker("MSFT")

#get option dates
optionChain = ticker.options
for date in optionChain:
    pass

#get top 10 volume options for single date
optionStrikes = ticker.option_chain(optionChain[10])
calls = optionStrikes.calls.nlargest(10, 'volume')
calls = calls.drop(["volume","lastTradeDate","strike","lastPrice","bid","ask","openInterest","impliedVolatility","inTheMoney","contractSize","currency","change","percentChange"],axis=1)

#column of DataFrame into list
callsList = []
for x in calls.values.tolist():
    callsList.append(x[0])

def singleData(optionID):
    data = yf.download([optionID])
    data = data.drop(["Open", "High", "Low", "Close", "Adj Close"], axis=1)
    return data

#get single option data
for id in callsList:
    temp = singleData(id)
    temp.plot()
    plt.show()
    plt.clf()


