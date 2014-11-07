# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 08:59:10 2014

stream data from yahoo with date and time
write output to csv file

@author: laml
"""
#allows date plot
import pandas as pd
from pandas import DataFrame
#allows plt.show
import matplotlib.pyplot as plt

#for yahoo finance datetime
import datetime
import pandas.io.data
sp500 = pd.io.data.get_data_yahoo('%5EGSPC', start = datetime.datetime (2000, 10, 1), end = datetime.datetime (2014, 6, 11))

#shows first 5x sample size to screen
print sp500.head()

#write to csv
sp500.to_csv('sp500_file.csv')

#plots using matplotlib however no dates
#sp500.plot('High')

#plots using pandas with dates
sp500['Close'].plot()
#plt.show()