# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 15:17:03 2014

@author: laml
"""
# array and mathematical manipulation, file import
import numpy as np
# plotting
#import pylab as pl
#allows plt.show
import matplotlib.pyplot as plt

#file import
import pandas as pd
#DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. 
#from pandas import DataFrame
#import matplotlib.dates as mdates

#for yahoo finance datetime
#import datetime
#import pandas.io.data
#sp500 = pd.io.data.get_data_yahoo('%5EGSPC', start = datetime.datetime (2000, 10, 1), end = datetime.datetime (2014, 6, 11))
#print sp500

#loadtxt only when NOT missing values
#date,value = np.loadtxt("testdata.txt", converters={0:mdates.strpdate2num('%d%m%Y %H:%M:%S')}))
file = '/Users/laml/Documents/Fall 2014/ESD.754 Data Mining/HW1/LaptopSalesJanuary2008.txt'
test = '/Users/laml/Documents/Fall 2014/ESD.754 Data Mining/HW1/testdata.txt'
#genfromtxt load with missing values but homogeneous data only
#data1 = np.genfromtxt('testdata.txt', dtype=None, delimiter='\t')
# assumes 1st line is header unless specified as header=None, heterogeneous data
data2 = pd.read_csv(file, sep='\t', index_col='Date', parse_dates=True)
                   # converters={0:mdates.strpdate2num('%d%m%Y %H:%M:%S')})

#prints first 5x rows
#data2.head()

#prints column names
#print data2["Store Postcode"]
#print(data2.columns)
#print data2[['Retail Price','Configuration']]


#pandas to plot so dates are preserved
#data2[['Configuration','Retail Price']].plot()
#data2[['Retail Price', 'Configuration']].plot()
#data2[['Retail Price','Configuration']]


td=pd.read_csv(test, sep='\t', index_col='Date', parse_dates=True)

#calculating mean
np.mean(td['Retail Price'])

#plot bar chart
#plt.bar(td['Store Postcode'],td['Configuration'])

#plot line chart
plt.plot(td['Retail Price'],td['Configuration'])
#plt.plot(td['Retail Price'])


#plots using matplotlib however no dates
#data2.plot('Retail Price')


#renames column names
#data2.columns=('a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p')

#creates bar chart
#data2.plot(data2.Date, kind='bar')
# plot the first column as x, and second column as y
#plt.plot(data2[:,0],data2[:,5],'rD')
#plt.xlabel('x')
#plt.ylabel('y')
#pl.xlim(0.0, 10.)
#plt.show()
