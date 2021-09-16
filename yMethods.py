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
for x in range(len(optionChain)):
    optionStrikes = ticker.option_chain(optionChain[x])
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

    frame = singleData(callsList[0])

    for x in range(len(callsList)-4):
        tmpFrame = singleData(callsList[x+1])
        tmpFrame.rename(columns={"Volume":str(callsList[x])}, inplace=True)
        frame = pd.merge(frame,tmpFrame, on="Date")

    print(frame)
    frame.plot()
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()