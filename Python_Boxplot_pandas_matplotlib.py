# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 19:31:38 2014

@author: laml
"""

#problem 3.3a
import pandas as pd #plot graph
import matplotlib.pyplot as plt #ylabel
#read file into data2 variable
file = '/Users/laml/Documents/Fall 2014/ESD.754 Data Mining/HW1/LaptopSalesJanuary2008.txt'
data2 = pd.read_csv(file, sep='\t', index_col='Date', parse_dates=True)
#create pivot table for Retail Price values categorized by Store Postcode
#plot as bar graph
#data2.pivot_table(values='Retail Price', index=['Store Postcode']).plot(kind='bar', title="Mean Retail Price per Store Postcode", legend=True)
#print data2[data2['Store Postcode']=='W4 3PH']
data2[data2['Store Postcode']==('N17 6QA')].append(data2[data2['Store Postcode']==('W4 3PH')]).boxplot(column='Retail Price',by='Store Postcode',rot='90')
#label y
plt.ylabel("Retail Price")