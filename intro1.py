"""
https://www.youtube.com/watch?v=2BrpKpWwT2A&index=1&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ
Intro and Getting Stock Price Data - Python Programming for Finance p.1

"""
import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end =dt.datetime(2016,12,31)

df = web.DataReader('TSLA','yahoo', start, end)
#print (df.head()) #by defualt it will print top 5 lines but i can adjsut to more lines
print (df.head(50)) #i can adjsut to more lines
print (df.tail(50)) #can get end of file