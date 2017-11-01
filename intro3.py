"""
https://www.youtube.com/watch?v=2BrpKpWwT2A&index=1&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ
Intro and Getting Stock Price Data - Python Programming for Finance p.1

getting daily OHLCV from yahoo for a specific symbol
"""
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#start = dt.datetime(2000,1,1)
#end =dt.datetime(2016,12,31)

#df = web.DataReader('TSLA','yahoo', start, end)
#print (df.head()) #by defualt it will print top 5 lines but i can adjsut to more lines
#print (df.head(50)) #i can adjsut to more lines

#print (df.tail()) #can get end of file

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

#print(df[['Open','Close']].head())
#df['Close'].plot()
#plt.show

df['100ma'] = df['Adj Close'].rolling(window=100).mean()#adding a column to calculate last 100 points - moving avarge
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()#same as above but on the first 99 days it will calcualte the avg till than and not creat "nan"

#df.dropna(inplace=True)#if i am getting "ana" due to problems i can remove them from the data frame


print(df.tail())































