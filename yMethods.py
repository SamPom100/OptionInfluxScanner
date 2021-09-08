from numpy import single
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
print(optionChain)
optionStrikes = ticker.option_chain(optionChain[2])
calls = optionStrikes.calls.nlargest(10, 'volume')
calls = calls.drop(["volume","lastTradeDate","strike","lastPrice","bid","ask","openInterest","impliedVolatility","inTheMoney","contractSize","currency","change","percentChange"],axis=1)

#column of DataFrame into list
callsList = []
for x in calls.values.tolist():
    callsList.append(x[0])

def singleData(optionID):
    data = yf.download([optionID])
    data = data.drop(["Open", "High", "Low", "Close", "Adj Close"], axis=1)
    data.plot()
    plt.show()
    return data

#get single option data

#for id in callsList:
    temp = singleData(id)
    print(temp)
    

d1 = (singleData(callsList[0]))
d2 = (singleData(callsList[1]))

result = d1.append(d2)
result.plot()
print(result)
plt.show()