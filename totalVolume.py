from numpy import single
from pandas.io.clipboards import read_clipboard
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
pd.set_option('display.float_format', lambda x: '%.2f' % x)


def printFrame(frame):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(frame)

def singleData(optionID):
        data = yf.download([optionID])
        data["Spent"] = data["Adj Close"]*data["Volume"]
        data = data.drop(["Volume","Open", "High", "Low", "Close", "Adj Close"], axis=1)
        return data

ticker = yf.Ticker("AAPL")
dates = ticker.options

optionStrikes = ticker.option_chain(dates[0])
calls = optionStrikes.calls

calls = calls.nlargest(15, 'volume')
callsList = []
for x in calls.values.tolist():
    callsList.append(x[0])

mergeFrame = singleData(callsList[0])
mergeFrame.rename(columns={"Spent":str(callsList[0])}, inplace=True)

for i in range(len(callsList)-1):
        tmpFrame = singleData(callsList[i+1])
        tmpFrame.rename(columns={"Spent":str(callsList[i+1])}, inplace=True)
        mergeFrame = pd.merge(mergeFrame, tmpFrame, on='Date',how='left')

mergeFrame = mergeFrame.fillna(0)
mergeFrame["sumRows"] = mergeFrame.sum(axis=1)
print(mergeFrame)

new = mergeFrame[['sumRows']].copy()
printFrame(new)
new.plot()
plt.show()