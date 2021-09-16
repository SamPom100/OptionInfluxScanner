from numpy import single
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os


def printFrame(frame):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(frame)

def singleData(optionID):
        data = yf.download([optionID])
        data = data.drop(["Open", "High", "Low", "Close", "Adj Close"], axis=1)
        return data

ticker = yf.Ticker("MSFT")
dates = ticker.options

mergeFrame = pd.DataFrame()

for i in range(len(dates)):
    optionStrikes = ticker.option_chain(dates[i])
    calls = optionStrikes.calls.nlargest(10, 'volume')
    calls = calls.drop(["lastTradeDate","strike","lastPrice","bid","ask","openInterest","impliedVolatility","inTheMoney","contractSize","currency","change","percentChange"],axis=1)
    mergeFrame = mergeFrame.append(calls)
    if len(mergeFrame) == 0:
        mergeFrame = calls

largestCalls = mergeFrame.nlargest(10, 'volume')
callsList = []
for x in largestCalls.values.tolist():
    callsList.append(x[0])


frame = singleData(callsList[0])
sys.stdout = open(os.devnull, "w")
for x in range(len(callsList)-4):
    tmpFrame = singleData(callsList[x+1])
    tmpFrame.rename(columns={"Volume":str(callsList[x])}, inplace=True)
    frame = pd.merge(frame,tmpFrame, on="Date")
sys.stdout = sys.__stdout__
printFrame(frame)